print("welcome to shadow.com")
#Let the user input their password
password=input("enter your password: ")

#check password length
password_length = len(password)

has_uppercase = False
has_lowercase = False
has_digit = False

# password="!P0rlfav0r"
for char in password:
    if char.isupper():
        has_uppercase= True

    elif char.islower():
        has_lowercase= True

    elif char.isdigit():
        has_digit= True

if password_length >=8 and has_uppercase and has_lowercase and has_digit:
    print("password is strong")

elif password_length >=8:
    print("password is fair")

else:
    print("password strength is weak")
