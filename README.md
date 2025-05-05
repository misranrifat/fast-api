# FastAPI CRUD Demo

A demonstration of CRUD operations using FastAPI, SQLAlchemy, and Pydantic.

## Project Structure

```
fast-api/
│
├── app/                        # Application package
│   ├── api/                    # API endpoints
│   │   ├── endpoints/          # API endpoint modules
│   │   │   └── items.py        # Item endpoints
│   │   ├── api.py              # API router
│   │   └── __init__.py
│   │
│   ├── core/                   # Core modules
│   │   └── config.py           # Configuration settings
│   │
│   ├── crud/                   # CRUD operations
│   │   ├── base.py             # Base CRUD class
│   │   ├── item.py             # Item CRUD operations
│   │   └── __init__.py
│   │
│   ├── db/                     # Database modules
│   │   ├── deps.py             # Dependencies (DB session)
│   │   └── session.py          # DB session configuration
│   │
│   ├── models/                 # SQLAlchemy models
│   │   ├── item.py             # Item model
│   │   └── __init__.py
│   │
│   ├── schemas/                # Pydantic schemas
│   │   ├── item.py             # Item schemas
│   │   └── __init__.py
│   │
│   ├── tests/                  # Tests directory
│   │
│   └── main.py                 # FastAPI application
│
├── .env                        # Environment variables (create this)
├── .gitignore                  # Git ignore file
├── main.py                     # Entry point
├── README.md                   # Project documentation
└── requirements.txt            # Project dependencies
```

## Features

- CRUD operations for items
- SQLAlchemy ORM with SQLite database
- Pydantic models for request/response validation
- Dependency injection for database sessions
- API documentation with Swagger/OpenAPI

## Installation

1. Clone the repository
```bash
git clone https://github.com/misranrifat/fast-api.git
cd fast-api
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application
```bash
python main.py
```

2. Open your browser and navigate to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc
   - Base URL: http://localhost:8000

## API Endpoints

| Method | URL                     | Description         |
|--------|-------------------------|---------------------|
| GET    | /api/v1/items           | List all items      |
| POST   | /api/v1/items           | Create a new item   |
| GET    | /api/v1/items/{item_id} | Get an item by ID   |
| PUT    | /api/v1/items/{item_id} | Update an item      |
| DELETE | /api/v1/items/{item_id} | Delete an item      |
| DELETE | /api/v1/items           | Delete all items    |

## Development

To run the development server with auto-reload:
```bash
uvicorn app.main:app --reload
``` 