#creating my first calculator

print("welcome to shadow")
num1=float(input("enter the first number: "))
num2=float(input("enter the second number: "))
operation_symbol=input("provide the operation symbol (*,/,+,-): ") 
answer=None

if operation_symbol=="+":
    answer=num1+num2

elif operation_symbol=="-":
    answer=num1-num2

elif operation_symbol=="/":
    answer=num1/num2

elif operation_symbol=="*":
    answer=num1*num2

else: 
    answer="please provide a valid operation symbol"

print(answer)
