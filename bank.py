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
    }
]
def login(customers):
    username=input("Enter correct user name: ")
    password=input("Enter correct password: ")
    for customer in Customers:
        if (customer["username"]==username and customer["password"]==password):
            print("login successful: ")
            print("WELCOME", customer["name"])
            return customer

    
    print("incorrect username or password, invalid login: ")
    return None
#Run login 
logged_in_customer= login(Customers)

#procced only if login is successful
if logged_in_customer is None:
    print("System stopped, try again later: ")

#Display activities 
else: 
    logged_in_customer is not None

    print("ACTIVITIES")
    print("1. Bank statement: ")
    print("2. Check balance: ")
    print("3. Withdraw: ")
    print("4. Deposit: ")


choice = input("Choose the activity you want to perform (1-4): ")

if choice == "1":
     print("Displaying bank statement...")

elif choice == "2":
    print("Your current balance is:",
         logged_in_customer["current_balance"])

elif choice == "3":
    print("Proceeding to withdrawal...")

elif choice == "4":
    print("Proceeding to deposit...")

else:
    print("Invalid activity selected.")


    

def check_customer_balance(new_customer_balance,customer_id):
    for customer in Customers:
        if customer_id == customer("Customer_id"):
            customer["Current_balancee"]=new_customer_balance

def get_customer_balance(customer_id):
    balance=0
    for customer in Customers:
        if customer ["customer_id"]== customer_id:
            balance = customer["customer_id"]
        return balance




        
        

    