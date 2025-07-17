from flask import Flask
from routes.traps import traps_bp
from routes.dashboard import dashboard_bp
from dotenv import load_dotenv
import os

# Load .env if exists
load_dotenv()

app = Flask(__name__, template_folder="templates", static_folder="static")
@app.route("/")
def home():
    return "<h2>Welcome to my Server </h2>"

# Register routes
app.register_blueprint(traps_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    print("Loaded DASHBOARD_USER:", os.getenv("DASHBOARD_USER"))
    app.run(host="0.0.0.0", port=port, debug=True)
