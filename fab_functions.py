# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".
print()
def f1(name):
    print("hello "+ name )#this function is printing hello with name which was inputed
f1('bob')
print()
# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.
def sum_numbers(a,b):
    print(a+b)#this function is adding 2 numbers together
sum_numbers(1,2)
print()
# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.
def factorial(n):
    nnn=1
    while n>1:#this function is finding factiorial by multiplication
        nnn= nnn*n
        print(nnn)
        n-=1
factorial(12)
print()
# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.
def is_even(num):
        second=(num%2)
        if second == 1:#this function is cheking if number is odd or even
         print(False)
        else:
          print(True)


is_even(1)
print()
# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.
def calculate_area(length,withd):
    n=length * withd#this function is calculating
    print(n)
calculate_area(38,22)