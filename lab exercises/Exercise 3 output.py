Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

============================================ RESTART: /Users/agil/Desktop/python_lab_exercise/Exercise 3.py ============================================
Please select the shape
1. Triangle
2. Square
3. Rectangle
4. Circle
Enter choice(1/2/3/4): 1
Enter the base length: 2
Enter the base height: 3
the area of triangle is:  3.0
Enter choice(1/2/3/4): 4
Enter the radius: 3
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/Exercise 3.py", line 51, in <module>
    area_circle()
  File "/Users/agil/Desktop/python_lab_exercise/Exercise 3.py", line 32, in area_circle
    area = math.pi * (r * r)
NameError: name 'r' is not defined

============================================ RESTART: /Users/agil/Desktop/python_lab_exercise/Exercise 3.py ============================================
Please select the shape
1. Triangle
2. Square
3. Rectangle
4. Circle
Enter choice(1/2/3/4): 3
Enter the length: 2
Enter the breadth: 
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/Exercise 3.py", line 40, in <module>
    area_rectangle()
  File "/Users/agil/Desktop/python_lab_exercise/Exercise 3.py", line 17, in area_rectangle
    breadth = float(input("Enter the breadth: "))
ValueError: could not convert string to float: ''

============================================ RESTART: /Users/agil/Desktop/python_lab_exercise/Exercise 3.py ============================================
Please select the shape
1. Triangle
2. Square
3. Rectangle
4. Circle
Enter choice(1/2/3/4): 2
Enter the side length: 3
the area of square is:  9.0
Enter choice(1/2/3/4): 2
Enter the side length: 1
the area of square is:  1.0
Enter choice(1/2/3/4): 4
Enter the radius: 3
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/Exercise 3.py", line 42, in <module>
    area_circle()
  File "/Users/agil/Desktop/python_lab_exercise/Exercise 3.py", line 23, in area_circle
    area = math.pi * radius / (radius - radius)
ZeroDivisionError: float division by zero

============================================ RESTART: /Users/agil/Desktop/python_lab_exercise/Exercise 3.py ============================================
Please select the shape
1. Triangle
2. Square
3. Rectangle
4. Circle
Enter choice(1/2/3/4): 2
Enter the side length: 3
the area of square is:  9.0
Enter choice(1/2/3/4): 3
Enter the length: 2
Enter the breadth: 3
the area of rectangle is:  6.0
Enter choice(1/2/3/4): 1
Enter the base length: 3
Enter the base height: 4
the area of triangle is:  6.0
Enter choice(1/2/3/4): 4
Enter the radius: 0
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/Exercise 3.py", line 42, in <module>
    area_circle()
  File "/Users/agil/Desktop/python_lab_exercise/Exercise 3.py", line 23, in area_circle
    area = math.pi * radius / (radius - radius)
ZeroDivisionError: float division by zero
>>> 
============================================ RESTART: /Users/agil/Desktop/python_lab_exercise/Exercise 3.py ============================================
Please select the shape
1. Triangle
2. Square
3. Rectangle
4. Circle
Enter choice(1/2/3/4): 4
Enter the radius: 4
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/Exercise 3.py", line 42, in <module>
    area_circle()
  File "/Users/agil/Desktop/python_lab_exercise/Exercise 3.py", line 23, in area_circle
    area = math.pi * radius / (radius - radius)
ZeroDivisionError: float division by zero
>>> 
============================================ RESTART: /Users/agil/Desktop/python_lab_exercise/Exercise 3.py ============================================
Please select the shape
1. Triangle
2. Square
3. Rectangle
4. Circle
Enter choice(1/2/3/4): 2
Enter the side length: 1
the area of square is:  1.0
Enter choice(1/2/3/4): 23
choose the correct option
Enter choice(1/2/3/4): 1.0
choose the correct option
Enter choice(1/2/3/4): 2
Enter the side length: 4
the area of square is:  16.0
Enter choice(1/2/3/4): 4
Enter the radius: 
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/Exercise 3.py", line 42, in <module>
    area_circle()
  File "/Users/agil/Desktop/python_lab_exercise/Exercise 3.py", line 23, in area_circle
    area = math.pi * (radius * radius)
TypeError: can't multiply sequence by non-int of type 'str'
