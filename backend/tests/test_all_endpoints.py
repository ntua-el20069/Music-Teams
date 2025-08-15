"""
Tests for the Music Teams all-endpoints API
Uses requests to test the endpoints while server is running
"""
import requests
import json
import base64
from unittest import TestCase, main


class TestMusicTeamsEndpoints(TestCase):
    
    def setUp(self):
        """Set up test configuration"""
        self.base_url = "http://localhost:5001"
        self.username = "AntonisNikos"
        self.password = "ablaoublas"
        
        # Create Basic Auth header
        credentials = f"{self.username}:{self.password}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        self.auth_headers = {
            'Authorization': f'Basic {encoded_credentials}',
            'Content-Type': 'application/json'
        }
        
        # Headers without auth for testing auth required endpoints
        self.no_auth_headers = {
            'Content-Type': 'application/json'
        }
    
    def test_public_all_composers(self):
        """Test GET /public/all-composers endpoint"""
        response = requests.get(f"{self.base_url}/public/all-composers", headers=self.auth_headers)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('composers', data)
        self.assertIn('count', data)
        self.assertIsInstance(data['composers'], list)
        self.assertEqual(data['count'], len(data['composers']))
    
    def test_public_all_composers_no_auth(self):
        """Test GET /public/all-composers endpoint without authentication"""
        response = requests.get(f"{self.base_url}/public/all-composers", headers=self.no_auth_headers)
        self.assertEqual(response.status_code, 401)
        
        data = response.json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Authentication required')
    
    def test_public_all_lyricists(self):
        """Test GET /public/all-lyricists endpoint"""
        response = requests.get(f"{self.base_url}/public/all-lyricists", headers=self.auth_headers)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('lyricists', data)
        self.assertIn('count', data)
        self.assertIsInstance(data['lyricists'], list)
        self.assertEqual(data['count'], len(data['lyricists']))
    
    def test_public_all_lyricists_no_auth(self):
        """Test GET /public/all-lyricists endpoint without authentication"""
        response = requests.get(f"{self.base_url}/public/all-lyricists", headers=self.no_auth_headers)
        self.assertEqual(response.status_code, 401)
    
    def test_public_all_songs(self):
        """Test GET /public/all-songs endpoint"""
        response = requests.get(f"{self.base_url}/public/all-songs", headers=self.auth_headers)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('songs', data)
        self.assertIn('count', data)
        self.assertIsInstance(data['songs'], list)
        self.assertEqual(data['count'], len(data['songs']))
        
        # Check song structure
        if data['songs']:
            song = data['songs'][0]
            self.assertIn('id', song)
            self.assertIn('title', song)
            self.assertIn('made_by', song)
    
    def test_public_all_songs_no_auth(self):
        """Test GET /public/all-songs endpoint without authentication"""
        response = requests.get(f"{self.base_url}/public/all-songs", headers=self.no_auth_headers)
        self.assertEqual(response.status_code, 401)
    
    def test_my_teams_all_composers(self):
        """Test GET /my_teams/all-composers endpoint"""
        response = requests.get(f"{self.base_url}/my_teams/all-composers", headers=self.auth_headers)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('composers', data)
        self.assertIn('count', data)
        self.assertIn('user', data)
        self.assertEqual(data['user'], self.username)
        self.assertIsInstance(data['composers'], list)
    
    def test_my_teams_all_lyricists(self):
        """Test GET /my_teams/all-lyricists endpoint"""
        response = requests.get(f"{self.base_url}/my_teams/all-lyricists", headers=self.auth_headers)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('lyricists', data)
        self.assertIn('count', data)
        self.assertIn('user', data)
        self.assertEqual(data['user'], self.username)
        self.assertIsInstance(data['lyricists'], list)
    
    def test_my_teams_all_songs(self):
        """Test GET /my_teams/all-songs endpoint"""
        response = requests.get(f"{self.base_url}/my_teams/all-songs", headers=self.auth_headers)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('songs', data)
        self.assertIn('count', data)
        self.assertIn('user', data)
        self.assertEqual(data['user'], self.username)
        self.assertIsInstance(data['songs'], list)
    
    def test_my_teams_no_auth(self):
        """Test my_teams endpoints without authentication"""
        endpoints = ['/my_teams/all-composers', '/my_teams/all-lyricists', '/my_teams/all-songs']
        
        for endpoint in endpoints:
            response = requests.get(f"{self.base_url}{endpoint}", headers=self.no_auth_headers)
            self.assertEqual(response.status_code, 401)
    
    def test_specific_team_all_composers(self):
        """Test GET /specific_team/all-composers endpoint"""
        team_name = "team1"
        response = requests.get(
            f"{self.base_url}/specific_team/all-composers?team_name={team_name}", 
            headers=self.auth_headers
        )
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('composers', data)
        self.assertIn('count', data)
        self.assertIn('team', data)
        self.assertIn('user', data)
        self.assertEqual(data['team'], team_name)
        self.assertEqual(data['user'], self.username)
        self.assertIsInstance(data['composers'], list)
    
    def test_specific_team_all_lyricists(self):
        """Test GET /specific_team/all-lyricists endpoint"""
        team_name = "team1"
        response = requests.get(
            f"{self.base_url}/specific_team/all-lyricists?team_name={team_name}", 
            headers=self.auth_headers
        )
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('lyricists', data)
        self.assertIn('count', data)
        self.assertIn('team', data)
        self.assertIn('user', data)
        self.assertEqual(data['team'], team_name)
        self.assertEqual(data['user'], self.username)
        self.assertIsInstance(data['lyricists'], list)
    
    def test_specific_team_all_songs(self):
        """Test GET /specific_team/all-songs endpoint"""
        team_name = "team1"
        response = requests.get(
            f"{self.base_url}/specific_team/all-songs?team_name={team_name}", 
            headers=self.auth_headers
        )
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('songs', data)
        self.assertIn('count', data)
        self.assertIn('team', data)
        self.assertIn('user', data)
        self.assertEqual(data['team'], team_name)
        self.assertEqual(data['user'], self.username)
        self.assertIsInstance(data['songs'], list)
    
    def test_specific_team_no_team_name(self):
        """Test specific_team endpoints without team_name parameter"""
        endpoints = ['/specific_team/all-composers', '/specific_team/all-lyricists', '/specific_team/all-songs']
        
        for endpoint in endpoints:
            response = requests.get(f"{self.base_url}{endpoint}", headers=self.auth_headers)
            self.assertEqual(response.status_code, 400)
            
            data = response.json()
            self.assertIn('error', data)
            self.assertEqual(data['error'], 'team_name parameter required')
    
    def test_specific_team_invalid_team(self):
        """Test specific_team endpoints with invalid team name"""
        team_name = "invalid_team"
        endpoints = ['/specific_team/all-composers', '/specific_team/all-lyricists', '/specific_team/all-songs']
        
        for endpoint in endpoints:
            response = requests.get(
                f"{self.base_url}{endpoint}?team_name={team_name}", 
                headers=self.auth_headers
            )
            self.assertEqual(response.status_code, 403)
            
            data = response.json()
            self.assertIn('error', data)
            self.assertEqual(data['error'], f'User not enrolled in team {team_name}')
    
    def test_specific_team_no_auth(self):
        """Test specific_team endpoints without authentication"""
        team_name = "team1"
        endpoints = ['/specific_team/all-composers', '/specific_team/all-lyricists', '/specific_team/all-songs']
        
        for endpoint in endpoints:
            response = requests.get(
                f"{self.base_url}{endpoint}?team_name={team_name}", 
                headers=self.no_auth_headers
            )
            self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    print("Running Music Teams API tests...")
    print("Make sure the server is running on http://localhost:5001")
    main()