import json

file = open("data.json", "r")
try:
    students = json.load(file)
except:
    students = []
file.close()