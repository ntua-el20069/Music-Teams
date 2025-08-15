"""
Tests for all endpoints using requests library.
These tests assume that the server is up and running.
"""

import requests
import json
import sys
import os

# Configuration
BASE_URL = "http://localhost:5001"  # Update this if server runs on different port
TIMEOUT = 30


class TestAllEndpoints:
    """Test class for all endpoint functionality."""
    
    def __init__(self):
        self.base_url = BASE_URL
    
    def test_public_endpoints(self):
        """Test all public endpoints."""
        print("Testing public endpoints...")
        
        endpoints = [
            "/public/all-composers",
            "/public/all-lyricists", 
            "/public/all-songs"
        ]
        
        for endpoint in endpoints:
            url = f"{self.base_url}{endpoint}"
            print(f"Testing {url}...")
            
            try:
                response = requests.get(url, timeout=TIMEOUT)
                print(f"Status Code: {response.status_code}")
                
                if response.status_code == 200:
                    data = response.json()
                    print(f"Response: {json.dumps(data, indent=2)}")
                    
                    # Check response structure
                    if endpoint.endswith('composers'):
                        assert 'composers' in data
                        assert 'count' in data
                        assert isinstance(data['composers'], list)
                        print(f"✓ Found {data['count']} composers")
                    elif endpoint.endswith('lyricists'):
                        assert 'lyricists' in data
                        assert 'count' in data
                        assert isinstance(data['lyricists'], list)
                        print(f"✓ Found {data['count']} lyricists")
                    elif endpoint.endswith('songs'):
                        assert 'songs' in data
                        assert 'count' in data
                        assert isinstance(data['songs'], list)
                        print(f"✓ Found {data['count']} songs")
                        
                else:
                    print(f"✗ Request failed: {response.text}")
                    
            except requests.exceptions.RequestException as e:
                print(f"✗ Connection error: {e}")
            except Exception as e:
                print(f"✗ Test error: {e}")
                
            print()
    
    def test_myteams_endpoints(self):
        """Test all myteams endpoints."""
        print("Testing myteams endpoints...")
        
        endpoints = [
            "/myteams/all-composers",
            "/myteams/all-lyricists",
            "/myteams/all-songs"
        ]
        
        for endpoint in endpoints:
            url = f"{self.base_url}{endpoint}"
            print(f"Testing {url}...")
            
            try:
                response = requests.get(url, timeout=TIMEOUT)
                print(f"Status Code: {response.status_code}")
                
                if response.status_code == 200:
                    data = response.json()
                    print(f"Response: {json.dumps(data, indent=2)}")
                    
                    # Check response structure
                    if endpoint.endswith('composers'):
                        assert 'composers' in data
                        assert 'count' in data
                        assert 'user_teams' in data
                        assert isinstance(data['composers'], list)
                        print(f"✓ Found {data['count']} composers for user's teams")
                    elif endpoint.endswith('lyricists'):
                        assert 'lyricists' in data
                        assert 'count' in data
                        assert 'user_teams' in data
                        assert isinstance(data['lyricists'], list)
                        print(f"✓ Found {data['count']} lyricists for user's teams")
                    elif endpoint.endswith('songs'):
                        assert 'songs' in data
                        assert 'count' in data
                        assert 'user_teams' in data
                        assert isinstance(data['songs'], list)
                        print(f"✓ Found {data['count']} songs for user's teams")
                        
                else:
                    print(f"✗ Request failed: {response.text}")
                    
            except requests.exceptions.RequestException as e:
                print(f"✗ Connection error: {e}")
            except Exception as e:
                print(f"✗ Test error: {e}")
                
            print()
    
    def test_specific_team_endpoints(self):
        """Test all specific team endpoints."""
        print("Testing specific team endpoints...")
        
        endpoints = [
            "/specific_team/all-composers",
            "/specific_team/all-lyricists",
            "/specific_team/all-songs"
        ]
        
        test_team_name = "test_team"
        
        for endpoint in endpoints:
            url = f"{self.base_url}{endpoint}?team_name={test_team_name}"
            print(f"Testing {url}...")
            
            try:
                response = requests.get(url, timeout=TIMEOUT)
                print(f"Status Code: {response.status_code}")
                
                # Since team functionality is not implemented, we expect 403 (forbidden)
                # because user is not enrolled in the test team
                if response.status_code == 403:
                    data = response.json()
                    print(f"Expected response: {json.dumps(data, indent=2)}")
                    assert 'error' in data
                    print(f"✓ Correctly rejected access to team '{test_team_name}'")
                elif response.status_code == 200:
                    data = response.json()
                    print(f"Response: {json.dumps(data, indent=2)}")
                    
                    # Check response structure
                    if endpoint.endswith('composers'):
                        assert 'composers' in data
                        assert 'count' in data
                        assert 'team_name' in data
                        assert isinstance(data['composers'], list)
                        print(f"✓ Found {data['count']} composers for team {test_team_name}")
                    elif endpoint.endswith('lyricists'):
                        assert 'lyricists' in data
                        assert 'count' in data
                        assert 'team_name' in data
                        assert isinstance(data['lyricists'], list)
                        print(f"✓ Found {data['count']} lyricists for team {test_team_name}")
                    elif endpoint.endswith('songs'):
                        assert 'songs' in data
                        assert 'count' in data
                        assert 'team_name' in data
                        assert isinstance(data['songs'], list)
                        print(f"✓ Found {data['count']} songs for team {test_team_name}")
                        
                else:
                    print(f"✗ Request failed: {response.text}")
                    
            except requests.exceptions.RequestException as e:
                print(f"✗ Connection error: {e}")
            except Exception as e:
                print(f"✗ Test error: {e}")
                
            print()
        
        # Test missing team_name parameter
        print("Testing missing team_name parameter...")
        for endpoint in endpoints:
            url = f"{self.base_url}{endpoint}"  # No team_name parameter
            print(f"Testing {url}...")
            
            try:
                response = requests.get(url, timeout=TIMEOUT)
                print(f"Status Code: {response.status_code}")
                
                if response.status_code == 400:
                    data = response.json()
                    print(f"Expected response: {json.dumps(data, indent=2)}")
                    assert 'error' in data
                    print("✓ Correctly rejected request without team_name parameter")
                else:
                    print(f"✗ Expected 400 status code, got {response.status_code}")
                    
            except requests.exceptions.RequestException as e:
                print(f"✗ Connection error: {e}")
            except Exception as e:
                print(f"✗ Test error: {e}")
                
            print()
    
    def test_home_endpoint(self):
        """Test the home endpoint that lists all available endpoints."""
        print("Testing home endpoint...")
        
        url = f"{self.base_url}/"
        print(f"Testing {url}...")
        
        try:
            response = requests.get(url, timeout=TIMEOUT)
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"Response: {json.dumps(data, indent=2)}")
                
                assert 'message' in data
                assert 'endpoints' in data
                assert 'public' in data['endpoints']
                assert 'myteams' in data['endpoints']
                assert 'specific_team' in data['endpoints']
                print("✓ Home endpoint working correctly")
                
            else:
                print(f"✗ Request failed: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ Test error: {e}")
            
        print()
    
    def run_all_tests(self):
        """Run all tests."""
        print("=" * 60)
        print("RUNNING ALL ENDPOINT TESTS")
        print("=" * 60)
        print()
        
        self.test_home_endpoint()
        self.test_public_endpoints()
        self.test_myteams_endpoints()
        self.test_specific_team_endpoints()
        
        print("=" * 60)
        print("TESTS COMPLETED")
        print("=" * 60)


if __name__ == "__main__":
    # Check if server is running before running tests
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        print(f"Server is running at {BASE_URL}")
        print()
        
        # Run tests
        tester = TestAllEndpoints()
        tester.run_all_tests()
        
    except requests.exceptions.RequestException:
        print(f"Error: Server is not running at {BASE_URL}")
        print("Please start the server first using:")
        print("python backend/monolith/app.py")
        sys.exit(1)