from flask import Flask, request, jsonify, session
import uuid

app = Flask(__name__)
app.secret_key = 'super_secret_unsecure_key'

# Mock user database
USERS_DB = {"admin": "password123"}

@app.before_request
def establish_initial_session():
    # Vulnerability: Allocating a fixed session token before authentication
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())

@app.route('/login', methods=['POST'])
def vulnerable_login():
    data = request.json or {}
    username = data.get('username')
    password = data.get('password')
    
    # Check credentials
    if username in USERS_DB and USERS_DB[username] == password:
        # Vulnerability: The session_id is NOT regenerated upon privilege change.
        # Vulnerability: There is no track of failed attempts (susceptible to brute force).
        session['authenticated'] = True
        session['username'] = username
        return jsonify({"message": "Login successful", "session_id": session['session_id']}), 200
        
    return jsonify({"error": "Invalid credentials"}), 401
