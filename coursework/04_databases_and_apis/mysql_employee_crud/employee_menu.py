# Console front end for the employee table: opens the connection once, then
# loops on a menu calling the CRUD functions in employee_dao.py.

import sys

import employee_dao as emp

# tabulate draws the table with box characters the default Windows console
# cannot encode, so printing it would fail.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main():
    connection = emp.connect_db()

    if connection:
        emp.create_table(connection)

        while True:
            print("\nMENU:")
            print("1. View All Employees")
            print("2. Insert New Employee")
            print("3. Update Existing Employee")
            print("4. Delete Employee")
            print("5. Exit")

            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                emp.read_all_employees(connection)
            elif choice == 2:
                emp.insert_employee(connection)
            elif choice == 3:
                emp.update_employee(connection)
            elif choice == 4:
                emp.delete_employee(connection)
            elif choice == 5:
                emp.disconnect_db(connection)
                break
            else:
                print("Invalid Choice")


if __name__ == "__main__":
    main()