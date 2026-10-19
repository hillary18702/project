from math import pi

#Function to calculate area of a circle
def area_of_circle(radius):
    return pi * radius **2

#Function to calculate area of a square 
def area_of_square(side):
    return side **2

#Function to calculate area of a rectangle 
def area_of_rectangle(length, width):
    return length*width

#Function to calculate the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * (base*height)

#Function to calculate area of a trapezium
def area_of_trapezium(longer_side,shorter_side,height):
    return 0.5* ((longer_side+shorter_side)*height)

#calculation
print("AREA CALCULATOR")
print("circle")
print("triangle")
print("square")
print("rectangle")
print("trapezium")

choice = input("choose the shape(circle, triangle, square, rectangle, trapezium): ")
if choice == "circle":
    radius=float(input("Enter radius: "))
    print("Area of circle: =", area_of_circle(radius))

elif choice == "triangle":
    base=float(input("Enter base: "))
    height=float(input("Enter height: "))
    print("Area of triangle: =", area_of_triangle(base,height))

elif choice =="square":
    side=float(input("Enter side: "))
    print("Area of square: =", area_of_square(side))

elif choice =="rectangle":
    length=float(input("Enter length: "))
    width=float(input("Enter width: "))
    print("Area of rectangle: =",area_of_rectangle(length,width))

elif choice== "trapezium":
    longer_side=float(input("Enter longer_side: "))
    shorter_side=float(input("Enter shorter_side: "))
    height=float(input("Enter height: "))
    print("Area of trapezium: =", area_of_trapezium(longer_side,shorter_side,height))
else:
    print("invalid choice, choose 1 to 4(triangle, circle, rectangle, square)")

    

