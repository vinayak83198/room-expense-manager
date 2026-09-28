from database import execute_query , fetch_query
from datetime import datetime

def get_name():
    while True:
        name = input("Enter your name: ").strip()
    
        if not name:
            print("Name cannot be empty")
        elif not name.isalpha():
            print("Name should contain only letters")
        else:
            break
    return name

def get_item():
    while True:
        item = input("Enter the item name: ").strip()
        if not item:
            print("item can not be empty")
        else:
            break

    return item

def get_price():
    while True:
        try:
            price = int(input("Enter your price: "))
    
            if price > 0:
                break
            else:
                print("Please write a positive price")
    
        except ValueError:
            print("Please enter a valid number")
    return price

def get_date():
    while True:
        try:
            date = input("Enter the date: ")
            datetime.strptime(date, "%d/%m/%Y")
            break
    
        except ValueError:
            print("Please enter a valid date in DD/MM/YYYY format.")
                
    return date



def add_Expenses():
   
    name = get_name()
    item = get_item()
    price = get_price()
    date = get_date()
    
    execute_query(
        "INSERT INTO expenses (name, item, price, date) VALUES (?, ?, ?, ?)",
        (name, item, price, date)
    )


def show_Expenses():
    rows = fetch_query("""
        SELECT * FROM expenses
    """)
    print(f"{'ID':<5}{'Name':<12}{'Item':<15}{'Price':<10}{'Date':<12}")
    print("-" * 50)
    for row in rows:
        print(f"{row[0]:<5}{row[1]:<12}{row[2]:<15}{row[3]:<10}{row[4]:<12}")


def total_Expenses():
    result = fetch_query("""
        SELECT SUM(price) FROM expenses
    """)

    print(result[0][0])

def Person_wise_Expenses():

    rows = fetch_query("""
        SELECT name, SUM(price)
        FROM expenses
        GROUP BY name
    """)

    for row in rows:
        print(f"{row[0]},{row[1]}")

    return rows

def monthly_settlement():
    person_wise = Person_wise_Expenses()
    if not person_wise:
        print("No Expenses found")
        return 
    
    total_Expenses = 0
    for row in person_wise:
        total_Expenses  += row[1]

    number_of_people = len(person_wise)

    equal_share = total_Expenses / number_of_people

    print(f"Total Expense: ₹{total_Expenses}")
    print(f"Number of People: {number_of_people}")
    print(f"Each Person Should Pay: ₹{equal_share}")

    for row in person_wise:
        person = row[0]
        paid = row[1]

        diff = paid - equal_share

        if diff > 0:
            print(f"{person} → Receive ₹{diff:.2f}")
        elif diff < 0:
            print(f"{person} → Pay ₹{-diff:.2f}")
        else:
            print(f"{person} → Settled")

    
def delete_Expenses():
    expenses_id = get_positive_number()

    deleted_rows = execute_query(
        "DELETE FROM expenses WHERE id = ?",
        (expenses_id,)
    )

    if deleted_rows > 0:
        print("Expenses deleted successfully")
    else:
        print("Expenses id not found")



def update_Expenses():
    expenses_price = get_positive_number()
    expenses_id = get_positive_number()

    updated_row = execute_query("""
        UPDATE expenses
        SET price = ?
        WHERE id = ?
        """,
        (expenses_price, expenses_id)
    )

    if updated_row > 0:
        print("Expenses updated successfully")
    else:
        print("Expenses id not found")


def get_positive_number():

    while True:
        try:
            number = int(input("Enter a positive number: "))

            if number > 0:
                return number
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Please enter a valid number.")