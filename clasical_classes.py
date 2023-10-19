
#Task 1: People Class
#Define a class called Person with attributes name and age.
#Then, write a method within the class to introduce the person with their name and age.

#Create a new object using this new class, and call the method you created.

print("")
print("task 1")
print("")

class Person:
 type21="living creature"

 def __init__(self, name, age):
       self.name = name
       self.age = age
 def hello(self):
     print("hello "+ str(self.name), "your age is " +str(self.age))

nikita=Person("Nikita",22)
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
class Animal:
    def __init__(self,speak):
        self.speak=speak

animal=Animal

class Dog(Animal):
    def speak():
        print("bark")

animal=Dog

class Cat(Animal):
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





print("")
print("task 3")
print("")
