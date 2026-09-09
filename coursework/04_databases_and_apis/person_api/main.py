"""FastAPI CRUD endpoints over the MySQL persons table. SQL lives in person_dao.py.

Run with:  uvicorn main:app --reload
"""

from contextlib import asynccontextmanager

from datetime import date
from typing import Literal

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field, field_validator

from person_dao import Db_operations, Person

persons = Db_operations()


class PersonIn(BaseModel):
    """Request body for POST and PUT. Types mirror the table, so bad input is
    rejected here with a 422 instead of failing in MySQL as a 500.
    """

    name: str = Field(min_length=1, max_length=32)
    gender: Literal["M", "F"]
    dob: date                                        # ISO format: YYYY-MM-DD
    location: str = Field(min_length=1, max_length=32)

    @field_validator("gender", mode="before")
    @classmethod
    def normalise_gender(cls, value):
        """Accept 'm'/'f' in either case; the column is a single character."""
        if isinstance(value, str):
            return value.strip().upper()
        return value


class PersonOut(PersonIn):
    """A stored person, i.e. the request fields plus the database id."""

    id: int


def to_person_out(row):
    """Map a row to the response model. Column order: id, name, gender,
    location, dob - location comes before dob.
    """
    return PersonOut(
        id=row[0],
        name=row[1],
        gender=row[2],
        location=row[3],
        dob=row[4],
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Make sure the table exists before the first request is served.
    persons.create_table()
    yield


app = FastAPI(
    title="Person CRUD API",
    description="CRUD REST API over a MySQL persons table.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


def get_person_or_404(person_id: int):
    row = persons.search_row(person_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return row


@app.post("/persons", response_model=PersonOut, status_code=201)
def create_person(body: PersonIn):
    new_person = Person(body.name, body.gender, body.dob, body.location)
    new_id = persons.insert_row(new_person)
    return to_person_out(get_person_or_404(new_id))


@app.get("/persons", response_model=list[PersonOut])
def list_persons():
    rows = persons.list_all_rows() or []
    return [to_person_out(row) for row in rows]


@app.get("/persons/{person_id}", response_model=PersonOut)
def read_person(person_id: int):
    return to_person_out(get_person_or_404(person_id))


@app.put("/persons/{person_id}", response_model=PersonOut)
def update_person(person_id: int, body: PersonIn):
    get_person_or_404(person_id)
    # Order must match the UPDATE statement: name, gender, location, dob, id.
    persons.update_row((body.name, body.gender, body.location, body.dob, person_id))
    return to_person_out(get_person_or_404(person_id))


@app.delete("/persons/{person_id}")
def delete_person(person_id: int):
    get_person_or_404(person_id)
    persons.delete_row(person_id)
    return {"message": "Person is deleted", "id": person_id}
