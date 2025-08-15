# All Endpoints Implementation - EPIC #3 Task #1

This implementation provides the requested "all" endpoints for the Music Teams application.

## Structure

```
backend/
├── monolith/
│   ├── __init__.py
│   ├── app.py                    # Main application file to register blueprints
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── all_utils.py          # Main utility functions for getting data
│   │   └── team_utils.py         # Team-related utility functions (placeholder)
│   └── routes/
│       ├── __init__.py
│       ├── all_public.py         # Public endpoints
│       ├── all_myteams.py        # User's teams endpoints
│       └── all_team.py           # Specific team endpoints
├── tests/
│   └── test_all_endpoints.py     # Test suite using requests
├── test_app.py                   # Simplified test server
└── enhanced_test_app.py          # Enhanced test server with DB connection
```

## Endpoints Implemented

### Public Endpoints
Requires authenticated user (depends on `get_current_user`)

- `GET /public/all-composers` - Returns all composers that are in public songs
- `GET /public/all-lyricists` - Returns all lyricists that are in public songs  
- `GET /public/all-songs` - Returns all public songs

### My Teams Endpoints
Requires authenticated user and access to `team_data` cookie (depends on `get_current_user` and `get_teams_of_user`)

- `GET /myteams/all-composers` - Returns all composers that are in songs in teams in which the user participates
- `GET /myteams/all-lyricists` - Returns all lyricists that are in songs in teams in which the user participates
- `GET /myteams/all-songs` - Returns all songs in teams in which the user participates

### Specific Team Endpoints
Requires authenticated user and access to `team_data` cookie (depends on `get_current_user`, `get_teams_of_user`, and `team_if_enrolled`)

- `GET /specific_team/all-composers?team_name=sample_name` - Returns all composers that are in songs in the team specified by `team_name`
- `GET /specific_team/all-lyricists?team_name=sample_name` - Returns all lyricists that are in songs in the team specified by `team_name`
- `GET /specific_team/all-songs?team_name=sample_name` - Returns all songs in the team specified by `team_name`

## Usage

### Integration with existing Flask app

```python
from backend.monolith.app import register_all_endpoints

# In your main Flask app
app = Flask(__name__)
register_all_endpoints(app)
```

### Testing

1. **Simple testing without database:**
   ```bash
   cd backend
   python test_app.py
   python tests/test_all_endpoints.py
   ```

2. **Enhanced testing with database:**
   ```bash
   cd backend  
   python enhanced_test_app.py
   python tests/test_all_endpoints.py
   ```

## Implementation Notes

### Current Status

1. **✅ Public endpoints** - Fully implemented with database queries
2. **⚠️ Team endpoints** - Structure implemented but team functionality is placeholder
3. **✅ Authentication** - Placeholder implementation ready for integration
4. **✅ Tests** - Comprehensive test suite using requests library

### Database Queries

The public endpoints use proper SQL queries:

```sql
-- Get composers from public songs
SELECT DISTINCT c.name 
FROM composer c 
JOIN wrotemusic wm ON c.name = wm.composer 
JOIN song s ON wm.song_id = s.id 
WHERE s.public = 1
ORDER BY c.name
```

### Team Functionality Placeholder

The team-related functions (`get_teams_of_user`, `team_if_enrolled`) are implemented as placeholders that:
- Return empty lists/False for now
- Include TODO comments with the expected SQL queries
- Are ready to be replaced with actual implementation once team tables are created

### Response Format

All endpoints return JSON responses with consistent structure:

```json
{
  "composers": ["name1", "name2"],
  "count": 2,
  "additional_info": "..."
}
```

Error responses:
```json
{
  "error": "Error message"
}
```

## Next Steps

1. **Implement team tables** in the database:
   - `team` table (team_name, description, created_by, etc.)
   - `user_teams` table (username, team_name, role, etc.)
   - `team_songs` table (team_name, song_id, added_by, etc.)

2. **Replace placeholder functions** in `team_utils.py` with actual database queries

3. **Implement proper authentication** to replace the placeholder `get_current_user` function

4. **Add cookie handling** for `team_data` cookie access

5. **Integration** with the main Flask application

## Database Schema Requirements

For full functionality, these tables need to be added:

```sql
-- Team table
CREATE TABLE team (
    name VARCHAR(50) PRIMARY KEY,
    description TEXT,
    created_by VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES user(username)
);

-- User-Team relationship
CREATE TABLE user_teams (
    username VARCHAR(20),
    team_name VARCHAR(50),
    role ENUM('member', 'admin') DEFAULT 'member',
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (username, team_name),
    FOREIGN KEY (username) REFERENCES user(username),
    FOREIGN KEY (team_name) REFERENCES team(name)
);

-- Team-Song relationship  
CREATE TABLE team_songs (
    team_name VARCHAR(50),
    song_id INT,
    added_by VARCHAR(20),
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (team_name, song_id),
    FOREIGN KEY (team_name) REFERENCES team(name),
    FOREIGN KEY (song_id) REFERENCES song(id),
    FOREIGN KEY (added_by) REFERENCES user(username)
);
```