from flask import Flask, request, Response
import os
from routes.dashboard import dashboard_bp
from routes.api import api_bp
from routes.traps import traps_bp

app = Flask(__name__, template_folder="templates", static_folder="static")

# ✅ Load credentials from environment variables
USERNAME = os.getenv("DASHBOARD_USER", "admin")
PASSWORD = os.getenv("DASHBOARD_PASS", "securepass")

# ✅ Basic Auth Check
def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

def authenticate():
    return Response('Authentication required', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

def require_auth():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    return None

# ✅ Apply auth only to dashboard and API routes
@app.before_request
def restrict_dashboard():
    if request.path.startswith("/dashboard") or request.path.startswith("/api"):
        return require_auth()

# ✅ Register Blueprints
app.register_blueprint(dashboard_bp)
app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(traps_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
