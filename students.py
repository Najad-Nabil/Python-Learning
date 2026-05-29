import json

file = open("data.json", "r")
try:
    students = json.load(file)
except:
    students = []
file.close()

admNumber = 2

def addStudent():
    global admNumber
    name = input("Enter the name of the student : ")
    age = int(input("Enter age of the student : "))
    mark = int(input("Enter the total marks : "))

    student = {
        "name": name,
        "age": age,
        "mark": mark,
        "id": admNumber + 1
    }

    admNumber += 1
    students.append(student)

    file = open("data.json", "w")
    json.dump(students, file)
    file.close()

def removeStudent(idOfStudent):
    found = False

    for n in students:
        if n["id"] == idOfStudent:
            students.remove(n)
            found = True
            print("Student deleted")

            file = open("data.json", "w")
            json.dump(students, file)
            file.close()
            break

    if not found:
        print("Student not found")


def searchStudent(idOfStudent):
    found = False

    for i in students:
        if i["id"] == idOfStudent:
            print(i)
            found = True
            break

    if not found:
        print("Student not found")


def getMarks(idOfStudent):
    found = False

    for i in students:
        if i["id"] == idOfStudent:
            if i["mark"] < 500:
                print("Not eligible for higher studies")
            else:
                print("Eligible for higher studies")

            found = True
            break

    if not found:
        print("Student not found")

while(1):
    print("1.Add Student\n2.Remove Student\n3.Search Student\n4.View Marks\n5.Exit")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        addStudent()
    elif choice == 2:
        idOfStudent = int(input("Enter id to remove : "))
        removeStudent(idOfStudent)
    elif choice == 3:
        idOfStudent = int(input("Enter id to search : "))
        searchStudent(idOfStudent)
    elif choice == 4:
        idOfStudent = int(input("Enter id to view marks : "))
        getMarks(idOfStudent)
    elif choice == 5:
        break
    else:
        print("Invalid choice")