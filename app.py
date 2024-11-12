import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('calculator.db')
cursor = conn.cursor()

# Create table to store results
cursor.execute('''CREATE TABLE IF NOT EXISTS results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    operation TEXT,
                    result REAL)''')

def store_result(operation, result):
    """Store the operation and result in the database"""
    cursor.execute("INSERT INTO results (operation, result) VALUES (?, ?)", (operation, result))
    conn.commit()

def view_results():
    """View all results stored in the database"""
    cursor.execute("SELECT * FROM results")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Operation: {row[1]}, Result: {row[2]}")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Simple Calculator")
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View Results")
        print("6. Exit")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '1':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            result = add(x, y)
            operation = f"{x} + {y}"
            print(f"Result: {result}")
            store_result(operation, result)

        elif choice == '2':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            result = subtract(x, y)
            operation = f"{x} - {y}"
            print(f"Result: {result}")
            store_result(operation, result)

        elif choice == '3':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            result = multiply(x, y)
            operation = f"{x} * {y}"
            print(f"Result: {result}")
            store_result(operation, result)

        elif choice == '4':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            result = divide(x, y)
            operation = f"{x} / {y}"
            print(f"Result: {result}")
            store_result(operation, result)

        elif choice == '5':
            print("\nStored Results:")
            view_results()

        elif choice == '6':
            print("Exiting the calculator.")
            break

        else:
            print("Invalid input, please try again.")

# Start the calculator
calculator()

# Close the database connection
conn.close()
