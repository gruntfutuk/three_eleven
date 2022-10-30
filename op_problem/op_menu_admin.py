# I suggest using a dictionary to hold a menu
# you can include name of function to call as well
# e.g. {"1": ("Display Statistics" display_stat), ...}
# for Exit, use None instead of a function name and check for it
def menu_admin():
    print("[1] Display Statistics")
    print("[2] Add an Employee")
    print("[3] Display all Employees")
    print("[4] Change Employee’s Salary")
    print("[5] Remove Employee")
    print("[6] Raise Employee’s Salary")
    print("[7] Exit")

def admin_actions(records):

    menu_admin()

    # use "1" instead of 1, no need for int if not doing maths


    while True:
        option = int(input("Hello admin, enter your option: "))
        if option == 1:
            print("show salary")
        elif option == 2:
            print("add")
        elif option == 3:
            print("Display")
        elif option == 4:
            print("Change salary")
        elif option == 5:
            print("remove")
        elif option == 6:
            print("raise")
        elif option == 7:
            print("exit")
            break
        else:
            print("invalid option,please choose between 1 and 7")
