# 📝 FastAPI TODO App

> 🧭 This is **Project 2** of my `fastapi-projects` learning series.  
> In this project, I implemented a full **CRUD** TODO app with in-memory storage and unit tests.

Overview: A **FastAPI-based TODO list application** that demonstrates full CRUD functionality, data validation with **Pydantic**, and **unit testing** using FastAPI's built-in TestClient.

---

## 🌟 Features

- ✅ **Create / Read / Update / Delete (CRUD)** operations for TODO items  
- ✅ **Modular project structure** (routes, models, logic separated)  
- ✅ **Data validation** using Pydantic models  
- ✅ **Comprehensive tests** with FastAPI’s `TestClient`  
- ✅ **Lightweight & beginner-friendly** — no database setup required (in-memory list)

---

## ⚙️ Tech Stack

- 🐍 **Python 3.11+**
- ⚡ **FastAPI**
- 📦 **Pydantic**
- 🧪 **Pytest + TestClient**
- 🚀 **Uvicorn**

---

## 🧱 Project Structure
```text
fastapi-todo/
├── app/
│ ├── main.py # Entry point
│ ├── routes.py # API routes (CRUD endpoints)
│ ├── models.py # Pydantic models for data validation
│ └── db.py # Business logic (in-memory data store)
├── tests/
│ └── test_main.py # Unit tests (FastAPI TestClient)
├── requirements.txt # Project dependencies
├── .gitignore
└── README.md
```
---

## ▶️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/y1kng/fastapi-projects.git
cd fastapi-projects/fastapi-todo
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the App
```bash
uvicorn app.main:app --reload
```
Now visit 👉 http://127.0.0.1:8000/docs to access the interactive Swagger UI.

---

## 🧪 How to Test
This project includes unit tests for all CRUD endpoints:
```bash
pytest -v
```
✅ Tests include:

POST /todos → Add a TODO

GET /todos → Retrieve all TODOs

GET /todos/{id} → Retrieve one TODO

PUT /todos/{id} → Update a TODO

DELETE /todos/{id} → Delete a TODO

---

## 💡 Example Endpoints
```text
Method	Endpoint	Description
GET	    /todos	    Get all TODOs
GET	    /todos/{id}	Get a specific TODO
POST	/todos	    Add a new TODO
PUT	    /todos/{id}	Update a TODO
DELETE	/todos/{id}	Delete a TODO
```

---

## 🧠 Notes
This version uses in-memory storage (list) for simplicity.

Future versions can integrate **PostgreSQL** or **SQLite** via **SQLAlchemy** for persistent storage.

---

## License
MIT © 2025 y1kng


