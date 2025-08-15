# FastAPI All-Endpoints Implementation

This document describes the FastAPI-based implementation of the all-endpoints API for the Music Teams application.

## Overview

This implementation replaces the Flask-based approach with a modern FastAPI application, following the concepts from `backend/all.py` but extending them to support three different access scenarios:

1. **Public Endpoints** - Access to public songs data
2. **MyTeams Endpoints** - Access to songs from the current user's teams (requires authentication)
3. **Specific Team Endpoints** - Access to songs from a specific team (requires authentication and team enrollment)

## Architecture

```
backend/fastapi_app/
├── main.py                 # FastAPI app instance and configuration
├── models/
│   └── responses.py        # Pydantic response models
├── routers/
│   ├── public.py          # Public endpoints router
│   ├── myteams.py         # MyTeams endpoints router
│   └── specific_team.py   # Specific team endpoints router
└── utils/
    ├── database.py        # Database connection and query functions
    └── auth.py           # Authentication and authorization utilities
```

## Key Features

### 1. Database Integration
- Reuses the existing database connection logic from `backend/__init__.py`
- Implements the core functions from `backend/all.py` with proper connection management
- Extends with public-only queries using SQL JOINs for better performance
- Includes placeholder functions for team-related queries (ready for team table implementation)

### 2. Authentication & Authorization
- HTTP Basic Authentication for simplicity (easily replaceable with JWT)
- User enrollment validation for team access
- Proper error handling with appropriate HTTP status codes

### 3. API Documentation
- Automatic OpenAPI/Swagger documentation
- Comprehensive response models with examples
- Detailed endpoint descriptions and parameter documentation

### 4. Error Handling
- Proper HTTP status codes (400, 401, 403, 500)
- Structured error responses
- Database connection error handling

## Endpoints

### Public Endpoints (No Authentication Required)

- `GET /public/all-composers` - Get composers from public songs
- `GET /public/all-lyricists` - Get lyricists from public songs  
- `GET /public/all-songs` - Get all public songs

### MyTeams Endpoints (Authentication Required)

- `GET /myteams/all-composers` - Get composers from user's team songs
- `GET /myteams/all-lyricists` - Get lyricists from user's team songs
- `GET /myteams/all-songs` - Get songs from user's teams

### Specific Team Endpoints (Authentication + Team Enrollment Required)

- `GET /specific_team/all-composers?team_name=<name>` - Get composers from specific team
- `GET /specific_team/all-lyricists?team_name=<name>` - Get lyricists from specific team  
- `GET /specific_team/all-songs?team_name=<name>` - Get songs from specific team

## Running the Application

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements_fastapi.txt
```

### 2. Run the Server

```bash
cd backend
python run_fastapi.py
```

The server will start on `http://localhost:8000`

### 3. View API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 4. Run Tests

```bash
cd backend
python test_fastapi_endpoints.py
```

## Authentication

For testing purposes, use these credentials:
- Username: `demo_user`
- Password: `demo_password`

Example curl request:
```bash
curl -u demo_user:demo_password http://localhost:8000/myteams/all-composers
```

## Database Configuration

The application uses the same database configuration as the existing codebase:
- Local mode: MySQL on localhost:3307 with database "songs"
- Web mode: PythonAnywhere MySQL database

To change the mode, edit `backend/fastapi_app/utils/database.py`:
```python
mode = 'local'  # or 'web'
```

## Team Functionality

Since team tables don't exist yet, the implementation includes placeholder functions with:
- Complete function signatures matching expected usage
- TODO comments with the expected SQL queries
- Mock data for testing purposes

Once team tables are created, simply replace the placeholder functions in `database.py` with actual database queries.

## Response Format

All endpoints return JSON responses with a consistent structure:

```json
{
  "composers": ["John Lennon", "Paul McCartney"],
  "count": 2
}
```

Error responses follow this format:
```json
{
  "detail": "Error description",
  "error_code": "ERROR_TYPE"
}
```

## Comparison with Flask Implementation

### Advantages of FastAPI approach:
1. **Automatic API Documentation** - Built-in Swagger/OpenAPI docs
2. **Type Safety** - Pydantic models ensure response validation
3. **Better Performance** - Async support and faster request handling
4. **Modern Python** - Uses type hints and modern async/await patterns
5. **Dependency Injection** - Clean separation of concerns with FastAPI dependencies
6. **Better Testing** - Built-in test client and easier mocking

### Migration from Flask:
The FastAPI implementation maintains the same endpoint structure and functionality as the original Flask version, making it a drop-in replacement.

## Next Steps

1. **Create Team Tables** - Implement the actual team database schema
2. **Replace Placeholder Functions** - Update team-related functions with real SQL queries
3. **Enhanced Authentication** - Implement JWT-based authentication
4. **Database Connection Pooling** - Add connection pooling for better performance
5. **Logging** - Add structured logging for better monitoring
6. **Rate Limiting** - Add rate limiting for production use