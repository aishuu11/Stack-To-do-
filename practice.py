

import datetime as dt

menu_list = ["Options", "1. Add task", "2. Complete task", "3. Delete task", "4. View tasks","5. Clear All", "6. Exit"]
task_dict = {"1": "study"}


def menu():
     
    print("MY STACK TO-DO LIST\n")
    print(f" Today : {dt.datetime.today()}")

    for option in menu_list: 
          print(option)

    try:
        option_num = int(input("Choose an option num : "))

    except ValueError:
        print("Please enter a number from 1 to 5.")
        return None

    if option_num not in [1,2,3,4,5,6]:
        print("Invalid option number") 

    return option_num
     
def display_task():
    print("Tasks : ")
    for key, value in task_dict.items() :
        print(f"{key} : {value}")
    


def adding_task():
    task_num = max((int(key) for key in task_dict), default=0) + 1
    task = input("What is your task? ")

    while task == "": 
        task = input("What is your task? ")

    task_dict[str(task_num)] = task

    display_task()



def delete_task():
    delete_num = input("Which task number do you want to delete? ")

    if delete_num in task_dict:
        del task_dict[delete_num]
        print("Deleted")
        display_task()
    else:
        print("Invalid task number")


def complete_task():
    complete_num = input("Which task number did u complete? ")

    if complete_num in task_dict: 
        task_dict[complete_num] = task_dict[complete_num] + " " + "(COMPLETED)"
        display_task()

    else:
        print("Invalid task number")


def clearAll(): 
    task_dict.clear()
    print("cleared all")




if __name__ == "__main__":


    while True: 
        num = menu()
        if num == None:
            continue

        if num == 1:
            adding_task()

        elif num == 2: 
            complete_task()

        elif num == 3 :
            delete_task()

        elif num == 4:
            display_task()

        elif num == 5: 
            clearAll()

        elif num == 6:
            print("Bye")
            break

        




