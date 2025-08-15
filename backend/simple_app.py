"""
Simple standalone Flask app for testing the new monolith endpoints
"""
from flask import Flask, g, render_template
from monolith.routes.public import public_bp
from monolith.routes.my_teams import my_teams_bp
from monolith.routes.specific_team import specific_team_bp

app = Flask(__name__)

# Register new monolith blueprints
app.register_blueprint(public_bp)
app.register_blueprint(my_teams_bp)
app.register_blueprint(specific_team_bp)

# Simple home route
@app.route('/', methods=['GET'])
def home_route():
    return """
    <h1>Music Teams API</h1>
    <h2>Public Endpoints (require auth)</h2>
    <ul>
        <li><a href="/public/all-composers">GET /public/all-composers</a></li>
        <li><a href="/public/all-lyricists">GET /public/all-lyricists</a></li>
        <li><a href="/public/all-songs">GET /public/all-songs</a></li>
    </ul>
    <h2>My Teams Endpoints (require auth)</h2>
    <ul>
        <li><a href="/my_teams/all-composers">GET /my_teams/all-composers</a></li>
        <li><a href="/my_teams/all-lyricists">GET /my_teams/all-lyricists</a></li>
        <li><a href="/my_teams/all-songs">GET /my_teams/all-songs</a></li>
    </ul>
    <h2>Specific Team Endpoints (require auth + team_name param)</h2>
    <ul>
        <li><a href="/specific_team/all-composers?team_name=team1">GET /specific_team/all-composers?team_name=team1</a></li>
        <li><a href="/specific_team/all-lyricists?team_name=team1">GET /specific_team/all-lyricists?team_name=team1</a></li>
        <li><a href="/specific_team/all-songs?team_name=team1">GET /specific_team/all-songs?team_name=team1</a></li>
    </ul>
    <p><strong>Note:</strong> All endpoints require HTTP Basic Auth with username=AntonisNikos, password=ablaoublas</p>
    """

# Close database connection at the end of request
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

if __name__ == '__main__':
    app.run(debug=True, port=5001)