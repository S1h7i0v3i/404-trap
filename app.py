from flask import Flask
from routes.traps import traps_bp
from routes.dashboard import dashboard_bp
from dotenv import load_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix
import os

# Load .env if exists (for local development)
load_dotenv()

app = Flask(__name__, template_folder="templates", static_folder="static")

# Fix for Render / Gunicorn reverse proxy
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1)

# Home Route
@app.route("/")
def home():
    return "<h2>Welcome to 404 Trap Honeypot!</h2>"

# Register Blueprints
app.register_blueprint(traps_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
