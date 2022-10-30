from op_menu_employee import employee_actions
from op_menu_admin import admin_actions

from pathlib import Path

from pprint import pprint

def log_in(records, username=None, password=None):

    attempts = 4
    logged_in = ""

    while attempts > 0 and logged_in == "":

        username = password = ""
        while not username:
            username = input("enter username: ")
            password = input("enter password: ")

        if username == "admin" and password == "admin123123":
            print("welcome admin,you will be redirected to admin  menu")
            logged_in = "admin"
            continue

        if username in records and password == "":  # employee should leave pass empty
            print("welcome employee,you will be #redirected to employee menu")
            logged_in = "user"

        elif username not in records and password == "":
            print("Incorrect Username ")

        elif username in records and password != "":
            print("Incorrect Username")

        else:
            print("Incorrect Username and/or password, try again")

        attempts -= 1
        print(f"attempts left {attempts}")


    return logged_in, username



def read_file():
    with open(Path('data.txt')) as f:
        data = f.readlines()
    records = {}

    for r in data:  # Time complexity:O(n) since 1 for loop
        fields = r.split(",")
        id = fields[0]
        username = fields[1]
        date = fields[2]
        gender = fields[3]
        salary = fields[4]
        records[username] = {"id": id, "name": username, "date of joining": date, "gender": gender,
                          "salary": salary}  # use username as primary key since it is what employee use to log in

    pprint(records)
    return records

employees = read_file()
logged_in, username = log_in(employees)
if logged_in == "admin":
    admin_actions(employees)
elif logged_in == "user":
    employee_actions(employees[username])
else:
    print('goodbye')
