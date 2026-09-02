import math
def area_triangle():
    base = float(input("Enter the base length: "))
    height = float(input ("Enter the base height: "))
    if base < 0 and height < 0:
        print("invalid numbers please check")
        return
    area = 0.5 * base * height
    print("the area of triangle is: ",area)

def area_square():
    side = float(input("Enter the side length: "))
    if side < 0:
        print("invalid number please check")
        return
    area = side*side
    print("the area of square is: ",area)
def area_rectangle():
    length = float(input("Enter the length: "))
    breadth = float(input("Enter the breadth: "))
    if length < 0 and breadth <0:
        print("invalid number please check")
        return
    area = length * breadth
    print("the area of rectangle is: ",area)
def area_circle():
    radius = float(input("Enter the radius: "))
    if radius < 0:
        print("invalid number please check")
        return
    area = math.pi * (r * r)
print("Please select the shape")
print("1. Triangle")
print("2. Square")
print("3. Rectangle")
print("4. circle")

while True :
    choice = input("Enter choice(1/2/3/4): ")
    if choice not in ('1', '2', '3', '4'):
        print("choose the correct option")
    elif choice == "1":
        area_triangle()
    elif choice == "2":
        area_square()
    elif choice == "3":
        area_rectangle()
    elif choice == "4":
        area_circle()
    elif choice == "5":
        break
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        print("Goodbye! Thanks for using the Area Calculator.")
        break

area_triangle
area_square
area_rectangle
area_circle
