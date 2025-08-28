# Song Lists Feature

This implementation provides song list management functionality for the Music Teams application.

## Overview

- Users can create up to 3 song lists (numbered 1, 2, 3)
- Teams can also create up to 3 song lists (numbered 1, 2, 3)
- Each list can contain up to `MAX_SONGS_IN_LIST` songs (default: 300)
- Song lists are stored as JSON files in `backend/monolith/songlists/`

## File Structure

- User lists: `songlist-user{user_id}.json`
- Team lists: `songlist-team{team_name}.json`

Example JSON structure:
```json
{
  "1": [
    {"id": 234, "title": "I surrender"},
    {"id": 54, "title": "Welcome to the Jungle"}
  ],
  "2": [
    {"id": 66, "title": "zorbas the greek"}
  ],
  "3": []
}
```

## API Endpoints

### GET `/songlists/get-list`
Retrieve songs from a specific list.

**Parameters:**
- `songlist` (required): List number (1, 2, or 3)
- `team_name` (optional): Team name for team lists

**Response:**
```json
{
  "songs": [
    {"id": 234, "title": "Eye of the tiger"},
    ...
  ]
}
```

### GET `/songlists/add-song`
Add a song to the end of a specific list.

**Parameters:**
- `songlist` (required): List number (1, 2, or 3)
- `song_id` (required): ID of the song to add
- `team_name` (optional): Team name for team lists

**Response:**
```json
{
  "message": "Song 'Song Title' added to list 1"
}
```

### POST `/songlists/save-list`
Save/reshape a complete song list.

**Request Body:**
```json
{
  "songlist_id": 2,
  "songs": [12, 345, 54, 23],
  "team_name": "MyTeam"
}
```

**Response:**
```json
{
  "message": "Song list 2 saved with 4 songs"
}
```

## Permissions

### User Lists
- Songs must be accessible to the user (created by user or shared with user's teams)

### Team Lists
- User must be enrolled in the specified team
- User must have `can_edit = True` permission for the team
- Songs must be shared with the team

## Environment Variables

Add to `.env`:
```
MAX_SONGS_IN_LIST=300
```

## Files Added/Modified

- `backend/env_template` - Added MAX_SONGS_IN_LIST variable
- `backend/monolith/models/models.py` - Added SongListSaveModel and SongInListModel
- `backend/monolith/routes/songlists.py` - New API routes
- `backend/monolith/utils/songlists.py` - New utility functions
- `backend/monolith/app.py` - Registered new router
- `backend/tests/test_songlists_basic.py` - Unit tests