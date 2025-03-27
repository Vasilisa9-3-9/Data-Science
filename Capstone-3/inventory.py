#create a list where the items from the text file will be stored
shoes_objects = []


#identify the Shoe class with functions      
class Shoe: 
    def __init__(self, country, code, product, cost, Quantity):
        self.country = country 
        self.code = code 
        self.product = product
        self.cost = cost 
        self.Quantity = Quantity 

    def get_cost(self):
        return float(self.cost) 
    
    def get_quantity(self):
        return float(self.Quantity)
    
    def update_quantity(self, new_quantity):
        self.Quantity = new_quantity
        
    def __str__(self):
        return(f'''\nThe country of the shoe product is {self.country}, the code of the shoe {self.code}, the full name of the product is {self.product},the cost is {self.cost}, and the quantity is {self.Quantity}''')


#create a menu choice function
def menu():
    return("Select an option:\n1-View all the shoe models and their details\n2-Add a shoe model\
           \n3-Check the restock\n4-Search for a specific shoe through a code\
            \n5-Acsess the list of total value calculations for each shoe model\
            \n6-Sale\n7-Exit")
   
#create a function that will while adding shoe objects from the text file will index them via using shoe class parameters 
def read_shoes_data():
    with open("inventory.txt","r") as file:
        try:
            for lines in file.readlines()[1:]:
                temp = lines.strip()
                country = temp.split(",")[0]
                code = temp.split(",")[1]
                product = temp.split(",")[2]
                cost = temp.split(",")[3]
                quality = temp.split(",")[4]
                shoe_object = Shoe(country, code, product, cost, quality)
                shoes_objects.append(shoe_object)

        except FileNotFoundError:
            print("The file that your are trying to open does not exist")

        finally: 
            if file != "inventory.txt":
                file.close()

#create a function that will intake information from the user and add as a shoe object to the list 
def capture_shoe():
    user_intake = input("Please input Country,Code,Product,Cost,Quantity of the Shoe: ")
    country = user_intake.split(",")[0]
    code = user_intake.split(",")[1]
    product = user_intake.split(",")[2]
    cost = user_intake.split(",")[3]
    quality = int(user_intake.split(",")[4])
    shoe_object = Shoe(country, code, product, cost, quality)
    shoes_objects.append(shoe_object)
    with open("inventory.txt", "w") as file:
        for shoes in shoes_objects:
            file.write(f"{shoes.country},{shoes.code},{shoes.product},{shoes.cost},{shoes.Quantity}\n")
    print("Your shoe have been successfully added to the inventory")

#disply all shoe objects from the list
def view_all():
    for shoe in shoes_objects:
        print(shoe)

#display the lowest quantity of a shoe model and ask the user if they'd like to alter the quantity, change the quantity
# number in the list as wel as in the text file  
def re_stock():
    quantity = []
    for shoe in shoes_objects:
        quantity_object = [shoe.Quantity, shoe]
        quantity.append(quantity_object)
    quantities = []

    for i in quantity:
        number = float(i[0])
        quantities.append(number)
    min_value = min(quantities)

    for i in quantity:
        if min_value == float(i[0]):
            object = i[1]
            break
    print(f"The lowest shoe product is {object.product} is with {object.Quantity}")
    user_input = input("Enter the new quantity of this shoe: ")
    object.update_quantity(user_input)
    with open("inventory.txt", "w") as file:
        for shoes in shoes_objects:
            file.write(f"{shoes.country},{shoes.code},{shoes.product},{shoes.cost},{shoes.Quantity}\n")
    print(f"The new quantity for the {object.product} has been updated")

#with user's shoe code input display the correlated shoe product name
def search_shoe():  
    line_indication = input("Please ente the code of the shoe, that you would like to be displayed: ")
    for shoe in shoes_objects:
        if line_indication == shoe.code:
            print(shoe) 
            break

#display the calculated vale per shoe object
def value_per_item():
    for shoe in shoes_objects:
        print(f"The value for {shoe.product} product equals to {shoe.get_cost() * shoe.get_quantity()}")

#show the highest quantity of a shoe object and propose sale as an option to the user 
def highest_qty():
    quantity = []
    for shoe in shoes_objects:
        quantity_object = [shoe.Quantity, shoe]
        quantity.append(quantity_object)
    quantities = []

    for i in quantity:
        number = float(i[0])
        quantities.append(number)
    min_value = max(quantities)

    for i in quantity:
        if min_value == float(i[0]):
            object = i[1]
            break
    print(f"""{object.product} displays the highest quantity in stock equaling to {object.Quantity}, consider for sale""" )
    
#create the menu selecting code               
while True: 
    read_shoes_data()
    print("\n")
    menu_user = menu()
    print(menu_user)
    print("\n")
    menu_choice = input("Please enter your choice: ")
    if menu_choice == ("1"):
        view_all()
    if menu_choice == ("2"):
        capture_shoe()
    if menu_choice == ("3"):
        re_stock()
    if menu_choice == ("4"):
        search_shoe()
    if menu_choice == ("5"):
        value_per_item()
    if menu_choice ==("6"):
        highest_qty()
    if menu_choice == ("7"):
        print("You have successfully exited the program")
        break 
         
#Hi, thank you for looking through this task, 
#Im stuck with the restock() function as i cant seem to make it add the altered product information to the text file
#i have accidentally deleted the text file infomation, due to using "w" for my restock() code
         

            



