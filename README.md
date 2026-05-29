# 📘 Student Management System (Python CLI)

A simple **Student Management System** built using Python.  
It uses a JSON file for storage and provides basic CRUD operations through a command-line interface.

---

## 🚀 Features

- Add new student records  
- Remove student by ID  
- Search student by ID  
- View marks and eligibility  
- Persistent storage using `data.json`  
- Menu-driven CLI system  

---

## 🛠️ Technologies Used

- Python 3  
- JSON file handling  
- Command Line Interface (CLI)  

---

## 📂 Project Structure


Python-Learning/
├── Hello.py
├── data.json
└── README.md


---

## ▶️ How to Run

### 1. Clone the repository

git clone https://github.com/your-username/Python-Learning.git


### 2. Enter the folder

cd Python-Learning


### 3. Run the program

python Hello.py


---

## 📌 Functionalities

### ➕ Add Student
- Enter student name, age, and marks  
- Automatically generates a unique ID  
- Saves data into `data.json`  

### ❌ Remove Student
- Deletes student using ID  
- Updates JSON file  

### 🔍 Search Student
- Finds student details by ID  

### 📊 View Marks
- Displays total marks  
- Eligibility:
  - ≥ 500 → Eligible for higher studies  
  - < 500 → Not eligible  

---

## 💾 Data Storage

Example `data.json`:


[
{
"name": "John",
"age": 18,
"mark": 520,
"id": 1
}
]


---

## 📚 What I Learned

- File handling in Python  
- JSON read/write operations  
- Functions and loops  
- CLI application structure  

---

## 🔮 Future Improvements

- Add update student feature  
- Input validation  
- Use SQLite database instead of JSON  
- GUI version using Tkinter or web app  

---

## 👨‍💻 Author

Made by a student learning Python 🚀
