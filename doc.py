from random import randint
attemps=0
while True:
    random_number=randint(1,15)
    #choose any random number to play the game 
    Choose_int = int(input("Chosse a number from 1 to 15: "))
    #if the choosen number is correct, returns congratulations
    if Choose_int == random_number:
        attemps= attemps+1
        print("congratulations. you got it ")
        print("Attemps ",attemps)
        break
    else:
        #displays a failed message when the choosen number is wrong
        print("Oop!. you missed")
        #informs the user to try again
        print("Try again!")
        #displays the correct number for the user
        print("The correct number is" ,random_number)
        #shows the number of attempts and adds the number by 1 everytime an attempt is made
        attemps= attemps+1
        print("Attemps " , attemps)
        continue


