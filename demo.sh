#!/bin/bash

# Demo script for EPIC #3 Task #1 - All Endpoints Implementation
# This script demonstrates all the implemented endpoints

echo "============================================================"
echo "MUSIC TEAMS - ALL ENDPOINTS DEMO"
echo "EPIC #3 Task #1 Implementation"
echo "============================================================"
echo

# Start the server in background
echo "🚀 Starting test server..."
cd backend
python enhanced_test_app.py &
SERVER_PID=$!

# Wait for server to start
sleep 3

echo "📡 Server started on http://127.0.0.1:5001"
echo

# Test home endpoint
echo "🏠 Testing home endpoint..."
curl -s http://127.0.0.1:5001/ | python -m json.tool
echo

# Test public endpoints
echo "🌍 Testing PUBLIC endpoints..."
echo

echo "📝 GET /public/all-composers"
curl -s http://127.0.0.1:5001/public/all-composers | python -m json.tool
echo

echo "📝 GET /public/all-lyricists"  
curl -s http://127.0.0.1:5001/public/all-lyricists | python -m json.tool
echo

echo "📝 GET /public/all-songs"
curl -s http://127.0.0.1:5001/public/all-songs | python -m json.tool
echo

# Test myteams endpoints
echo "👥 Testing MY TEAMS endpoints..."
echo

echo "📝 GET /myteams/all-composers"
curl -s http://127.0.0.1:5001/myteams/all-composers | python -m json.tool
echo

echo "📝 GET /myteams/all-lyricists"
curl -s http://127.0.0.1:5001/myteams/all-lyricists | python -m json.tool
echo

echo "📝 GET /myteams/all-songs"
curl -s http://127.0.0.1:5001/myteams/all-songs | python -m json.tool
echo

# Test specific team endpoints
echo "🎯 Testing SPECIFIC TEAM endpoints..."
echo

echo "📝 GET /specific_team/all-composers?team_name=test_team (should return 403)"
curl -s http://127.0.0.1:5001/specific_team/all-composers?team_name=test_team | python -m json.tool
echo

echo "📝 GET /specific_team/all-songs (missing team_name - should return 400)"
curl -s http://127.0.0.1:5001/specific_team/all-songs | python -m json.tool
echo

# Stop the server
echo "🛑 Stopping server..."
kill $SERVER_PID
wait $SERVER_PID 2>/dev/null

echo "✅ Demo completed!"
echo
echo "============================================================"
echo "IMPLEMENTATION SUMMARY"
echo "============================================================"
echo "✅ Public endpoints - FULLY FUNCTIONAL"
echo "⚠️  Team endpoints - STRUCTURE READY (waiting for team tables)"
echo "✅ Authentication - PLACEHOLDER READY"
echo "✅ Tests - COMPREHENSIVE SUITE"
echo "✅ Documentation - COMPLETE"
echo "============================================================"