
#Task 1: People Class
#Define a class called Person with attributes name and age.
#Then, write a method within the class to introduce the person with their name and age.

#Create a new object using this new class, and call the method you created.

print("")
print("task 1")
print("")

class Person:
 type21="living creature"

 def __init__(self, name, age):#
       self.name = name#this is a part which holds your name
       self.age = age#this part is holding your age
 def hello(self):#this function is showing your name and age in one line
     print("hello "+ str(self.name), "your age is " +str(self.age))

nikita=Person("Nikita",22)#in this line you insert name and age and save class as working object
nikita.hello()

print("")
print("task 1")
print("")
#Task 2: Animals Speak
#Create a base class Animal with a empty method called speak. 

#Then create two subclasses, Dog and Cat, each with their own speak method. 


#Create objects using these subclasses and call the speak method.
print("")
print("task 2")
print("")


class Animal:#this a empty class 
    def __init__(self,speak):
        self.speak=speak

animal=Animal

class Dog(Animal):#empty class is getting transformed in class with bark sound
    def speak():
        print("bark")

animal=Dog

class Cat(Animal):#alredy transofrmedclass is getting transformed in another class which makes meow sound
    def speak():
        print("meow")

animal=Cat

animal.speak()


print("")
print("task 2")
print("")
#Task 3: Banking
#Create a class BankAccount with attributes balance and owner. 

#Include methods for depositing and withdrawing money, which should modify the balance attribute.

#Test these methods with instances of the class.

print("")
print("task 3")
print("")


class BankAccount:#this class is created to store money
    def __init__(self,balance,owner):
        self.balance = balance
        self.owner = owner

    def balances(self,dep):# this class is created tp add money into account
        self.balance=self.balance + dep
        print("here is your new deposid: ",self.balance)


    def withdrawing(self,wdraw):#this class is created to remove money from account
        self.balance = self.balance - wdraw
        print("here is your new deposid: ",self.balance)

#here class are applied  and used to check if class working
nikitas_bank= BankAccount(1000,"nikita")

nikitas_bank.deposid(500)

nikitas_bank.withdrawing(750)

print("")
print("task 3")
print("")
