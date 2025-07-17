import csv
from utils.logger import parse_logs

def export_csv(date):
    logs = parse_logs(date)
    csv_path = f"honeypot_{date}.csv"
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "IP", "Location", "Path", "User-Agent"])
        for line in logs:
            parts = line.split(" - ")
            if len(parts) >= 5:
                timestamp = parts[0]
                ip = parts[1].replace("IP: ", "")
                location = parts[2].replace("Location: ", "")
                path = parts[3].replace("Path: ", "")
                ua = parts[4].replace("UA: ", "")
                writer.writerow([timestamp, ip, location, path, ua])
    return csv_path
