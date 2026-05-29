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