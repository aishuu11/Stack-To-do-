print("Stack To - Do List")


task_list = ["learn python", "practice leetcode",]

def display_task():
    for num,task in enumerate(task_list):
        print(f"{num+1} : {task}")

def adding_task():
        task = input('what is your task? ')
        task_list.append(task)


display_task()


add = input("Do you want to add a task? ")

while add.strip().lower() == "yes": 
    adding_task()
    print("Added")
    add = input("Do you want to add a task? ")

    

display_task()


