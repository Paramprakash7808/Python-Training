from employee import (add_employee,remove_employee,update_employee,find_employee,list_employees,search_employees)

while True:
    print("\nEmployee Management System")
    print("1.Add Employee")
    print("2.Remove Employee")
    print("3.Update Employee")
    print("4.Find Employee")
    print("5.List Employees")
    print("6.Search Employees")
    print("7.Exit")

    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        add_employee()
    elif choice == 2:
        remove_employee()
    elif choice == 3:
        update_employee()
    elif choice == 4:
        find_employee()
    elif choice == 5:
        list_employees()
    elif choice == 6:
        search_employees()
    elif choice == 7:
        print("Program exited safely.")
        break
    else:
        print("Invalid choice. Please select 1 to 7.")