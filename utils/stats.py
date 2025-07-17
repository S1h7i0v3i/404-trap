from collections import Counter

def calculate_stats(logs):
    if not logs:
        return {"total_hits": 0, "unique_ips": 0, "top_path": None, "top_ips": []}

    ips = []
    paths = []
    for log in logs:
        parts = log.split(" - ")
        if len(parts) >= 5:
            ip = parts[1].replace("IP: ", "")
            path = parts[3].replace("Path: ", "")
            ips.append(ip)
            paths.append(path)

    top_path = Counter(paths).most_common(1)[0][0] if paths else None
    top_ips = Counter(ips).most_common(5)

    return {
        "total_hits": len(logs),
        "unique_ips": len(set(ips)),
        "top_path": top_path,
        "top_ips": top_ips
    }
