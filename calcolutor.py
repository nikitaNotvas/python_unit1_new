import math
print("Hello and welcome to calcolutor")
numone=int(input(print("please enter number:")))#first input
numtwo=int(input(print("please enter second number:")))#second input
print("")
print("")
print('choose one the optinonts to calculete')
print('Select operation:')
print('1. Addition')#+
print('2. Subtraction')#-
print('3. Multiplication')#*
print('4. Division')#/
print('5. Floor Division')#//
print('6. Exponential')#**
print('7. Remainder')#%

actct=int(input(print('enter action what you want to do:')))#this part is allowing user to choose what kind of math action they want to do



if actct==1:
    print(numone+numtwo)#this part is adding num 1 and num 2
elif actct==2:
    print(numone-numtwo)#this part is subtracting num 1 from num 2
elif actct==3:
    print(numone*numtwo)#this part is multiplication num 1 by num 2
elif actct==4:
    if numone == 0:#this is a if statement inside elif statement 
        print("you can't divide by zero")
    elif numtwo==0:#those parts check if user inputed 0 as number and if user did it will warn them 
        print("you can't divide by zero")
    else:
        print(numone/numtwo)#this part is division
    
elif actct==5:
    print(numone//numtwo)#this part is floor division:floor division is 
elif actct==6:
    print(numone**numtwo)#this part is the exponent 
elif actct==7:
    print(numone%numtwo)#this part is remainer:it divedes number by other number and tells you the left over number
else:
    print("you didnt choose action from list and so calculator can not do anything")