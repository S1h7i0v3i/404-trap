# 404 Trap – Low Interaction Honeypot
A low-interaction honeypot that mimics sensitive endpoints, detects malicious activity, and provides a real-time dashboard for monitoring. Designed for cybersecurity research and awareness.

# ✨ Features
✔ Fake admin panel (/admin) with credential capture

✔ Common trap endpoints (/phpmyadmin, /config, /backup, etc.)

✔ Attack detection: SQL Injection, XSS, Command Injection, Credential Harvesting

✔ GeoIP Lookup for attacker location (Country, City)

✔ Real-time dashboard with:

Attack stats (Total hits, Unique IPs, Top Paths)

Logs table with IP, Location, Attack type, Credentials

Download logs as CSV

✔ Basic Authentication for secure dashboard access

✔ Daily log rotation (honeypot_YYYY-MM-DD.log)

# 🚀 How It Works
Honeypot listens for HTTP requests on fake endpoints like /admin, /config, /phpmyadmin.

Captures:

- IP & GeoIP

- User-Agent

- Attack type (SQLi, XSS, Command Injection, etc.)

- Captured credentials

- Logs data into logs/honeypot_YYYY-MM-DD.log.

Dashboard (with Basic Auth) displays:

- Summary statistics

- Attack logs in real-time

- Option to download logs as CSV

🌐 Live Demo

🚀 Deployed on Render

🔗 Honeypot: https://https://four04-trap.onrender.com/admin

🔗 Dashboard: https://https://four04-trap.onrender.com/dashboard (Basic Auth Required)



✅ Run Locally
bash
Copy
Edit
# Clone the repository
git clone https://github.com/S1h7i0v3i/404-trap.git

cd 404-trap

# Install dependencies
pip install -r requirements.txt

# Set dashboard credentials
set DASHBOARD_USER=admin

set DASHBOARD_PASS=securepassword

# Start the honeypot
python app.py

Access:

Honeypot fake admin: http://localhost:5000/admin

Dashboard: http://localhost:5000/dashboard (Basic Auth required)

# 📈 Future Enhancements
✔ Fake SQLi responses for realism

✔ Threat Intelligence integration 

✔ Email/Slack alerts for high-risk IPs

✔ Brute-force detection and rate limiting
