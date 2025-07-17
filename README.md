# 404 Trap - Modular Honeypot & Security Dashboard

404 Trap is a **lightweight Flask-based honeypot** designed to detect reconnaissance attempts (e.g., `/admin`, `/phpmyadmin`) and log suspicious activity. It includes an interactive **web dashboard** for analytics and log management.

---

## ✨ Features
- **Fake endpoints** to catch reconnaissance bots
- **Daily log rotation**
- **Interactive dashboard**:
  - Date filter for logs
  - Summary cards (Total Hits, Unique IPs, Top Path)
  - CSV Export for compliance/reporting
  - Chart.js visualization for top attacker IPs
  - Dark Mode toggle
- **Modular code structure** (Blueprints & Utils)
- **Ready for Render deployment**

---

## 📂 Project Structure
404-trap/
├── app.py
├── routes/
│ ├── dashboard.py
│ ├── api.py
│ └── traps.py
├── utils/
│ ├── logger.py
│ ├── stats.py
│ └── exporter.py
├── templates/
│ └── dashboard.html
├── static/
│ ├── css/style.css
│ └── js/dashboard.js
├── logs/
├── requirements.txt
├── Procfile
└── README.md