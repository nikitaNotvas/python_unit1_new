
#Exercise 1:
#Write a program to print numbers from 1 to 10 using a for loop.

for x in range(11):
    print(x)#this part of code is adding 1 to x which is starting at 0 this is why its 11
    

print("----------------")
#Exercise 2:
#Write a program to count by 10s from 900 to 1000
for x in range(900, 1010, 10):#first number is starting point,second number is endpoint and last number is by what you are counting
 print(x)

print("----------------")

#Exercise 3:
#Write a program that counts form 1-100 by 9
for x in range(1, 101, 9):#same as one before but counting by 9 and if number greater than 101 it will stop on previos number
    print(x)

print("----------------")

#Exercise 4:
#Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
a=0
for x in range(1,11):#this part is setting range and starting point
 a+=x
 print(x)#this part is adding and counting total
print(a)
 



print("----------------")
#Excercise 5:
#Uncomment the following code and run it. Then answer the following:
#- What is the ouput of the code?

#- Explain the iterative process that this code executes to get that output


rows = 5
 
for i in range(rows):#this part is setting how many lines it will print 
     for j in range(i + 1):#this part is adding one star to the line 
         print('*', end=' ')#this part of the code is printing stars
     print()#this part is printing separet line thats is why each star is separt