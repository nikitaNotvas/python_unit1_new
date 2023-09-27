
#Exercise 1:
#Check if an integer is even and greater than 10.
#Return True if both conditions are met, False otherwise.
a=int(input("enter your number: "))
b=(a%2)
if b == 0:
    if a>=10:
        print("True")
    else:
        print("False")
else:
        print("False")

#Exercise 2:
#Determine the ticket price based on age and student status.
#Price is $10 if under 18 or a student, $20 otherwise.

c=int(input("enter you age: "))
d=str(input("are you student or no: Y/N"))
if c <=18 and c >= 0 or d == "Y":
     print("your price for ticket is $18")
else:
     print("your price for ticket is $20")
#Exercise 3:
#Prompt the user to enter a fruit name. Check if the fruit is in the list. 
#If it is, print "Yes, that fruit is in the list." 
#If it's not, print "No, that fruit is not in the list."
fruit =["apple","mango","orange","strawberry","banana","watermelon","kiwi"]
useri=input("enter one fruit: ")
if useri==fruit:
     print("Yes, that fruit is in the list")
else:
    print("No, that fruit is not in the list")


#Exercise 4:
#Check if a year is a century year and a leap year.

userii=input("Enter year: ")

if int(userii)%4==0 and int(userii) %100 ==0:
     print("your year is a century and a leap year")
else:
     print("your year is not a century and leap year")



#Exercise 5:
#Calculate the cost of shipping for an online order based on the order weight and destination zone. 
#The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
#If the order weight is less than 0 kg, return an error message.

ent=int(input("weithg of packeg: "))
entt=input("area of delivery: ")

if ent==0:
   print("ERROR")  
elif entt == "A":
     print(ent*5)
elif entt=="B":
     print(ent*7)



#Exercise 6:
#Determine the type of a triangle based on side lengths.
#Equilateral, Isosceles, Scalene, or Not a triangle.
