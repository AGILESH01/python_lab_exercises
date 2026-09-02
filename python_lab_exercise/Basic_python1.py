Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2=2
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 2==2
True
>>> 2.2
2.2
>>> 2
2
>>> [2.5]
[2.5]
>>> "Python"
'Python'
>>> Python
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Python
NameError: name 'Python' is not defined
>>> 5>3
True
>>> '5'>3
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    '5'>3
TypeError: '>' not supported between instances of 'str' and 'int'
>>> 5*2
10
>>> abc*3
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    abc*3
NameError: name 'abc' is not defined. Did you mean: 'abs'?
>>> 'abc'*3
'abcabcabc'
>>> 'abc'+'abc'
'abcabc'
>>> print(hello world)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("hello world")
hello world
>>> a in abc
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a in abc
NameError: name 'a' is not defined
>>> letter = a
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    letter = a
NameError: name 'a' is not defined
letter = "a"
a in letter
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a in letter
NameError: name 'a' is not defined
50%3
2
50/3
16.666666666666668
50//3
16
3**3
27
3*3
9
1234*789
973626
5+'4'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    5+'4'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
5+4
9
"4"+'5'
'45'
"4"+a
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    "4"+a
NameError: name 'a' is not defined
'6'+'a'
'6a'
'python'*'vscode'
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    'python'*'vscode'
TypeError: can't multiply sequence by non-int of type 'str'
'python'*4
'pythonpythonpythonpython'
'python'*4
'pythonpythonpythonpython'
car = 'ev'
car
'ev'
y = abcd
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    y = abcd
NameError: name 'abcd' is not defined
y = 'abcd'
a in 'abcd'
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a in 'abcd'
NameError: name 'a' is not defined
a in y
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a in y
NameError: name 'a' is not defined
a in 'y'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a in 'y'
NameError: name 'a' is not defined
a in abcd
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a in abcd
NameError: name 'a' is not defined
print(2 in (1,2,3))
True
print(a in (1,2,3))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(a in (1,2,3))
NameError: name 'a' is not defined
print(A in abcd)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(A in abcd)
NameError: name 'A' is not defined
x = 3
x += 3
print(x)
6
x-=3
print(x)
3
x,y = 10, 20
x<5 , y < 20
(False, False)

=========================================== RESTART: /Users/agil/Desktop/python_lab_exercise/Basic_python.py ===========================================
enter number a: 3
enter number b: 5
8
a = "AGIL"
len(a)
4
