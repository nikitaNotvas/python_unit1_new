
import datetime
#here i imported modular which helps to deal with time

#Exercise 1:
#Write a Python program that prints the current date and time using the datetime module.
print(datetime.datetime.now())
print("---")
#this part is uses datetime function to show time now 


#Exercise 2:
#Write a Python program that prints the current date and time using the datetime module.
#Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
x = datetime.datetime.now()
#this part is storing tine in x for later uses
print(x.strftime("%D"))
print(x.strftime("%T"))
print("---")
#this part here is uses only date in one line and time in differnet line

#Exercise 3:
#Using the strptime function, convert two strings into dates.
#Then find the difference in days between the two.
import datetime
from datetime import datetime
it2= "21 February, 2018"
it1= "23 February, 2018"
dd1=datetime.strptime(it2, "%d %B, %Y")
dd2=datetime.strptime(it1, "%d %B, %Y")

print(dd2-dd1)


#Excercise 4:
#Write a program that asks the user for their birthdate and calculates their current 
#age using the datetime module.

x1=(x.strftime("%Y"))#this part is showing this year
age=input("enter your age: ")#here user are inputing their age
bd=(int(x1) - eval(age))#here it calculates year they were born

print(bd)
