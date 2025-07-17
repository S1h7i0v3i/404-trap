from flask import Flask
from routes.dashboard import dashboard_bp
from routes.api import api_bp
from routes.traps import traps_bp

app = Flask(__name__, template_folder="templates", static_folder="static")

# Register Blueprints
app.register_blueprint(dashboard_bp)
app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(traps_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
