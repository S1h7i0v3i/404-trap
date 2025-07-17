from flask import Blueprint, request
from utils.logger import log_request

traps_bp = Blueprint("traps", __name__)

TRAP_PATHS = ["/admin", "/config", "/.git", "/phpmyadmin", "/env", "/wp-login.php", "/backup"]

@traps_bp.route("/")
def home():
    return "Welcome to our site."

for route in TRAP_PATHS:
    def handler(route=route):
        log_request(route, request)
        return "This page has moved.", 200

    endpoint_name = route.replace("/", "_").replace(".", "_")
    traps_bp.add_url_rule(route, endpoint=endpoint_name, view_func=handler)

@traps_bp.app_errorhandler(404)
def all_others(e):
    if request.path == "/favicon.ico":
        return "", 204
    log_request(request.path, request)
    return "Nothing to see here.", 200
