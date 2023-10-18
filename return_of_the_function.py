
#Task 1: Calculate the Square of a Number
#Write a function that takes an integer as an argument and returns its square.

def calculatorofsquare(num1):
    return(num1*num1)

g=calculatorofsquare(9)

assert g == 81

try:
    assert calculatorofsquare == 4
except:
    print("there is a mistake ")

#Task 2: Calculate the Area of a Rectangle:
#Write a function that takes the length and width of a rectangle and returns its area.

def calculatorofrectangle(l,w):
  return(l*w)

gg=calculatorofrectangle(4,6)

assert gg == 24
try:
    assert calculatorofrectangle == 25
except:
    print("there is a mistake")

#Task 3: Convert Temperature from Celsius to Fahrenheit:
#Write a function that takes a temperature in Celsius and returns 
#the equivalent temperature in Fahrenheit using the correct formula


def calculatorofctof(c):
    return((c*9/5)+32)
calculatorofctof(10)

assert calculatorofctof(0) == 32
try:
    assert calculatorofctof(0)== 33
except:
    print("there is a mistake")
#Task 4: Calculate the Average of Numbers:
#Write a function that takes a list of numbers 
#and returns the average (mean) of those numbers.

def calculatorofaveragenum(lst):   
    sslist=sum(lst)/len(lst)
    return sslist

coollist=calculatorofaveragenum([20,30,400,50,20120])
print(coollist)
assert coollist == 4124
try:
    assert coollist==4125
except:
    print("you made mistake")