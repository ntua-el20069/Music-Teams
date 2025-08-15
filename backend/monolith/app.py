"""
Main application file for the new endpoints.
This file can be used to register the new blueprints with the main Flask app.
"""

from flask import Flask
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import the blueprints
from monolith.routes.all_public import public_bp
from monolith.routes.all_myteams import myteams_bp
from monolith.routes.all_team import specific_team_bp


def register_all_endpoints(app: Flask):
    """
    Register all the new endpoints with the Flask app.
    
    Args:
        app: Flask application instance
    """
    app.register_blueprint(public_bp)
    app.register_blueprint(myteams_bp)
    app.register_blueprint(specific_team_bp)


if __name__ == "__main__":
    # For testing purposes - create a simple Flask app
    app = Flask(__name__)
    register_all_endpoints(app)
    
    @app.route('/')
    def home():
        return {
            "message": "Music Teams All-Endpoints API",
            "endpoints": {
                "public": [
                    "GET /public/all-composers",
                    "GET /public/all-lyricists", 
                    "GET /public/all-songs"
                ],
                "myteams": [
                    "GET /myteams/all-composers",
                    "GET /myteams/all-lyricists",
                    "GET /myteams/all-songs"
                ],
                "specific_team": [
                    "GET /specific_team/all-composers?team_name=<name>",
                    "GET /specific_team/all-lyricists?team_name=<name>",
                    "GET /specific_team/all-songs?team_name=<name>"
                ]
            }
        }
    
    app.run(debug=True, port=5001)