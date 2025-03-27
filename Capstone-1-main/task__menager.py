
#create list spaces, to identify "usernames" and "passwords" categories from the text file.

usernames = []

passwords = []

#open the "user.txt" as a file, in a reading mode.

with open("user.txt", "r") as file: 

#using "strip" and "split" functions, convert the "user.text" information into a suitable list format.

    for lines in file: 

        temp = lines.strip()

        temp = temp.split(", ")
    
#sort the "user.txt" obtained items, into the two earlier created list spaces: "usernames" and "passwords".

        usernames.append(temp[0])
        
        passwords.append(temp[1])

#close the "user.txt" file.

file.close()

print("\n")

#create a login platform by asking the user to enter a username.

user_name = input("Please enter your username : ")

#create a loop. 

while True: 
    
#identify if the user entered a username existent in the "usernames" list.

    if user_name in usernames:

#grant access to a password entry.

        pass_word = input("Please enter your password : ")

#terminate the loop if user entered password is with in "passwords" list.

        if pass_word in passwords: 

            break 

#give an error message, if a password outside the "passwords" list is entered.

        else: 

            print("Incorect password")

#give an error message, if a username outside the "usernames" list is entered.

    else: 

        print("Try again")

        user_name = input("Please enter your username : ")

print("\n")

#upon login, print the function menu options.

print("Please select one of the following options:")

#ask the user to input their "menu function" choice.

#give an admin login only option of "statistics" display.

while True: 

    with open("user.txt", "r") as file: 

      for lines in file:

        temp = lines.strip()

        temp = temp.split(", ")

        if user_name in (temp[0]):

            print("\n")

            print("st - display of statistics")

      file.close()

    menu = input("\nr - register user\na - add task\nva - view all tasks\nvm - view my tasks\ne - exit\nyour choice: ")

    print("\n")
    
#make the selection of "r" only possible to manipulate via an admin login.

    if menu == ("r"):

      with open("user.txt", "r") as file: 

         for lines in file:

             temp = lines.strip()

             temp = temp.split(", ")

             if user_name in (temp[0]):

#ask the admin to enter a new username.

                 user_name = input("Please create a username : ")

#if the entered username is in "usernames" list, display an "already exists" error, ask for another input.     

                 if user_name in usernames:

                      print("This username already exists!")

                      user_name = input("Please create a username : ")

                 if user_name not in usernames:

#if the entered username is not detected in "usernames" list, add the username to the "user.txt" file.
 
                       file = open("user.txt", "a")

                       file.write(f"\n{user_name}, ")

                       file.close()

#ask the user to input a new password 

                       pass_word = input("Please create a password : ")

#if the entered password is in "passwords" list, display an "already exists" error, ask for another input.

                       if pass_word in passwords:

                         print("Such password already exists ! ")

                         pass_word = input("Please create a password : ")

                       if  pass_word not in passwords:

#if the entered password is not detected in "passwords" list, ask the admin to confirm the password.
 
                         pass_word_confirm = input("Please confirm your password : ")

#if both passwords match, add the password to the "user.txt" file. 

                         if pass_word_confirm == pass_word:

                             file = open("user.txt", "a")

                             file.write(f"{pass_word}")

                             file.close()

                             print("\n")

                             print("Username and password has been successfully registered ! ")

                             break 

      file.close()

#upon "a" selection, open the "tasks.txt" file in an append mode, to add the new entered task.

    elif menu == ("a") :

      file = open("tasks.txt", "a")

#ask the user to enter new task details.

      task_assigment = input("Please enter the user name, to whom the task is assigned to : ")

      print("\n")

      task_title = input("Please input the title of the task : ")

      print("\n")

      task_description = input("Please write the a description of the task : ")

      print("\n")

      task_due_date= input("Please enter the due date of the task : ")

      task_complition = ("No")

#use the datetime import mode, to make the "set date" of the task, as a current date.

      from datetime import date

      current_date = date.today()

#through the "write" function, add the user's inputs in the wanted order to the "tasks.txt" file. 
    
      file.write(f"\n{task_assigment}, {task_title}, {task_description}, {current_date}, {task_due_date}, {task_complition}")
    
#close the file.

      file.close()

      print("\n")

      print("Your task has been successfully added! ")

      print("\n")

#upon "va" selection, open the "tasks.txt" in a reading mode

    elif menu == ("va") :

#display all of the "task" items, in a easily readable format. 

     with open("tasks.txt", "r") as file:

         for lines in file:

             temp = lines.strip()

             temp = temp.split(", ")

             print(f"\nAssigned to : \t{temp[0]}\nThe tital of the task : \t{temp[1]} \
                  \nThe description of the task : \t{temp[2]}\nSet date : \t{temp[3]} \
                  \nDue date : \t{temp[4]}\nTask complete ? \t{temp[5]} ")
            
#close the file 
 
         file.close()

#upon "vm" selection, open "tasks.txt" in a reading mode. 

    elif menu == ("vm"): 
    
        with open("tasks.txt", "r") as file: 

#make the tasks, that only contain the user's "username" displayed, in an easily readable format. 

         for lines in file:

             temp = lines.strip()

             temp = temp.split(", ")

             if user_name in (temp[0]):

                 print(f"\nAssigned to : \t{temp[0]}\nThe tital of the task : \t{temp[1]} \
                 \nThe description of the task : \t{temp[2]}\nSet date : \t{temp[3]} \
                 \nDue date : \t{temp[4]}\nTask complete ? \t{temp[5]}")

#close the file.

         file.close()

#upon "st" selection, only accessible for an admin login use, open the "user.txt" in a reading mode.

    elif menu == ("st"):

         with open("user.txt", "r") as file:

            for lines in file:

             temp = lines.strip()

             temp = temp.split(", ")

             if user_name in (temp[0]):

#through the "readlines" and "len" functions, display the total number of "usernames".

                 user_count = len(file.readlines())

                 print (f"Total number of users : {user_count}")

#open the "tasks.txt" in a reading mode. 

                 with open("tasks.txt", "r") as file:
        
#through the "readlines" and "len" functions, display the total number of "tasks".

                     task_count = len(file.readlines())

                     print("\n")

                     print (f"Total number of tasks : {task_count}")

#close both files.

                     file.close()

         file.close()

#if the user enters "e", dispaly the logout message 

    else:

     print("You have successfully logged out !")

     break 




    









    
    


