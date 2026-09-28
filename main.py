import expense
def main():
    print("ROOM EXPENSE MANGER")

    print("1 : Add Expenses")
    print("2 : Show Expenses")
    print("3 : Total Expenses")
    print("4 : Person_wise Expenses")
    print("5 : Monthly Settlement")
    print("6 : Delete Expenses")
    print("7 : Update Expenses")
    print("8 : Exit")

    while True:

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                expense.add_Expenses()

            elif choice == 2:
                expense.show_Expenses()

            elif choice == 3:
                expense.total_Expenses()

            elif choice == 4:
                expense.Person_wise_Expenses()

            elif choice == 5:
                expense.monthly_settlement()

            elif choice == 6:
                expense.delete_Expenses()

            elif choice == 7:
                expense.update_Expenses()

            elif choice == 8:
                print("Exit..Good Bye!")
                break

            else:
                print("Please enter a choice between 1 and 8.")
                
        except ValueError:
            print("Enter valid number")

if __name__ == "__main__":
    main()