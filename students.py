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