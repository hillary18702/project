import jwt
Customers=[
    {
        "name":"Hillary oswago",
        "customer_id":"38918344",
        "username": "oswago",
        "password": "876",
        "id_or_passport": "555444",
        "current_balance": "100000",
        "Citizenship":"Kenyan",
        "customer_location":{
            "region":"Nyanza",
            "county":"Homabay",
            "sub-county":"Rachuonyo north",
            "location": "Kanyaluo east",
            "sub_location": "Kowuor east",
        },
    },
    {
        "name":"Vincent  Mireri",
        "customer_id":"23918344",
        "username": "Mireri",
        "password": "876",
        "id_or_passport": "655444",
        "current_balance": "900000",
        "Citizenship":"Kenyan",
        "customer_location":{
            "region":"Nyanza",
            "county":"Homabay",
            "sub-county":"Rachuonyo north",
            "location": "Kanyaluo east",
            "sub_location": "Kowuor east",
                },
    },
    {
        "name":"John ouma",
        "username": "ouma",
        "customer_id":"38918344",
        "password": "876qer",
        "id_or_passport": "555444",
        "current_balance": "100000",
        "Citizenship":"Kenyan",
        "customer_location":{
            "region":"Nyanza",
            "county":"Homabay",
            "sub-county":"Rachuonyo north",
            "location": "Kanyaluo east",
            "sub_location": "Kowuor east",
                },
    },
]


# Prepare customer account balances and transaction histories
for customer in Customers:
    customer["current_balance"] = float(customer["current_balance"])
    customer.setdefault("transactions", [])


# 1. LOGIN 
def login(customers):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    token=None

    for customer in customers:
        if (customer["username"] == username.lower()
                and customer["password"] == password):
            payload={
                "username": customer['username'],
                "fullname": customer["name"]
            }
            secret="DAGo5678912345678912345fghytrscv"
            token= jwt.encode(payload, secret, algorithm="HS256")
            print(token)
            print("Login successful!")
            print("Welcome ", customer["name"])
            return customer

    print("Incorrect username or password.")
    print("System stopped.")
    return token


# 2. BANK STATEMENT FUNCTION
def bank_statement(customer):
    print("BANK STATEMENT ")
    print("Customer name:", customer["name"])
    print("Customer ID:", customer["customer_id"])

    if len(customer["transactions"]) == 0:
        print("No transactions have been recorded.")

    else:
        for transaction in customer["transactions"]:
        
            print("Type:", transaction["type"])
            print("Amount:", transaction["amount"])
            print("Balance after transaction:",
                  transaction["balance"])

    
    print("Current balance:", customer["current_balance"])


# 3. CHECK BALANCE FUNCTION
def check_balance(customer):
    print("ACCOUNT BALANCE")
    print("Account holder:", customer["name"])
    print("Current balance:", customer["current_balance"])


# 4. WITHDRAW FUNCTION
def withdraw(customer):
    print("WITHDRAW MONEY")

    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Amount must be greater than zero.")

        elif amount > customer["current_balance"]:
            print("Insufficient funds.")

        else:
            customer["current_balance"] -= amount

            customer["transactions"].append({
                "type": "Withdrawal",
                "amount": amount,
                "balance": customer["current_balance"]
            })

            print("Withdrawal successful!")
            print("Amount withdrawn:", amount)
            print("Remaining balance:",
                  customer["current_balance"])

    except ValueError:
        print("Invalid amount. Please enter a number.")


# 5. DEPOSIT FUNCTION
def deposit(customer):
    print("DEPOSIT MONEY ")

    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Amount must be greater than zero.")

        else:
            customer["current_balance"] += amount

            customer["transactions"].append({
                "type": "Deposit",
                "amount": amount,
                "balance": customer["current_balance"]
            })

            print("Deposit successful!")
            print("Amount deposited:", amount)
            print("New balance:",
                  customer["current_balance"])

    except ValueError:
        print("Invalid amount. Please enter a number.")


# 6. MAIN PROGRAM
logged_in_customer = login(Customers)

if logged_in_customer is not None:

    while True:
        print("ACTIVITIES")
        print("1. Bank statement")
        print("2. Check balance")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Exit")

        choice = input("Choose an activity (1-5): ")

        if choice == "1":
            bank_statement(logged_in_customer)

        elif choice == "2":
            check_balance(logged_in_customer)

        elif choice == "3":
            withdraw(logged_in_customer)

        elif choice == "4":
            deposit(logged_in_customer)

        elif choice == "5":
            print("Thank you for banking with us.")
            print("Goodbye", logged_in_customer["name"])
            break

        else:
            print("Invalid choice. Please select from 1 to 5.")
