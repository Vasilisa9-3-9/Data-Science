
#create functions, which can be easily accesable for further use in the main body code 

from datetime import date
import datetime

def admin_logg_in_menu():
     print("\nPlease select one of the following options:",
         "\nr - register user",
         "\na - add task",
         "\nva - view all task",
         "\nvm - view my tasks",
         "\ngr - general reports",
         "\nds - display statistics",
         "\ne - exit\n")
   
def non_admin_logg_in_menu():
     print("\nPlease select one of the following options:",
         "\na - add task",
         "\nva - view all tasks",
         "\nvm - view my tasks",
         "\ne - exit\n")
   
def reg_user(user_name, pass_word_confirm):
     file = open("user.txt", "a")
     file.write(f"\n{user_name}, {pass_word_confirm} ")
     file.close()
     print("\nUsername and password has been successfully registered !")

def add_task(task_assigment, task_title, task_description, task_due_date):
     task_complition = ("No")
     current_date = date.today().strftime("%d %b %Y")
     file.write(f"\n{task_assigment}, {task_title}, {task_description}, {current_date}, {task_due_date}, {task_complition}")
     file.close()
     print("\nYour task has been successfully added!")

def view_all():
     with open("tasks.txt", "r") as file:
         for i, lines in enumerate(file):
             temp = lines.strip()
             temp = temp.split(", ")
             print("\n" + str(i+1) + ". " + f"Assigned to : \t{temp[0]}\nThe tital of the task : \t{temp[1]} \
                 \nThe description of the task : \t{temp[2]}\nSet date : \t{temp[3]} \
                 \nDue date : \t{temp[4]}\nTask complete ? \t{temp[5]} ")
     file.close()

def view_mine():
     with open("tasks.txt", "r") as file: 
         for i, lines in enumerate(file):
             temp = lines.strip()
             temp = temp.split(", ")
             if user_name in (temp[0]):
                 print("\n" + str(i+1) + ". " + f"Assigned to:\t{temp[0]}\nThe tital of the task:\t{temp[1]}\
                     \nThe description of the task :\t{temp[2]}\nSet date:\t{temp[3]}\
                     \nDue date:\t{temp[4]}\nTask complete? :\t{temp[5]}")
     file.close()

def user_count():
     with open("user.txt", "r") as file:
         user_count = len(file.readlines())
         file.close()

         return(user_count)
     
def task_count():
     with open("tasks.txt", "r") as file:  
         task_count = len(file.readlines())
         file.close()

         return(task_count)
     
#create list spaces, to identify "usernames" and "passwords" categories, obtained from the "user.txt" file.
usernames = []
passwords = []

#open the "user.txt" as a file, in a reading mode.
with open("user.txt", "r") as file: 
    #using "strip" and "split" functions, to convert the "user.text" information into a suitable list format.
    for lines in file: 
         temp = lines.strip()
         temp = temp.split(", ")
         #sort the "user.txt" obtained items, into the two earlier created list spaces: "usernames" and "passwords".
         usernames.append(temp[0])
         passwords.append(temp[1])
         #close the "user.txt" file.
file.close()

#create a login platform by asking the user to enter a username.
print("\n")
user_name = input("Please enter your username: ")

#create a loop. 
while True: 
     #identify if the user entered a username existent in the "usernames" list.
     if user_name in usernames:
         #grant access to a password entry.
         pass_word = input("Please enter your password: ")
         #terminate the loop if user entered password is with in "passwords" list.
         if pass_word in passwords: 
             break   
         #give an error message, if a password outside the "passwords" list is entered.
         else: 
             print("Incorect password")
     #give an error message, if a username outside the "usernames" list is entered.
     else: 
         print("Try again")
         user_name = input("Please enter your username: ")

#for the main code usage, create a dictionary, that store the information from in a dictionary format with 
#the infromation obtained from the "tasks.txt" file, using "count" idetify each "task-line" with a number
task_dict = {}
count = 1       

with open("tasks.txt", "r+") as f: 
     for line in f: 
         temp = line.strip()
         temp = temp.split(", ")
         task_dict[count] = temp
         count += 1
