import os
import requests
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_log_file(date_str):
    return os.path.join(LOG_DIR, f"honeypot_{date_str}.log")

def get_today_log_file():
    return get_log_file(datetime.now().strftime('%Y-%m-%d'))

def get_available_dates():
    return [f.split("_")[1].replace(".log", "") for f in os.listdir(LOG_DIR) if f.startswith("honeypot_")]

def parse_logs(date_str):
    logs = []
    log_file = get_log_file(date_str)
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            logs = [line.strip() for line in f]
    return logs

def get_geo(ip):
    if ip.startswith("127.") or ip.startswith("192.168.") or ip.startswith("10.") or ip.startswith("::1"):
        return "Local Network"
    try:
        res = requests.get(f"https://ipapi.co/{ip}/json/", timeout=3).json()
        city = res.get("city", "Unknown")
        country = res.get("country_name", "Unknown")
        return f"{city}, {country}"
    except:
        return "Unknown"

def log_request(path, request):
    ip = request.remote_addr
    ua = request.headers.get('User-Agent', 'N/A')
    location = get_geo(ip)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_line = f"{timestamp} - IP: {ip} - Location: {location} - Path: {path} - UA: {ua}\n"

    with open(get_today_log_file(), "a") as f:
        f.write(log_line)

    print(log_line.strip())
