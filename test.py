#creating a list of phone numbers 

list_of_phone_numbers=["0735535334 ","0756536773 ","0723434336"]
print(list_of_phone_numbers)

#adding elemnts in a list using append 
list_of_phone_numbers.append("0767635363 ")
print(list_of_phone_numbers)

#enabling the user to provide phone number
# provide_number = List_of_phone_numbers
# print("number exists")

# if provide_number== List_of_phone_numbers:
#     print("number exist")
# else:
#     print

search = input("Enter the number you want to search: ")

if search in list_of_phone_numbers:
    print("Number is in the inventory")

else:
    print("Number not found")
