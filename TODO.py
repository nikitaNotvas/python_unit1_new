todos=[]
todos.append(input("Enter your first todo: "))#this part of code is asking user to input first todo
while 1:

    print("-----------------------------------------------------")
    print(todos)
    print("-----------------------------------------------------")
    q=input("do you want to add one more todo to your todos? Y/N ")#this part of code allows user to choose action which they will do 
    if q=="Y"or q=="y":
        todos.append(input("Add you new todo: "))#this part of code adds 1 todo to list
    elif q=="N" or q=="n":
        z=input("do you want to delete one todo from your todos? Y/N ")#this part of code allows user to choose action which they will do 
        if z== "y" or z=="Y":
            todos.remove(input("Enter you todo which you would like to remove: "))#this part of code removes 1 todo to list
        else:
            continue#if user didn't choose any thing it will just continue on 