tasks=[] #empty
print("----Welcome to the to do app----")

total_task=int(input("enter how many tasks yo wanna enter"))
for i in range(1,total_task+1):
       task_name=input(f"enter task {i}")
       tasks.append(task_name)

print(f"today tasks are\n{tasks}")


while True:
    operation=int(input("enter 1 to add\n 2 for update\n3 for delete\n 4 for View \n 5 for Exit"))
    if operation==1:
        add = input("enter you want to add task = ")
        tasks.append(add)
        print(f"Task {add} is added successfully")

    elif operation==2:
         updated=input("which task name you want to update")
         if updated in tasks:
          up=input("enter new task")
          index=tasks.index(updated)
          tasks[index]=up
          print(f"you task has been updated, so updated is {up}")
         else:
          print("no task found enter carefully")

    elif operation==3:
        delete=input("Enter task name you want to delete")
        if delete in tasks:
            tasks.remove(delete)
            print("your task has been successfuly deleted")
            print(f"so, tasks for  the day is {tasks}")
        else:
          print("no task found enter carefully")


    elif operation==4:
        print(f"your final tasks of the day is {tasks}")

    elif operation==5:
        print("closing the program")
        break

    else:
        print("invalid input")
        


