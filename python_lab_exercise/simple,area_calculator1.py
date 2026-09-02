Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

========================================= RESTART: /Users/agil/Desktop/python_lab_exercise/simple_calculator.py ========================================
please select an operation to perform
1. add
2. subtract
3. multiply
4. power
5. divide
Enter choice(1/2/3/4): 1
Enter first number: 2
Enter second number: 4
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/simple_calculator.py", line 30, in <module>
    print(num1, "+", num2, "=", add(num1, num2))
NameError: name 'num1' is not defined

========================================= RESTART: /Users/agil/Desktop/python_lab_exercise/simple_calculator.py ========================================
please select an operation to perform
1. add
2. subtract
3. multiply
4. power
5. divide
Enter choice(1/2/3/4): 1
Enter first number: 1
Enter second number: 2
1.0 + 2.0 = 3.0

========================================= RESTART: /Users/agil/Desktop/python_lab_exercise/simple_calculator.py ========================================
please select an operation to perform
1. add
2. subtract
3. multiply
4. power
5. divide
Enter choice(1/2/3/4): 3
Enter first number: 3456
Enter second number: 65432
3456.0 * 65432.0 = 226132992.0
Let's do next calculation? (yes/no): yes
Enter choice(1/2/3/4): 5
Enter choice(1/2/3/4): 5
Enter choice(1/2/3/4): 
========================================= RESTART: /Users/agil/Desktop/python_lab_exercise/simple_calculator.py ========================================
please select an operation to perform
1. add
2. subtract
3. multiply
4. power
5. divide
Enter choice(1/2/3/4): 5
choose the correct option
Enter choice(1/2/3/4): 2
Enter first number: 234'
Invalid input. Please enter a number.
Enter choice(1/2/3/4): 432
choose the correct option
Enter choice(1/2/3/4): 234
choose the correct option
Enter choice(1/2/3/4): 4
Enter first number: 3
Enter second number: 2
3.0 / 2.0 = 1.5
Let's do next calculation? (yes/no): 
========================================= RESTART: /Users/agil/Desktop/python_lab_exercise/simple_calculator.py ========================================
please select an operation to perform
1. add
2. subtract
3. multiply
4. power
5. divide
Enter choice(1/2/3/4): 5
choose the correct option
Enter choice(1/2/3/4): 32
choose the correct option
Enter choice(1/2/3/4): 3
Enter first number: 432d
Invalid input. Please enter a number.
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/simple_calculator.py", line 38, in <module>
    print(x, "*", y, "=", multiply(x, y))
NameError: name 'x' is not defined

========================================= RESTART: /Users/agil/Desktop/python_lab_exercise/simple_calculator.py ========================================
please select an operation to perform
1. add
2. subtract
3. multiply
4. power
5. divide
Enter choice(1/2/3/4): 3
Enter first number: 543d
Invalid input. Please enter a number.
Enter choice(1/2/3/4): 1
Enter first number: 3d
Invalid input. Please enter a number.
Enter choice(1/2/3/4): 3
Enter first number: 3
Enter second number: 36543
3.0 * 36543.0 = 109629.0
Let's do next calculation? (yes/no): no
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/simple_calculator.py", line 51, in <module>
    power(x,y)
  File "/Users/agil/Desktop/python_lab_exercise/simple_calculator.py", line 9, in power
    return x**y
OverflowError: (34, 'Result too large')

========================================= RESTART: /Users/agil/Desktop/python_lab_exercise/simple_calculator.py ========================================
please select an operation to perform
1. add
2. subtract
3. multiply
4. power
5. divide
Enter choice(1/2/3/4): 2
Enter first number: 123
Enter second number: 43
123.0 - 43.0 = 80.0
Let's do next calculation? (yes/no): no

========================================= RESTART: /Users/agil/Desktop/python_lab_exercise/simple_calculator.py ========================================
please select an operation to perform
1. add
2. subtract
3. multiply
4. power
5. divide
Enter choice(1/2/3/4): 
========================================= RESTART: /Users/agil/Desktop/python_lab_exercise/simple_calculator.py ========================================
please select an operation to perform
1. add
2. subtract
3. multiply
4. power
5. divide
Enter choice(1/2/3/4/5): 5
Enter first number: 324
Enter second number: 432
324.0 / 432.0 = 0.75
Let's do next calculation? (yes/no): yes
Enter choice(1/2/3/4/5): 4
Enter first number: 2345
Enter second number: 4321
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/simple_calculator.py", line 41, in <module>
    print(x, "**",y, "=", power(x,y))
  File "/Users/agil/Desktop/python_lab_exercise/simple_calculator.py", line 9, in power
    return x ** y
OverflowError: (34, 'Result too large')
>>> 
========================================== RESTART: /Users/agil/Desktop/python_lab_exercise/area_calculator.py =========================================
Please select the shape
1. Triangle
2. Square
3. Rectangle
4. circle
Enter choice(1/2/3/4): 6
choose the correct option
Let's do next calculation? (yes/no): yes
Enter choice(1/2/3/4): 5
choose the correct option
Let's do next calculation? (yes/no): yes
Enter choice(1/2/3/4): 1
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/area_calculator.py", line 43, in <module>
    calculate_circle_area()
NameError: name 'calculate_circle_area' is not defined
>>> 
========================================== RESTART: /Users/agil/Desktop/python_lab_exercise/area_calculator.py =========================================
Please select the shape
1. Triangle
2. Square
3. Rectangle
4. circle
Enter choice(1/2/3/4): 2
Enter the side length: 2
the area of square is:  4.0
Let's do next calculation? (yes/no): yes
Enter choice(1/2/3/4): 7
choose the correct option
Let's do next calculation? (yes/no): yes
Enter choice(1/2/3/4): 1
Enter the base length: d
Traceback (most recent call last):
  File "/Users/agil/Desktop/python_lab_exercise/area_calculator.py", line 43, in <module>
    area_triangle()
  File "/Users/agil/Desktop/python_lab_exercise/area_calculator.py", line 3, in area_triangle
    base = float(input("Enter the base length: "))
ValueError: could not convert string to float: 'd'
