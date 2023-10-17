try:#this part is cheking if user inputed number correclty
 age = int(input('Enter your age: '))
 faveNum = int(input('What is your favorite number: '))
except:
 print("you inputed something diffent from number")
if age <= 21:
 print('You are not allowed to enter, you are too young.')
else:
 print('Welcome, you are old enough.')

try:#this part of code is using this try function to see if there is a error here it will do thing in except.
  print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except: 
  print('You migth putted 0 as your favorite number? If yes do again but different number')