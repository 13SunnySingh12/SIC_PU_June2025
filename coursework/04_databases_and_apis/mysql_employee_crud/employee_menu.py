# Console front end for the employee table: opens the connection once, then
# loops on a menu calling the CRUD functions in employee_dao.py.

import sys

import employee_dao as emp

# The employee table is drawn with tabulate's box-drawing characters, which the
# default Windows console code page (cp1252) cannot encode - printing it would
# raise UnicodeEncodeError. Switching stdout to UTF-8 lets the table render.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def main():
    connection = emp.connect_db()
    if connection:
        emp.create_table(connection)

        while True:
            print("\n MENU:")
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