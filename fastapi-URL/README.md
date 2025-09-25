# FastAPI URL Shortener

A simple URL shortening service built with FastAPI, SQLAlchemy, and PostgreSQL.  
Generate short links, retrieve original URLs, and track click counts.

## Features
- Shorten any URL
- Retrieve original URL by short code
- Track number of clicks per short URL
- FastAPI auto-generated Swagger UI

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

