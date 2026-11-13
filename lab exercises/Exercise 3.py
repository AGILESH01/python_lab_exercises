
import math

def area_triangle():
    base = float(input("Enter the base length: "))
    height = float(input("Enter the base height: "))
    area = 0.5 * base * height
    print("the area of triangle is: ", area)

def area_square():
    side = float(input("Enter the side length: "))
    area = side * side
    print("the area of square is: ", area)

def area_rectangle():
    length = float(input("Enter the length: "))
    breadth = float(input("Enter the breadth: "))
    area = length * breadth
    print("the area of rectangle is: ", area)

def area_circle():
    radius = input("Enter the radius: ")
    area = math.pi * (radius * radius)
    print("the area of circle is: ", area)

print("Please select the shape")
print("1. Triangle")
print("2. Square")
print("3. Rectangle")
print("4. Circle")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice == "1":
        area_triangle()
    elif choice == "2":
        area_square()
    elif choice == "3":
        area_rectangle()
    elif choice == "4":
        area_circle()
    else:
        print("choose the correct option")
