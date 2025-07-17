import re
from flask import Blueprint, request, render_template
from utils.logger import log_request

traps_bp = Blueprint("traps", __name__)

@traps_bp.route("/admin", methods=["GET", "POST"])
def fake_admin():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        # Log attempt for dashboard
        log_request("/admin", request, credentials=(username, password))

        # Fake validation for attacker
        if not re.match(r"^[a-zA-Z0-9_]{3,20}$", username):
            return render_template("admin.html", error="Invalid username format.")
        else:
            return render_template("admin.html", error="Incorrect password.")

    return render_template("admin.html")
