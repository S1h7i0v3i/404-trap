import os
import csv
from .logger import parse_logs

EXPORT_DIR = "logs"

def export_logs_as_csv(date):
    logs = parse_logs(date)
    file_path = os.path.join(EXPORT_DIR, f"export_{date}.csv")
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "IP", "Attack", "Path", "Credentials", "User-Agent"])
        for line in logs:
            parts = line.split(" - ")
            creds = ""
            if "Captured Credentials:" in line:
                creds = [p for p in parts if "Captured Credentials:" in p][0].replace("Captured Credentials: ", "")
            writer.writerow([parts[0], parts[1], parts[2], parts[3], creds, parts[-1]])
    return file_path
