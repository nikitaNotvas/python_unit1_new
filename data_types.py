
#TASK 1:
#Create a float variable, and then convert it to an integer
#Print both the original variable and the converted integer.

floats=12.2
print(int(floats)) 
#comment:I used int to convert float to integer, while float was converted it became 12 insted of 12.2

#TASK 2:
#Write code that takes a number as input and prints whether 
#it's positive, negative, or zero using if-elif-else statements.

number=int(input("enter number here"))#user enters number here 
if number == 0: # this part determens if number is 0 or not 
    print('your number is 0')
elif number <= 0:# if number is less than 0 it will say its negative other wise it will say its positeve
    print("your number is negative ")
else: print('your number is positve')


#TASK 3:

#Write code that takes two numbers as input (an integer and a float), 
#performs addition, subtraction, multiplication, and division, and prints the results.

interger=int(input("enter interger here "))#user puts integer here
floatss=float(input("enter float here "))#user puts float here
print(interger+floatss)#this is addion of users inputs
print(interger-floatss)#this is subtraction of users inputs
print(interger*floatss)#this is multiplication of users inputs
print(interger/floatss)#this is division of users inputs



#TASK 4:

#Create a dictionary with keys as fruit names and values as their respective quantities. 
#Then print out the quantity of one of the fruits.


fruts={
    'Apples':8,#this is dictionary where several things are placed
    'Potato':9

}
print(fruts["Apples"])    #this part will print quantity of one of the fruits

#TASK 5:

#Create a string variable with that is a list of numbers and convert that string into a tuple.
#Then print out the both the original string and tuple.

myString=('1,2,3,5,6,7')#this is string with numbers which will be convernted to turple
myTubple=myString.split(",") #this is how string is converted to tubple 
print(myTubple)#this part prints result of conversion