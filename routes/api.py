from flask import Blueprint, request, jsonify, send_file
from utils.logger import parse_logs, get_available_dates
from utils.stats import calculate_stats
from utils.exporter import export_csv
from datetime import datetime

api_bp = Blueprint("api", __name__)

@api_bp.route("/logs")
def get_logs():
    date = request.args.get("date", datetime.now().strftime('%Y-%m-%d'))
    logs = parse_logs(date)
    logs.sort(key=lambda x: x.split(" - ")[0], reverse=True)
    return jsonify(logs)

@api_bp.route("/dates")
def get_dates():
    return jsonify(sorted(get_available_dates(), reverse=True))

@api_bp.route("/stats")
def get_stats():
    date = request.args.get("date", datetime.now().strftime('%Y-%m-%d'))
    logs = parse_logs(date)
    return jsonify(calculate_stats(logs))

@api_bp.route("/export-logs")
def export_logs():
    date = request.args.get("date", datetime.now().strftime('%Y-%m-%d'))
    csv_path = export_csv(date)
    return send_file(csv_path, as_attachment=True)
