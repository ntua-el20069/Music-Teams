# Music Teams API - All Endpoints

This document describes the new monolith structure and API endpoints for the Music Teams application.

## Project Structure

```
backend/
├── monolith/
│   ├── __init__.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── auth.py          # Authentication utilities
│   │   └── queries.py       # Database query functions
│   └── routes/
│       ├── __init__.py
│       ├── public.py        # Public endpoints
│       ├── my_teams.py      # User teams endpoints
│       └── specific_team.py # Specific team endpoints
├── tests/
│   ├── __init__.py
│   └── test_all_endpoints.py # Comprehensive test suite
├── simple_app.py            # Standalone Flask app for testing
└── monolith_app.py          # Full Flask app with legacy compatibility
```

## API Endpoints

### Authentication

All endpoints require HTTP Basic Authentication:
- Username: `AntonisNikos`
- Password: `ablaoublas`

### Public Endpoints

These endpoints return data from public songs (songs with `public=1` in the database).

#### GET `/public/all-composers`
Returns all composers that are in public songs.

**Response:**
```json
{
  "composers": ["Μίκης Θεοδωράκης", "Lennon", "MacCartney", ...],
  "count": 15
}
```

#### GET `/public/all-lyricists`
Returns all lyricists that are in public songs.

**Response:**
```json
{
  "lyricists": ["Μίκης Θεοδωράκης", "Lennon", "MacCartney", ...],
  "count": 12
}
```

#### GET `/public/all-songs`
Returns all public songs with basic information.

**Response:**
```json
{
  "songs": [
    {
      "id": 2,
      "title": "Μαργαρίτα Μαργαρώ",
      "made_by": "AntonisNikos"
    },
    ...
  ],
  "count": 8
}
```

### My Teams Endpoints

These endpoints return data from songs in teams where the authenticated user participates.

#### GET `/my_teams/all-composers`
Returns all composers that are in songs in teams in which the user participates.

**Response:**
```json
{
  "composers": ["Μίκης Θεοδωράκης", "Διονύσης Σαββόπουλος", ...],
  "count": 25,
  "user": "AntonisNikos"
}
```

#### GET `/my_teams/all-lyricists`
Returns all lyricists that are in songs in teams in which the user participates.

**Response:**
```json
{
  "lyricists": ["Ρίτσος", "Διονύσης Σαββόπουλος", ...],
  "count": 22,
  "user": "AntonisNikos"
}
```

#### GET `/my_teams/all-songs`
Returns all songs in teams in which the user participates.

**Response:**
```json
{
  "songs": [
    {
      "id": 1,
      "title": "Αυτά τα δέντρα",
      "made_by": "AntonisNikos"
    },
    ...
  ],
  "count": 35,
  "user": "AntonisNikos"
}
```

### Specific Team Endpoints

These endpoints return data from songs in a specific team. Requires user to be enrolled in the specified team.

#### GET `/specific_team/all-composers?team_name=<team_name>`
Returns all composers that are in songs in the specified team.

**Parameters:**
- `team_name` (required): Name of the team

**Response:**
```json
{
  "composers": ["Μίκης Θεοδωράκης", "Διονύσης Σαββόπουλος", ...],
  "count": 12,
  "team": "team1",
  "user": "AntonisNikos"
}
```

#### GET `/specific_team/all-lyricists?team_name=<team_name>`
Returns all lyricists that are in songs in the specified team.

**Parameters:**
- `team_name` (required): Name of the team

**Response:**
```json
{
  "lyricists": ["Ρίτσος", "Διονύσης Σαββόπουλος", ...],
  "count": 10,
  "team": "team1",
  "user": "AntonisNikos"
}
```

#### GET `/specific_team/all-songs?team_name=<team_name>`
Returns all songs in the specified team.

**Parameters:**
- `team_name` (required): Name of the team

**Response:**
```json
{
  "songs": [
    {
      "id": 1,
      "title": "Αυτά τα δέντρα",
      "made_by": "AntonisNikos"
    },
    ...
  ],
  "count": 15,
  "team": "team1",
  "user": "AntonisNikos"
}
```

## Error Responses

### Authentication Required (401)
```json
{
  "error": "Authentication required"
}
```

### Missing Team Parameter (400)
```json
{
  "error": "team_name parameter required"
}
```

### Not Enrolled in Team (403)
```json
{
  "error": "User not enrolled in team invalid_team"
}
```

### Server Error (500)
```json
{
  "error": "Database connection failed"
}
```

## Running the Application

### Development Server
```bash
cd backend
python simple_app.py
```

Server will start on `http://localhost:5001`

### Running Tests
```bash
cd backend
python tests/test_all_endpoints.py
```

**Note:** Server must be running for tests to work.

## Example Usage

### Using curl

```bash
# Get public composers
curl -u "AntonisNikos:ablaoublas" http://localhost:5001/public/all-composers

# Get songs in team1
curl -u "AntonisNikos:ablaoublas" "http://localhost:5001/specific_team/all-songs?team_name=team1"
```

### Using Python requests

```python
import requests
import base64

# Setup authentication
credentials = "AntonisNikos:ablaoublas"
encoded_credentials = base64.b64encode(credentials.encode()).decode()
headers = {"Authorization": f"Basic {encoded_credentials}"}

# Get public songs
response = requests.get("http://localhost:5001/public/all-songs", headers=headers)
print(response.json())

# Get team composers
response = requests.get(
    "http://localhost:5001/specific_team/all-composers?team_name=team1", 
    headers=headers
)
print(response.json())
```

## Team System

The current implementation uses a simplified team system:
- Users can belong to multiple teams
- Teams are identified by name (e.g., "team1", "team2", "default_team")
- Currently hardcoded for demonstration - can be enhanced with proper database tables

### Available Teams for AntonisNikos:
- `team1`
- `team2`
- `default_team`

## Database Queries

All endpoints use efficient SQL queries with proper JOINs:
- Public endpoints filter by `song.public = 1`
- Team endpoints filter by team membership and song association
- Parameterized queries prevent SQL injection
- Results are ordered alphabetically for consistency

## Future Enhancements

1. **Team Management**: Add proper team tables and management endpoints
2. **User Management**: Add user registration and management
3. **Permissions**: Add role-based access control within teams
4. **Caching**: Add Redis caching for frequently accessed data
5. **Pagination**: Add pagination for large result sets
6. **Search**: Add search functionality within teams/public songs