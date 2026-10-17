# FastAPI Library API

A simple library management REST API built with FastAPI and Pydantic. This project allows users to create, retrieve, update, and delete books without using a database. Book data is stored in an in-memory Python list.

## Features

- Retrieve all books
- Add a new book
- Retrieve a book by ID
- Update book information using PATCH
- Delete a book by ID
- Validate request data using Pydantic
- Handle errors for books that do not exist
- Automatically generate interactive API documentation

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```text
fastapi-library-api/
├── main.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-library-api.git
cd fastapi-library-api
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Run the following command in the directory containing `main.py`:

```bash
uvicorn main:app --reload
```

The server will start at:

http://127.0.0.1:8000

## API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

You can use Swagger UI to test all endpoints directly in your browser.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/books` | Retrieve all books |
| POST | `/books` | Add a new book |
| GET | `/books/{id}` | Retrieve a book by ID |
| PATCH | `/books/{id}` | Update a book |
| DELETE | `/books/{id}` | Delete a book |

## Example Requests

### 1. Retrieve All Books

```http
GET /books
```

Returns a list of all books.

### 2. Add a New Book

```http
POST /books
```

Request body:

```json
{
  "title": "Python Crash Course",
  "author": "Eric Matthes",
  "year": 2019,
  "available": true
}
```

A successful request returns `201 Created` and the new book, including its automatically assigned ID.

### 3. Retrieve a Book by ID

```http
GET /books/1
```

Returns the details of the book with ID `1`.

If the book does not exist, the API returns `404 Not Found`.

### 4. Update a Book

```http
PATCH /books/1
```

Request body:

```json
{
  "available": false
}
```

Only the fields provided in the request are updated. Other fields remain unchanged.

Explicitly provided `null` values are rejected with `422 Unprocessable Entity`.

### 5. Delete a Book

```http
DELETE /books/1
```

Deletes the book with ID `1`.

A successful request returns `204 No Content`. If the book does not exist, the API returns `404 Not Found`.

## Data Storage

This project uses an in-memory Python list instead of a database.

**Note:** Changes are temporary and will be lost when the application restarts. The initial sample books will be loaded again.

## License

This project was developed for educational purposes.
