"""
Test file for FastAPI endpoints.
Uses requests library to test all endpoints.
"""

import requests
import base64
from typing import Dict


class FastAPITester:
    """Test class for FastAPI all-endpoints."""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.auth_headers = self._get_auth_headers()
    
    def _get_auth_headers(self) -> Dict[str, str]:
        """Get authentication headers for requests."""
        # Using basic auth with demo credentials
        credentials = base64.b64encode(b"demo_user:demo_password").decode("ascii")
        return {"Authorization": f"Basic {credentials}"}
    
    def test_root_endpoint(self):
        """Test the root endpoint."""
        print("Testing root endpoint...")
        response = requests.get(f"{self.base_url}/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "endpoints" in data
        print("✓ Root endpoint working")
    
    def test_health_endpoint(self):
        """Test the health check endpoint."""
        print("Testing health endpoint...")
        response = requests.get(f"{self.base_url}/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        print("✓ Health endpoint working")
    
    def test_public_endpoints(self):
        """Test all public endpoints."""
        print("\nTesting public endpoints...")
        
        # Test public composers
        response = requests.get(f"{self.base_url}/public/all-composers")
        assert response.status_code == 200
        data = response.json()
        assert "composers" in data
        assert "count" in data
        assert isinstance(data["composers"], list)
        assert data["count"] == len(data["composers"])
        print(f"✓ Public composers: {data['count']} found")
        
        # Test public lyricists
        response = requests.get(f"{self.base_url}/public/all-lyricists")
        assert response.status_code == 200
        data = response.json()
        assert "lyricists" in data
        assert "count" in data
        assert isinstance(data["lyricists"], list)
        assert data["count"] == len(data["lyricists"])
        print(f"✓ Public lyricists: {data['count']} found")
        
        # Test public songs
        response = requests.get(f"{self.base_url}/public/all-songs")
        assert response.status_code == 200
        data = response.json()
        assert "songs" in data
        assert "count" in data
        assert isinstance(data["songs"], list)
        assert data["count"] == len(data["songs"])
        print(f"✓ Public songs: {data['count']} found")
    
    def test_myteams_endpoints(self):
        """Test all myteams endpoints (require authentication)."""
        print("\nTesting myteams endpoints...")
        
        # Test myteams composers
        response = requests.get(
            f"{self.base_url}/myteams/all-composers",
            headers=self.auth_headers
        )
        assert response.status_code == 200
        data = response.json()
        assert "composers" in data
        assert "count" in data
        assert isinstance(data["composers"], list)
        print(f"✓ MyTeams composers: {data['count']} found")
        
        # Test myteams lyricists
        response = requests.get(
            f"{self.base_url}/myteams/all-lyricists",
            headers=self.auth_headers
        )
        assert response.status_code == 200
        data = response.json()
        assert "lyricists" in data
        assert "count" in data
        assert isinstance(data["lyricists"], list)
        print(f"✓ MyTeams lyricists: {data['count']} found")
        
        # Test myteams songs
        response = requests.get(
            f"{self.base_url}/myteams/all-songs",
            headers=self.auth_headers
        )
        assert response.status_code == 200
        data = response.json()
        assert "songs" in data
        assert "count" in data
        assert isinstance(data["songs"], list)
        print(f"✓ MyTeams songs: {data['count']} found")
    
    def test_myteams_unauthorized(self):
        """Test that myteams endpoints require authentication."""
        print("\nTesting myteams authentication...")
        
        # Test without auth headers
        response = requests.get(f"{self.base_url}/myteams/all-composers")
        assert response.status_code == 401
        print("✓ MyTeams endpoints properly require authentication")
    
    def test_specific_team_endpoints(self):
        """Test specific team endpoints."""
        print("\nTesting specific team endpoints...")
        
        team_name = "team1"  # Use an allowed team name
        
        # Test team composers
        response = requests.get(
            f"{self.base_url}/specific_team/all-composers",
            params={"team_name": team_name},
            headers=self.auth_headers
        )
        assert response.status_code == 200
        data = response.json()
        assert "composers" in data
        assert "count" in data
        assert isinstance(data["composers"], list)
        print(f"✓ Team '{team_name}' composers: {data['count']} found")
        
        # Test team lyricists
        response = requests.get(
            f"{self.base_url}/specific_team/all-lyricists",
            params={"team_name": team_name},
            headers=self.auth_headers
        )
        assert response.status_code == 200
        data = response.json()
        assert "lyricists" in data
        assert "count" in data
        assert isinstance(data["lyricists"], list)
        print(f"✓ Team '{team_name}' lyricists: {data['count']} found")
        
        # Test team songs
        response = requests.get(
            f"{self.base_url}/specific_team/all-songs",
            params={"team_name": team_name},
            headers=self.auth_headers
        )
        assert response.status_code == 200
        data = response.json()
        assert "songs" in data
        assert "count" in data
        assert isinstance(data["songs"], list)
        print(f"✓ Team '{team_name}' songs: {data['count']} found")
    
    def test_specific_team_missing_param(self):
        """Test specific team endpoints with missing team_name parameter."""
        print("\nTesting specific team parameter validation...")
        
        # Test without team_name parameter
        response = requests.get(
            f"{self.base_url}/specific_team/all-composers",
            headers=self.auth_headers
        )
        assert response.status_code == 400
        data = response.json()
        assert "team_name parameter is required" in data["detail"]
        print("✓ Specific team endpoints properly validate team_name parameter")
    
    def test_specific_team_unauthorized_team(self):
        """Test specific team endpoints with unauthorized team."""
        print("\nTesting specific team authorization...")
        
        # Test with unauthorized team name
        response = requests.get(
            f"{self.base_url}/specific_team/all-composers",
            params={"team_name": "unauthorized_team"},
            headers=self.auth_headers
        )
        assert response.status_code == 403
        data = response.json()
        assert "not enrolled in team" in data["detail"]
        print("✓ Specific team endpoints properly check team enrollment")
    
    def run_all_tests(self):
        """Run all tests."""
        print("Starting FastAPI All-Endpoints Tests")
        print("=" * 50)
        
        try:
            self.test_root_endpoint()
            self.test_health_endpoint()
            self.test_public_endpoints()
            self.test_myteams_endpoints()
            self.test_myteams_unauthorized()
            self.test_specific_team_endpoints()
            self.test_specific_team_missing_param()
            self.test_specific_team_unauthorized_team()
            
            print("\n" + "=" * 50)
            print("✓ All tests passed successfully!")
            
        except AssertionError as e:
            print(f"\n❌ Test failed: {e}")
            raise
        except requests.exceptions.ConnectionError:
            print("\n❌ Could not connect to FastAPI server.")
            print("Make sure the server is running on http://localhost:8000")
            raise


if __name__ == "__main__":
    tester = FastAPITester()
    tester.run_all_tests()