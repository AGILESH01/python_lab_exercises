def fibonacci_iterative(n):
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

loop = int(input("Enter how many numbers you need for the series: "))

if loop <= 0:
    print("Negative numbers and zero are not allowed.")
else:
    result = fibonacci_iterative(loop)
    
    print("fibonacci series of ", loop , "is" , result)
  

