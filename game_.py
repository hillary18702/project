#printing range of numbers from 1 to 101
# number=float(input("Enter the number "))
# fizbuzz=[]
# fizz=[]
# buzz=[]

for i in range (1, 50):

#checks if the number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        # fizbuzz.append(i)
        print("fizzbuzz ")

#checks if the number is divible by 3
    elif i % 3 == 0:
        # fizz.append(i)
        print("fizz ")

#checks if the number is divisble by 5
    elif i % 5== 0: 
        # buzz.append(i) 
        print("buzz ")

    else:
        print(i)

    # print(i)

# print("FizzBuzz: ", fizbuzz)
# print("Buzz: ", buzz)
# print("Fizz: ", fizz)    

