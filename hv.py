a=float(input("Enter firts number: "))
b=float(input("Enter second number: "))
c=float(input("Enter third number: "))
operation_symbol= input("provide an operation symbol(+,-,/,*,^)")
answer=0
counter=0
def add(a,b,c):
    result= a+b+c
    # counter+=1
    return result


def subtract(a,b,c):
    result = (a-b)-c
    # counter+=1
    return result

def divide(a,b,c):
    result= (a/b)/c
    # counter+=1
    return result

def multiply(a,b,c):
    result = a*b*c
    # counter+=1
    return result

def raise_to_power(a,b,c):
    result = (a**b)**c
    # counter+=1
    return result

if operation_symbol=='+':
    answer=add(a,b,c)

elif operation_symbol== "-":
    answer=subtract(a,b,c)

elif operation_symbol=="*":
    answer=multiply(a,b,c)

elif operation_symbol=='/':
    answer=divide(a,b,c)

elif operation_symbol=='^':
    answer=raise_to_power(a,b,c)

else:
    print('provide a valid operation symbol')

print(f"Answer: {answer}")
# print(f"Counter: {counter}")





