import math
#TASK 1 Even or Odd
#Determine if a number is even or odd.

first=int(input('enter your number: '))
second=(first%2)
if second == 1:
    print("your number is odd")
else:#this part is deviding number equali on differnt parts and if something left it means that number is odd becuase you cannot devied odds by 2
    print('your number is even')

#TASK 2 Positive, Negative, or Zero:
#Determine if a number is positive, negative, or zero.

#EXTRA CREDIT: Tell the user if they did not enter a valid number

third=int(input('enter number here: '))
if third >= 1:
    print('your number is positive')
elif third <= -1:#the inputed number is checked if number is above -1 or below it 
    print('your number is negative ')
else:
    print('your number is 0')


#TASK 3: Largest of Three
#Find and print the largest of three numbers.

yzy=int(input('give me number '))
yxy=int(input('give me number '))
ycy=int(input('give me number '))
action=max(yzy,yxy,ycy)
print(action)#here all of the numbers are compered and cheked if there a bigger number

#TASK 4: Leap Year
#Determine if a year is a leap year or not.
ff=int(input('please enter year: '))
if ff % 4==0:
     print('it is a leap year')
else: print('it is not a leap year')


#TASK 5: Vowel or Consonant:
#Identify if a character is a vowel or consonant.

#EXTRA CREDIT: Tell the user if they did not enter a valid letter
four=input('enter one letter ')
letters=['a','A','e','E','i','I','o','O','u','U']#all of those letters are cheked if they are same as vowel or not
if (four == letters ):
        print("Vowel")
else:
        print("Consonant")


