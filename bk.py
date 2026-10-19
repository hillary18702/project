#logging in 
correct_username="Hillary"
correct_password= "shadow123"

print("Welcome!! please log in: ")

username=input("Enter correct username: ")
password=input("Enter correct password: ")

if username==correct_username and password==correct_password:
    print("login successful: ")
else:
    print("incorrect username or password, login failed: ")

#Display Activities
print("ACTIVITIES")
print(1, "Bank statement")
print(2, "Check balance")
print(3, "Withdraw")
print(4,"Deposit")


choice=input(int("Choose the activity you want to perform:(1-4): "))

customers=[
    {
        "name": "Ouma Arera",
        "id_or_passport": "36354738",
        "customer_id": "DB123",
        "current_balance": 40000
    },
    {
        "name": "Hillary Oswago",
        "id_or_passport": "389182",
        "customer_id": "DB124",
        "current_balance": 70000
    },
    {
        "name": "Agnes Atieno",
        "id_or_passport": "20020023",
        "customer_id": "DB125",
        "current_balance": 23756
    }
]

def change_customer_balance(new_balance, cust_id):
    for customer in customers:
        if cust_id == customer["customer_id"]:
            customer["current_balance"]=new_balance


def get_customer_balance(customer_id):
    balance = 0
    for customer in customers:
        if customer["customer_id"] == customer_id:
            balance = customer["current_balance"]
    return balance 

def withdraw(cust_id):
    amount=float(input("Enter the amount to withdraw: "))
    current_balance= get_customer_balance(cust_id)
    print("Initial Balane: ", current_balance)
    if amount > current_balance:
        print(f"You have insufficient funds to withdraw {amount}")
        print("Current balance: ", current_balance)
    else:
        new_balance= current_balance-amount
        change_customer_balance(new_balance, cust_id)
        print("Transaction successful!")
        print(f"You have withdrawn {amount}")
        print(f"New Balance: {get_customer_balance(cust_id)}")

# customer_id = input("Enter your customer")
act = withdraw("DB124")




# else:
#     new_balance = current_balance - amount
#     change_customer_balance(new_balance, cust_id)

#     # Record the transaction
#     for customer in customers:
#         if customer["customer_id"] == cust_id:
#             customer["transactions"].append({
#                 "type": "Withdrawal",
#                 "amount": amount
#             })
#             break

#     print("Transaction successful!")
#     print(f"You have withdrawn {amount}")
#     print(f"New Balance: {get_customer_balance(cust_id)}")
