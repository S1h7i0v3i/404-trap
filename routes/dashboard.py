from flask import Blueprint, render_template, request, jsonify, send_file
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash
import os
from utils.logger import parse_logs, get_available_dates
from utils.stats import calculate_stats
from utils.exporter import export_logs_as_csv

dashboard_bp = Blueprint("dashboard", __name__)
auth = HTTPBasicAuth()

# Secure credentials - required
DASHBOARD_USER = os.getenv("DASHBOARD_USER")
DASHBOARD_PASS = os.getenv("DASHBOARD_PASS")

if not DASHBOARD_USER or not DASHBOARD_PASS:
    raise RuntimeError("ERROR: DASHBOARD_USER and DASHBOARD_PASS must be set as environment variables!")

PASS_HASH = generate_password_hash(DASHBOARD_PASS)

@auth.verify_password
def verify(username, password):
    if username == DASHBOARD_USER and check_password_hash(PASS_HASH, password):
        return username
    return None

@dashboard_bp.route("/dashboard")
@auth.login_required
def dashboard():
    return render_template("dashboard.html")

@dashboard_bp.route("/api/logs")
@auth.login_required
def get_logs():
    date = request.args.get("date")
    logs = parse_logs(date)
    return jsonify(logs[::-1])

@dashboard_bp.route("/api/dates")
@auth.login_required
def get_dates():
    return jsonify(get_available_dates())

@dashboard_bp.route("/api/stats")
@auth.login_required
def get_stats():
    date = request.args.get("date")
    logs = parse_logs(date)
    stats = calculate_stats(logs)
    return jsonify(stats)

@dashboard_bp.route("/api/export-logs")
@auth.login_required
def export_logs():
    date = request.args.get("date")
    file_path = export_logs_as_csv(date)
    return send_file(file_path, as_attachment=True)
