
import sqlite3
import xml.etree.ElementTree as ET
import json 

try:
    db = sqlite3.connect("HyperionDev.db")
except sqlite3.Error:
    print("Please store your database as HyperionDev.db")
    quit()

cur = db.cursor()

def usage_is_incorrect(input, num_args):
    if len(input) != num_args + 1:
        print(f"The {input[0]} command requires {num_args} arguments.")
        return True
    return False

def store_data_as_json(data, filename):
    data_list = []

    with open(filename, "r+") as outfile:
        json_file = json.load(outfile)
        for key, value in data.items():
            data_list.append([key, value])
        data_dict = {}
        for key, value in data.items():
            if key == data_list[0][0]:
                main_key = value
            else:
                data_dict[main_key][key] = value 
        json_file.update(data_dict)

        with open(filename, "w") as outfile:
            json.dump(data_dict, outfile)

def store_data_as_xml(data, filename):
    data_list = []

    tree = ET.parse(filename)
    root = tree.getroot()
    for key, value in data.items():
        data_list.append([key, value])
    element = ET.SubElement(root, data_list[0][0])
    element.set("key", data_list[0][1])
    for i in range(1, len(data_list)):
        sub_element = ET.SubElement(element, data_list[i])
        sub_element.text = str(data_list[i][1])
    tree = ET.ElementTree(root)
    tree.write(filename, xml_declaration = True, encoding = "utf-8")

def offer_to_store(data):
    while True:
        print("Would you like to store this result?")
        choice = input("Y/[N]? : ").strip().lower()
        if choice == "y":
            filename = input("Specify filename. Must end in .xml or .json: ")
            ext = filename.split(".")[-1]
            if ext == 'xml':
                store_data_as_xml(data, filename)
            elif ext == 'json':
                store_data_as_json(data, filename)
            else:
                print("Invalid file extension. Please use .xml or .json")
        elif choice == 'n':
            break
        else:
            print("Invalid choice")

usage = '''
What would you like to do?

d - demo
vs <student_id>            - view subjects taken by a student
la <firstname> <surname>   - lookup address for a given firstname and surname
lr <student_id>            - list reviews for a given student_id
lc <teacher_id>            - list all courses taken by teacher_id
lnc                        - list all students who haven't completed their course
lf                         - list all students who have completed their course and achieved 30 or below
e                          - exit this program

Type your option here: '''

print("Welcome to the data querying app!")

while True:
    print()
    # Get input from user
    user_input = input(usage).split(" ")
    print()
    # Parse user input into command and args
    command = user_input[0]
    if len(user_input) > 1:
        args = user_input[1:]

    if command == 'd': # demo - a nice bit of code from me to you - this prints all student names and surnames :)
        cur.execute("SELECT * FROM Student")
        for _, firstname, surname, _, _ in cur:
            print(f"{firstname} {surname}")
        
    elif command == 'vs': # view subjects by student_id
        data = {}
        subjects = []
        if usage_is_incorrect(user_input, 1):
            student_id = args[0]
            cur.execute(f"""SELECT Course.course_name FROM Course
                               INNER JOIN StudentCourse ON StudentCourse.course_code = Course.course_code
                               WHERE StudentCourse.student_id = {student_id};""")
            for row in cur:
                print(row[0])
                subjects.append(row[0])
            data["student_id"] = student_id
            data["subjects"] = subjects
        offer_to_store(data)

    elif command == 'la':# list address by name and surname
        if usage_is_incorrect(user_input, 2):
            firstname, surname = args[0], args[1]
            data = {}
            subjects = []
            cur.execute(f"""SELECT Address.adress_id, Address.street, Address.city, Address.province,
                               Address.postal_code, Address.country FROM Address INNER JOIN Student 
                               ON Student.address_id = Address.address_id
                               WHERE Student.first_name, Student.last_name= {firstname, surname};""")
            for row in cur: 
                print(row[0])
                subjects.append(row[0])
            data["firstname, surname"] = firstname, surname 
            data["subjects"] = subjects
        offer_to_store(data)

    elif command == 'lr':# list reviews by student_id
        if usage_is_incorrect(user_input, 1):
            student_id = args[0]
            data = {}
            subjects = []
            cur.execute(f"""SELECT Review.review_text FROM Review INNER JOIN StudentCourse
                               ON StudentCourse.course_code = Review.course_code
                               WHERE StudentCourse.student_id = {student_id};""")   
            for row in cur:
                print(row[0])
                subjects.append(row[0])
            data["student_id"] = student_id
            data["subjects"] = subjects
        offer_to_store(data)

    elif command == 'lc': #list all courses taken by a given teacher_id
        if usage_is_incorrect(user_input, 1):
            teacher_id = args[0]
            data = {}
            subjects = []
            cur.execute(f"""SELECT Course.course_name FROM Course INNER JOIN Teacher 
                               ON Course.teacher_id = Teacher.teacher_id
                               WHERE Teacher.teacher_id = {teacher_id};""") 
            for row in cur: 
                print(row[0])
                subjects.append(row[0])
            data["student_id"] = teacher_id
            data["subjects"] = subjects
        offer_to_store(data)
    
    elif command == 'lnc':# list all students who haven't completed their course
        data = {}
        subjects = []
        cur.execute("""SELECT * FROM Student INNER JOIN StudentCourse 
                               ON Student.student_id = StudentCourse.student_id
                               WHERE StudentCourse.is_complete = False;""")  
        for row in cur: 
            print(row[0])
            subjects.append(row[0])
        data["subjects"] = subjects
        offer_to_store(data)
    
    elif command == 'lf':# list all students who have completed their course and got a mark <= 30
        data = {}
        subjects = []
        cur.execute("""SELECT * FROM Student INNER JOIN StudentCourse 
                               ON Student.student_id = StudentCourse.student_id
                               WHERE StudentCourse.is_complete = True AND 
                               StudentCourse.mark <= 30;""")  
        for row in cur: 
            print(row[0])
            subjects.append(row[0])
        data["subjects"] = subjects
        offer_to_store(data)
     
    elif command == 'e':# list address by name and surname
        print("Programme exited successfully!")
        break
    
    else:
        print(f"Incorrect command: '{command}'")
    
#Hi, thank you for looking at my task! My main issues with this task is in the "offer_to_store()" function, both the
#xml and json formation codes seem to be causing trouble, so I was wondering if you could please give me a little guidance 
#on how to modify it so that the function runs smoothly. 
#Thank you in advance! 

    
