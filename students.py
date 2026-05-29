import json

def load_data():
    try:
        file = open("data.json" , "r")
        data = json.load(file)
        file.close()
    except:
        data = {
            "admNumber" : 0,
            "students" : []
        }
    return data


def save_data(data):
    file = open("data.json" , "w")
    json.dump(data , file)
    file.close()


def addStudent():
    name = input(f"Enter the name of the student {data['admNumber'] + 1} : ")
    age = int(input("Enter of the student : "))
    mark = int(input("Enter the total marks : "))

    newID = data['admNumber'] + 1

    student = {
        "name" : name,
        "age" : age,
        "mark" : mark,
        "id" : newID
    }
    data['admNumber'] += 1

    data['students'].append(student)
    save_data(data)

    print(f"Student created with ID : {student['id']}")
    print(data['students'])

def removeStudent(idOfStudent):
    found = False
    for n in data['students']:
        if n["id"] == idOfStudent:
            data['students'].remove(n)
            found = True
            print(f"Student with ID {idOfStudent} Deleted")
            break
       
    if found == False:
        print("Student not found")
    else:
        save_data(data)
    print(data['students'])


def searchStudent(idOfStudent):
    found = False

    for i in data['students']:
        if i['id'] == idOfStudent:
            print(i)
            found = True
            break
    if found == False:
        print("Student not found")

def getMarks(idOfStudent):
    found = False

    for i in data['students']:
        if i['id'] == idOfStudent:
            if i['mark'] < 500:
                print(f"Total marks of {i['name']} is {i['mark']} and is not eligible for higher studies")
            else:
                print(f"Total marks of {i['name']} is {i['mark']} and is eligible for higher studies")

            found = True
            break
    if found == False:
        print("Student not found")



data = load_data()

while(1):
    print("1.Add Student\n2.Remove Student\n3.Search Student\n4.View Marks\n5.Exit")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        addStudent()
    elif choice == 2:
        idOfStudent = int(input("Enter the id of student to be removed : "))
        removeStudent(idOfStudent)
    elif choice == 3:
        idOfStudent = int(input("Enter the id of the student to be searched : "))
        searchStudent(idOfStudent)
    elif choice == 4:
        idOfStudent = int(input("Enter the id of the student to get marks : "))
        getMarks(idOfStudent)
    elif choice == 5:
        break
    else:
        print("Invalid choice")
   