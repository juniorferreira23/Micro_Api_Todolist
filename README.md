# Micro API To-Do List

## 📖 Description
This project was created to be a micro API for a To-Do list.

## 📌 Goal
The objective was to practice with the FastAPI, Pydantic, and Uvicorn libraries, gaining a better understanding of routes and processes.

---

## 💻 Technologies
- **Python**: Version 3.12.3 

## Libraries
- **FastAPI**: Version 0.115.8
- **Pydantic**: Version 2.10.6
- **Uvicorn**: Version 0.34.0

---

## ✨ Features
- Create tasks
- List all tasks
- Search for a specific task by ID
- Update tasks
- Delete tasks

---

## 🛠 Installation

### ✅ Requirements
1. **Python**: Make sure Python is installed on your system. https://www.python.org/downloads/
2. **Git**: Install Git to clone the repository. https://git-scm.com/downloads

### 🔄 Clone the Repository
Open your terminal (Bash, PowerShell, or CMD) and run the following command:
```bash
git clone https://github.com/juniorferreira23/Micro_Api_Todolist.git
```

### 🌐 Creating a Virtual Environment
```bash
python3 -m venv venv
```

### Activate Virtual Environment
Windows
```cmd
.\venv\Scripts\activate.ps1
```

Linux
```bash
source venv/bin/activate
```

### 📦 Installing Dependencies
In the virtual environment, install the required libraries:
```bash
pip install -r requirements.txt
```

### ▶️ Running the Code
To run the program directly, use:
```bash
uvicorn main:app --reload
```

### Swagger Endpoint Documentation
Access the links below to view the API endpoints:
http://localhost:8000/docs