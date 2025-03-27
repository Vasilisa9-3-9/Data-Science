
#define a function which contains the information on the menu display
def menu():
    print("""Please select from:
          1.Compute a calculation
          2.Read from a text file
          3.Exit the program\n""")
#create a function which will take in numbers and create a text file storing those numbers and the calculation 
#that the user wants done to those numbers, incude the error handeling method 
def intake():
    while True:
        try: 
             filename = input("Please create a name for the text file where your numbers will be stored: ")
             number_1 = int(input("Please enter a number: "))
             number_2 = int(input("Please enter another number: "))
             operation = input("Please select an operation you'd like to perform to the numbers(e.g. +, -, *, /): ")
             with open( filename + ".txt","a+") as f: 
                 if operation == ("+"):
                     outcome = number_1 + number_2
                     print("\n")
                     print(f"{number_1} + {number_2} = {outcome}\n")
                     f.write(f"{number_1} + {number_2} = {outcome}\n")
                 elif operation == ("-"):
                     if number_1 > number_2: 
                         outcome = number_1 - number_2
                         print("\n")
                         print(f"{number_1} - {number_2} = {outcome}\n")
                         f.write(f"{number_1} - {number_2} = {outcome}\n")
                     else: 
                         outcome = number_2 - number_1
                         print("\n")
                         print(f"{number_2} - {number_1} = {outcome}\n")
                         f.write(f"{number_2} - {number_1} = {outcome}\n")
                 elif operation == ("*"):
                     outcome = number_1 * number_2
                     print("\n")
                     print(f"{number_1} * {number_2} = {outcome}\n")
                     f.write(f"{number_1} * {number_2} = {outcome}\n")
                 elif operation == ("/"):
                     if number_1 > number_2:
                         outcome = number_1 / number_2
                         print("\n")
                         print(f"{number_1} / {number_2} = {outcome}\n")
                         f.write(f"{number_1} / {number_2} = {outcome}\n")
                     else: 
                         outcome = number_2 / number_1
                         print("\n")
                         print(f"{number_2} / {number_1} = {outcome}\n")
                         f.write(f"{number_2} / {number_1} = {outcome}\n")
                 f.close()
                 break     
        except Exception:
             print("That's not a valid number. Try again... ")
#create a loop which will uopn displaying the menu(coded by a function), take in the user's inputs and perform the choice 
#connected algorithms
while True:
     menu()
     intake_user = input("Enter your choice:")
     print("\n")
     if intake_user == ("1"):
         intake()
     elif intake_user == ("2"):
         try:
             filename = input("Please enter the name for the text file you would like to read from: ")
             print("\n")
             with open(filename  + ".txt","r") as file:
                 for line in file:
                     print(line)
         except FileNotFoundError as error: 
             print("The file that you are trying to open does not exist: ")
             print(error)
     else: 
         print("You have sucessfuly exitied the program")
         break
         


 