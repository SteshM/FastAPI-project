# Student Management System

This is a FastAPI project for managing student records in an educational institution. 
It provides RESTful APIs to handle common operations such as:

- Creating, updating, and deleting student records
- Retrieving student details individually or in bulk
- Filtering and searching students by attributes (e.g., name, class, age)
- Pagination for efficient data retrieval

The project uses Pydantic models for data validation and response serialization. 
It is designed to be lightweight, fast, and easy to extend with additional features such as authentication, reporting, or integration with databases like PostgreSQL or SQLite.

## Tech Stack
- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn (ASGI server)
- Optional: SQLAlchemy / PostgreSQL for database support

## Getting Started
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the server: `uvicorn app.main:app --reload`

## Features
- RESTful API endpoints for CRUD operations
- Input validation with Pydantic models
- Paginated responses for large datasets
- Modular and scalable architecture for adding new features
