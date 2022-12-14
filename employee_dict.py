import csv
from pathlib import Path
from password_func import hash_password, password_bad, generate_password, DEFAULT_PASSWORD


def employee_create(
        first: str,
        last: str,
        other: str,
        grade: str,
        salary: int,
        position: str='',
        password: str=DEFAULT_PASSWORD):
    if not isinstance(salary, int):
        try:
            salary = int(salary)
        except ValueError:
            raise ValueError('Salary was not a number')
    hashed_password = hash_password(password)
    return {"first": first,
        "last": last,
        "other": other,
        "grade": grade,
        "salary": salary,
        "position": position,
        "password": hashed_password}

def report(employee: dict):  # for printing a record
    bad_password = password_bad(employee['password'])
    return (f'Employee: {employee["last"]}, {employee["first"]}.\n'
            f'\tGrade: {employee["grade"]}, Position: {employee["position"]}\n'
            f'\tSalary: £{employee["salary"]}\n'
            f'\tDefault/empty/bad password: {bad_password}')

def line(employee: dict):  # for saving to csv format
    return (f'{employee["first"]},{employee["last"]},{employee["other"]},'
           f'{employee["grade"]},{employee["salary"]},{employee["position"]},{employee["password"]}')

def row(employee: dict):  # convert string of employee record to list for csv
    return line(employee).split(',')

def key(employee: dict):
    """create a unique key for each employee based on all name fields """
    return f'{employee["last"]}_{employee["first"]}_{employee["other"]}'.casefold()


def save_employees(filename: Path, employees: list):
    """ save dictionary of Employee records to a CSV file """
    if employees:  # check there's data to save, assume the data is valid
        with filename.open('w') as file:  # open file (new or overwrite)
            writer = csv.writer(file)  # writing in csv format
            for employee in employees.values():  # retrieve each Employee record
                writer.writerow(row(employee))  # convert record to list of fields for CSV and write

def read_employees(filename: Path):
    """ read Employee records from CSV into dictionary of Employee records"""
    employees: dict = {}  # start with empty dictionary
    if filename.is_file():  # make sure there is a file, lets assume we can read it
        with filename.open() as file:
            reader = csv.reader(file)
            for idx, row in enumerate(reader):  # need a row number for error reporting
                try:  # attempt to convert row from csv data into an Employee record
                    new_employee = employee_create(*row)
                except TypeError:  # probably too few/many fields on the row
                    print(f'Bad Record - row {idx}: {row}')
                except ValueError as err:  # probably failed check there is a number for salary
                    print(f'Bad Record - row {idx}: {row}')
                    print(err)
                else:  # add new Employee record to dictionary if not duplicate name
                    if not add_employee(new_employee, employees):
                        print(f'Duplicate Name - row {idx}: {row}')

    return employees  # dictionary of Employee records

def add_employee(new_employee: dict, employees: list):
    keyid = key(new_employee)  # generate unique key for potential new employee
    if keyid in employees:  # check key is unique, if not retain False
        return False
    employees[keyid] = new_employee  # otherwise add employee to dictionary of Employee records
    return True  # and return True to indicate new employee was added succesfully


def report_all(employees: dict, report_header: str = "\n\nEmployees:\n", report_footer: str = ""):
    """ print details of all Employee records in dictionary """
    print(report_header)
    for employee in employees.values():
        print()
        print(report(employee))
    print(report_footer)


filename = Path('employees.csv')

employees = read_employees(filename)  # see if we have employee data filed already
if employees:
    report_all(employees, "\nEmployee details read from file:\n")

# lets try to add some additional employees
new_emps = (employee_create('Fred', "Bloggs", "William", "S5", 23_000, "Junior Chef"),
            employee_create('Barry', "Smoth", "", "S6", 18_000, "Washer"),
            employee_create('Alpha', "Beta", "Charlie", "S2", 43_000, "CFO", generate_password())
            )

for employee in new_emps:
    if add_employee(employee, employees):
        print('\nAdded employee')
    else:
        print('\nEmployee already on file - details not updated')
    print(report(employee))

save_employees(filename, employees)
report_all(employees, '\n\nSaved to file Employee Details:\n')
