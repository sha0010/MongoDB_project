import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["project"]

while True:
    print("""    1. Create Account
    2. Login
    """)
    choice = input("Please Select an Option: ")

    if(choice == '1'): # CREATE ACCOUNT
        collection = db["students"]
        name = input("ENTER NAME: ")
        age = int(input("ENTER AGE: "))
        username = input("ENTER USERNAME: ")
        password = input("ENTER PASSWORD: ")
        collection.insert_one({
            "name": name,
            "age": age,
            "username": username,
            "password": password
        })
        break

    if(choice == '2'): # LOGIN
        collection = db["students"]
        User = input("\nENTER USERNAME: ")
        Pass = input("ENTER PASSWORD: ")
        results = collection.find( {"username": User}, {"_id": 0, "password": 1})
        num_records = 0
        for result in results:
            num_records += 1
            test = result["password"]
            if(Pass == test):
                print("\nlogin confirmed.")
            else:
                print("\nWrong password.")
                exit()
        if(num_records == 0):
            print("\nUsername Not Found.")
            exit()
        # logged into account
        
        print("\n1. Join a Course")
        print("2. Show Grades")
        choice1 = input("\nSelect an Option: ")
        if(choice1 == '1'): # Join a Course
            collection = db["Courses"]
            results = collection.find()
            print("\nHere's the Name of Courses. Choose One.\n")
            line_num = 1
            for result in results: # Print Avalable Courses
                print(f"{line_num}. {result["course_name"]}")
                line_num += 1

            # Select a Course
            course_chosen = input("\nSelect a Course to Join: ")

            collection = db["student_course"]
            if(course_chosen == '1'): # Python Programming
                print("\n1. python basic")
                print("2. python advanced")
                subset_chosen = input("\nNow Choose a Subset: ") # Select a Course Subet
                if(subset_chosen == '1'):
                    x = collection.find( {"username": User, "title": "python basic"})
                    num = 0
                    for i in x:
                        num += 1
                    if(num != 0):
                        print("\nYour Name is Already Here.")
                        exit()
                    collection.insert_one({
                    "username": User,
                    "title": "python basic",
                    "grade": 0
                })
                    print("\nRegistration Done")
                if(subset_chosen == '2'):
                    x = collection.find( {"username": User, "title": "python advanced"})
                    num = 0
                    for i in x:
                        num += 1
                    if(num != 0):
                        print("\nYour Name is Already Here.")
                        exit()
                    collection.insert_one({
                    "username": User,
                    "title": "python advanced",
                    "grade": 0
                })
                    print("\nRegistration Done")
            
            if(course_chosen == '2'): # Math Course
                print("\n1. differential equations")
                print("2. signal and systems")
                subset_chosen = input("\nNow Choose a Subset: ") # Select a Course Subet
                if(subset_chosen == '1'):
                    x = collection.find( {"username": User, "title": "differential equations"})
                    num = 0
                    for i in x:
                        num += 1
                    if(num != 0):
                        print("\nYour Name is Already Here.")
                        exit()
                    collection.insert_one({
                    "username": User,
                    "title": "differential equations",
                    "grade": 0
                })
                    print("\nRegistration Done")
                if(subset_chosen == '2'):
                    x = collection.find( {"username": User, "title": "signal and systems"})
                    num = 0
                    for i in x:
                        num += 1
                    if(num != 0):
                        print("\nYour Name is Already Here.")
                        exit()
                    collection.insert_one({
                    "username": User,
                    "title": "signal and systems",
                    "grade": 0
                })
                    print("\nRegistration Done")
        if(choice1 == '2'): # Show Grades
            collection = db["student_course"]
            results = collection.find( {"username": User}, {"_id": 0, "username": 0})
            for result in results:
                print(result)
    break