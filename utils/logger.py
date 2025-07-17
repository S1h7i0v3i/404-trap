import os
import re
import requests
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_today_log_file():
    date_str = datetime.now().strftime('%Y-%m-%d')
    return os.path.join(LOG_DIR, f"honeypot_{date_str}.log")

def get_geo_location(ip):
    # Skip local/private IPs
    if ip.startswith("127.") or ip.startswith("192.") or ip.startswith("10."):
        return "Local Network"
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}?fields=country,city", timeout=3)
        if res.status_code == 200:
            data = res.json()
            return f"{data.get('country', 'Unknown')}, {data.get('city', 'Unknown')}"
    except:
        pass
    return "Unknown"

def detect_attack_type(path, ua, username="", password=""):
    sql_patterns = [r"(select|union|insert|drop|update|delete)", r"(--|;|')"]
    xss_patterns = [r"<script.*?>", r"onerror=", r"javascript:"]
    cmd_patterns = [r"(;|\|\||&&).*"]

    for pattern in sql_patterns:
        if re.search(pattern, path, re.IGNORECASE) or re.search(pattern, username, re.IGNORECASE) or re.search(pattern, password, re.IGNORECASE):
            return "SQL Injection"

    for pattern in xss_patterns:
        if re.search(pattern, path, re.IGNORECASE) or re.search(pattern, username, re.IGNORECASE):
            return "XSS"

    for pattern in cmd_patterns:
        if re.search(pattern, path, re.IGNORECASE) or re.search(pattern, password, re.IGNORECASE):
            return "Command Injection"

    if "sqlmap" in ua.lower():
        return "SQLi Tool"

    if path == "/admin" and (username or password):
        return "Credential Harvesting Attempt"

    return "Normal"

def log_request(path, request, credentials=None):
    ip = request.remote_addr
    ua = request.headers.get('User-Agent', 'N/A')
    username, password = credentials if credentials else ("", "")
    attack_type = detect_attack_type(path, ua, username, password)
    location = get_geo_location(ip)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    creds_info = ""
    if credentials:
        creds_info = f" - Captured Credentials: {username}/{password}"

    log_line = f"{timestamp} - IP: {ip} - Location: {location} - Attack: {attack_type} - Path: {path}{creds_info} - UA: {ua}\n"

    with open(get_today_log_file(), "a") as f:
        f.write(log_line)

def parse_logs(date):
    log_file = os.path.join(LOG_DIR, f"honeypot_{date}.log")
    if not os.path.exists(log_file):
        return []
    with open(log_file, "r") as f:
        return [line.strip() for line in f.readlines()]

def get_available_dates():
    files = [f for f in os.listdir(LOG_DIR) if f.startswith("honeypot_")]
    return sorted([f.replace("honeypot_", "").replace(".log", "") for f in files], reverse=True)
