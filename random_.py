from random import randint
# import random as rand



# if random_number == choose_int:
#     print("Congratulations. you got it")

# else:
#     print("oops! you missed. keep trying")
#     print("The correct number was ", random_number)  
attemps=0

while True:
    random_number = randint(1,10)
    choose_int= int(input("Choose a number from 1 and 10: "))
    

    if random_number  == choose_int:
        attemps = attemps+1
        print("Congratulations. You got it ")
        print("Attemps ", attemps)
        break

    else:
        attemps = attemps+1
        print("Oops! you missed. keep trying ") 
        print("The correct number was", random_number)
        print("Try again!")
        print("Attemps ", attemps)
        continue                 