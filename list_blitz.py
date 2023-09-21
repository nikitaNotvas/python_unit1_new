
#Task 1: Create a list
#Create a list with 4 elements and print it.
""
lists=[1,2,3,5]#here i created list
print(lists)#here list will be printed
""
#Task 2: Add Element to a List
#Add an element to the end of the list. Print the updated 
#list.
""
lists.append(7)#this part adds item to list
print(lists)
""
#Task 3: Remove Element from a List
#Remove a specific element from the list.
#  Print the updated list.
""
lists.remove(3)#this part will remove item from list
print(lists)
""
#Task 4: Modify Element in a List
#Modify an element at a specific index with a new value. 
#Print the updated list.
""
lists[1]="hello"#this part is modifing list by changing value of 2 to hello
print(lists)
""
#Task 5: Append Multiple Elements to a List
#Append multiple elements to the end of the list. Print 
#the updated list.
""
lists.append("hello")#here i used multiple appendes to add multiple items in list
lists.append("fish")
print(lists)
""
#Task 6: Delete Element at a Specific Index
#Delete an element at a specific index. Print the updated 
#list.
""
del lists[1] #this part delits speccifec item by index
print(lists)
""
#Task 7: Subsetting lists
#Create a new variable equal to the first 2 items of your list
#Then print out the new variable
""
zz=[lists[0:2]]#this part is looking for first 2 items on list using index and storing them in list called zz
print(zz)
""
#Task 8: Extend a List
#Extend the list with the elements of another list. Print 
#the updated list.
""
combined_list=(zz+lists)#in this line i combined lists and zz in one list called combined_list
print(combined_list)
""