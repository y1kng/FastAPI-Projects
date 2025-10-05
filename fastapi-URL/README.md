# 📝 FastAPI URL Shortener

> 🧭 This is **Project 3** of my `fastapi-projects` learning series.  
> Each project builds upon the previous one, gradually adding new features and complexity.  
> In this project, I implemented a **URL shortening service** with FastAPI, PostgreSQL, and SQLAlchemy,  
> including short link generation, original URL retrieval, click tracking, and unit tests.

Overview: A simple URL shortening service built with FastAPI, SQLAlchemy and PostgreSQL.
Generate short links, retrieve original URLs, and track click counts.

---

## 🌟 Features
- ✅ Shorten any URL
- ✅ Retrieve original URL by short code
- ✅ Track number of clicks per short URL
- ✅ FastAPI auto-generated **Swagger UI**

---

## ⚙️ Tech Stack

- 🐍 **Python 3.11+**
- ⚡ **FastAPI**
- 🐘 **PostgreSQL**
- 🐍 **SQLAlchemy**
- 📦 **Pydantic**
- 🐳 **Docker & Docker Compose**
- 🧪 **Pytest + TestClient**
- 🚀 **Uvicorn**

---

## 🧱 Project Structure
```text
fastapi-URL/
├── app/
│   ├── main.py        # Entry point
│   ├── models.py      # Database models
│   ├── crud.py        # Business logic
│   ├── database.py    # Connect to production database and get session instance
│   ├── utils.py       # Helper functions (short code generator)
│   ├── schemas.py     # Pydantic data validation
│   ├── setup_db.py    # Map ShortUrl class into the database; only needs to run once per database
│   └── routes/
│       └── endpoints.py  # API endpoints
├── tests/
│   ├── test_main.py   # API test cases
│   └── conftest.py    # Test fixtures & dependencies
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```
---

## ▶️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/y1kng/fastapi-projects.git
cd fastapi-projects/fastapi-URL
```

### 2. Setup environment
```bash
cp .env.example .env # Fill in your own PostgreSQL database credentials
```

### 3. Build & start with Docker
```bash
docker compose up --build
```

### 4. Access API
Open http://localhost:8000/docs to try the endpoints

---

## 🧪 How to Test
```bash
pytest -v
```
✅ Includes tests for:
- URL shortening
- URL retrieval
- Click count tracking
- List all short URLs

Make sure your test database exists (as configured in DATABASE_URL_TEST) before running tests.

---

## 🧠 Notes
- This project uses **PostgreSQL**; ensure Docker is running.
- Short codes are generated randomly using **utils.py**.
- Future improvements could include user authentication and custom short codes.

---

## 📜 License
MIT © 2025 y1kng















## Setup & Run

1. Copy `.env.example` to `.env` and fill in your database info.
2. Build and start with Docker:

```bash
docker compose up --build

Open Swagger UI at http://localhost:8000/docs to test endpoints.

Project Structure
fastapi-URL/
│── app/
│ ├── main.py # Entry point
│ ├── models.py # Database models
│ ├── crud.py # Business logic
│ ├── utils.py # Helper functions (random short code generator)
│ ├── schemas.py # Pydantic data validation
│ └── routes/
│ └── endpoints.py # API endpoints
│── tests/
│ ├── test_main.py # API test cases
│ └── conftest.py # Test fixtures & dependencies
│── Dockerfile
│── docker-compose.yml
│── .env.example
│── README.md

Environment Variables
Create a .env based on .env.example. Minimal example:
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=fastapi_url
POSTGRES_TEST_DB=fastapi_url_test
POSTGRES_HOST=db
POSTGRES_PORT=5432
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000

