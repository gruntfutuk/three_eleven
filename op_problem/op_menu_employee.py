def salary(record):
    s = record['salary']
    print(s)


def exit():
    print("system will exit")


# suggest use dictionary for menu
def menu_employee():
    print("[1] Check my Salary")
    print("[2] Exit")

def employee_actions(record):

    menu_employee()

    # use "1" instead of 1, no need for int if not doing maths

    while True:
        option = int(input("Hello Mr. ali enter your option: "))
        if option == 1:
            salary(record)
        elif option == 2:
            break
        else:
            print("invalid option,please choose 1 or 2")
