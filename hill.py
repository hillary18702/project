print("LARRY-TECH")
password=input("enter your password")
#let the user input thier password

password_length=len(password)
#checking requirements
has_uppercase=False
has_lowercase=False
has_digit=False

for char in password:
    if char.isupper():
        has_uppercase = True

    elif char.islower():
        has_lowercase = True

    elif char.isdigit():
        has_digit = True

if password_length >= 8 and has_uppercase and has_lowercase and has_digit:
    print("password is strong")

elif password_length >= 8:
    print("password is fair")

else:
    print("password is weak")
    