#create a loop, with a "registration" function(only acsessable to the admin loggin)
while True:  
     if user_name == ("admin"):  
         admin_logg_in_menu()
     elif user_name != ("admin"):  
         non_admin_logg_in_menu()

     menu = input("Enter your choice here: ")
     print("\n")
     if menu == ("r"):
         with open("user.txt", "r") as file: 
             #ask the admin to enter a new username.
             user_name_new = input("Please create a username: ")
             #if the entered username is in "usernames" list, display an "already exists" error, ask for another input.     
             while user_name_new in usernames: 
                 print("This username already exists!")
                 user_name_new = input("Please create a username: ")
             if user_name_new not in usernames:
                 print("Your username has been registered") 
                 pass_word_new = input("Please create a password: ")
                 if pass_word_new in passwords:
                     print("Such password already exists ! ")
                     pass_word_new = input("Please create a password: ")
                 if  pass_word_new not in passwords:
                     #if the entered password is not detected in "passwords" list, ask the admin to confirm the password.
                     pass_word_confirm = input("Please confirm your password : ")
                     #if both passwords match, allow the user and the user's password to be registered 
                     if pass_word_confirm != pass_word_new: 
                         print("The passwords does not match")
                         pass_word_confirm = input("Please confirm your password: ")
                     #if passwords dont match, dispaly a message error and ask for another input 
                     if pass_word_confirm == pass_word_new and user_name_new not in usernames:
                         reg_user(user_name_new, pass_word_confirm)
                         file.close()
     #if user selects "a", through the append function allow the "new task" deatils to be 
     #added to the "tasks.txt" file 
     elif menu == ("a"):
         file = open("tasks.txt", "a")
         #ask the user to enter new task details.
         task_assigment = input("\nPlease enter the user name, to whom the task is assigned to: ")
         task_title = input("\nPlease input the title of the task: ")
         task_description = input("\nPlease write the a description of the task: ")
         task_due_date= input("\nPlease enter the due date of the task: ")
         add_task(task_assigment, task_title, task_description, task_due_date)
         file.close()
     #if the user selects "va" display all the tasks with in the "tasks.txt" file 
     elif menu == ("va"):
         print(view_all())
     #if the user selects "vm", dispaly the tasks that are assigned to the loggin user's username 
     elif menu == ("vm"): 
         view_mine()
         #ask the user to select from the personally assigned dispalyed tasks, which one they'd like to modify 
         task_selection = input("\nSelect a task number for modification? (enter -1 to return to the main menu): ")
         task_selection = int(task_selection)
         #give a return to the main menu option 
         if task_selection == - 1:
             print("\nYou are being returned to the main menu")
             continue 
         else: 
             selected_task = task_dict[task_selection]
             while True:
                    #give a user the options of modification 
                    task_modification = input("""\nWould you like to:\n1 - edit the task\n2 - mark the task as complete
                                            \nEneter your choice: """)
                    if task_modification == ("1"):   
                     #allow further options of modification 
                         task_modification_edit = input("""\nWould you like to:\n1 - edit the username the task is assigned to\n2-edit the due date
                                                     \nEnter your choice: """)
                         if task_modification_edit == ("1"):
                         #provide input to change the "tasks.txt" file info 
                             task_modification_username = input("Enter the username you wish to assign the task to: ")
                             old_name = selected_task[0]
                             selected_task[0] = task_modification_username
                             print(f"\nThe username has been sucsessfuly changed from {old_name} to {task_modification_username}")
                             break
                         elif task_modification_edit == ("2"):
                             task_modification_due_date = input("Please enter a new due date (e.g. 10 Oct 2019): ")
                             selected_task[3] = task_modification_due_date
                             print ("\nThe due date has been sucsesfully modified")
                             break 
                    elif task_modification == ("2"):
                         if selected_task[5] == "No":
                             selected_task[5] == "Yes"
                             print("\nThe task has been marked as complete")
                             break
                         else: 
                             print("The task is already marked as complete.") 
                             break
             with open("tasks.txt", "w") as file:
                for key in task_dict: 
                     task = task_dict[key]
                     task = ", ".join(task)
                     file.write(task + "\n")  
             #create a funtion which will modify the information just edited by the user, within the "tasks.txt" file                     
     elif menu == ("e"):
         print("You have been successfully logged out")
         break 
    #if the user sslects "ds" display the number of users & tasks registered
     elif menu == ("ds"):
         with open("user.txt", "r") as file:
             for lines in file:
                 print(lines)
         print("\n")
         print(f"The total number of users registered:{user_count()}")
         print("\n")
         with open("tasks.txt", "r") as file_tasks:
             for lines in file_tasks:
                 print(lines)
         print("\n")
         print(f"The total number of task: {task_count()}")
     #upon the "gr" selection, diplay in two separate files the statistical information on "tasks.txt" & "users.txt"
     #uses the earlier created dictionary to get the indexes of values that will influece the statistical count 
     elif menu == ("gr"):
         completed_tasks = 0 
         uncompleted_tasks = 0
         overdue_tasks = 0
         uncompleted_overdue_tasks = 0
         percentage = 0
         percantage_overdue = 0
         with open("task_overview.txt", "w+") as file_1:  
             file_1.write(f"The total number of tasks: " + str(task_count())+ "\n")
             for key in task_dict:
                 if task_dict[key][5] == "No":
                     uncompleted_tasks += 1
                     percantage = (((uncompleted_tasks)/task_count()) * 100 ) 
                     if task_dict[key][4] > (datetime.date.today().strftime("%d %b %Y")):
                         uncompleted_overdue_tasks += 1
                 if task_dict[key][5] == "Yes":
                     completed_tasks += 1
                 if task_dict[key][4] > (datetime.date.today().strftime("%d %b %Y")):
                     overdue_tasks += 1 
                     percantage_overdue = (((overdue_tasks)/task_count()) * 100) 
             file_1.write(f"The total number of uncompleted tasks: {uncompleted_tasks} \n")
             file_1.write(f"The percentage of tasks that are incomplete: {percantage} \n")
             file_1.write(f"The total number of tasks that haven't been completed and are overdue: {uncompleted_overdue_tasks}\n")
             file_1.write(f"The total number of complete tasks: {completed_tasks} \n")
             file_1.write(f"The percentage of tasks that are overdue: {percantage_overdue}\n")   
         file_1.close()        
     #for each user, display statistical information only relevant to them
     with open("tasks.txt", "r+") as f: 
         user_completed = 0
         user_dict = {}
         for line in f:
             task = line.split(", ")
             if task[0] not in user_dict:
                 user_dict[task[0]] = 0
             user_dict[task[0]] += 1
         with open("user_overview.txt", "w+") as file_2: 
             file_2.write(f"The total number of users: " + str(user_count()) + "\n")
             file_2.write(f"The total number of task: " + str(task_count())+ "\n")
             for user, num_task in user_dict.items():
                 uncompleted_tasks = 0
                 uncompleted_overdue_tasks = 0
                 user_uncompleted_overdue = 0
                 file_2.write(f"The total number of tasks assigned to that user is: {num_task}\n")
                 user_percentage = (num_task / task_count()) * 100
                 file_2.write(f"The percentage of the total number of tasks that have been asigned to {user}: {user_percentage}\n")
                 for key in task_dict:
                     if user == task_dict[key][0]:
                         if task_dict[key][5] == "No":
                             uncompleted_tasks += 1
                             user_completed = ((num_task - uncompleted_tasks)/ num_task) * 100
                             #file_2.write(f"""The percentage of the tasks that have been asigned to {user} that are complete: {user_completed}\n""")
                             user_uncompleted =(uncompleted_tasks/ num_task) * 100
                             #file_2.write(f"""The percentage of the tasks that have been asigned to {user} that must still be completed: {user_uncompleted}\n""")
                             if task_dict[key][4] > (datetime.date.today().strftime("%d %b %Y")):
                                 uncompleted_overdue_tasks += 1 
                                 user_uncompleted_overdue = (uncompleted_overdue_tasks / num_task) * 100
                 file_2.write(f"""The percentage of the tasks assigned to {user} that have not yet been completed and are overdue:{user_uncompleted_overdue}\n""")
                 file_2.write(f"""The percentage of the tasks that have been asigned to {user} that are complete: {user_completed}\n""")
                 file_2.write(f"""The percentage of the tasks that have been asigned to {user} that are uncomplete: {user_uncompleted}\n""")
     f.close()









             