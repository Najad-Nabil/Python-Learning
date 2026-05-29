import json

file = open("data.json" , "r")
try:
    students = json.load(file)
except:
    students = []
file.close()

admNumber = 2

def addStudent():
    global admNumber
    name = input(f"Enter the name of the student {admNumber + 1} : ")
    age = int(input("Enter of the student : "))
    mark = int(input("Enter the total marks : "))

    student = {
        "name" : name,
        "age" : age,
        "mark" : mark,
        "id" : admNumber + 1
    }
    admNumber += 1

    students.append(student)
    file = open("data.json" , "w")
    json.dump(students , file)
    file.close()

    print(f"Student created with ID : {student['id']}")
    print(students)

def removeStudent(idOfStudent):
    found = False
    for n in students:
        if n["id"] == idOfStudent:
            students.remove(n)
            found = True
            print(f"Student with ID {idOfStudent} Deleted")

            file = open("data.json" , "w")
            json.dump(students , file)
            file.close()

            break
       
    if found == False:
        print("Student not found")
    print(students)


def searchStudent(idOfStudent):
    found = False

    for i in students:
        if i['id'] == idOfStudent:
            print(i)
            found = True
            break
    if found == False:
        print("Student not found")

def getMarks(idOfStudent):
    found = False

    for i in students:
        if i['id'] == idOfStudent:
            if i['mark'] < 500:
                print(f"Total marks of {i['name']} is {i['mark']} and is not eligible for higher studies")
            else:
                print(f"Total marks of {i['name']} is {i['mark']} and is eligible for higher studies")

            found = True
            break
    if found == False:
        print("Student not found")



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
   