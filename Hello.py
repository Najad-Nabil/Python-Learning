students = []
i = 0

while(i<2):

    name = input("Enter the name : ")
    age = int(input("Enter the age : "))

    student = {
        "name" : name,
        "age" : age
    }
    students.append(student)
    i += 1

print(students[0]["name"])