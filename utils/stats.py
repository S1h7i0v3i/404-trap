def calculate_stats(logs):
    total_hits = len(logs)
    ips, paths, attacks = [], [], {}

    for line in logs:
        parts = line.split(" - ")
        if len(parts) < 6:
            continue
        ip = parts[1].replace("IP: ", "")
        attack = parts[2].replace("Attack: ", "")
        path = parts[3].replace("Path: ", "")
        ips.append(ip)
        paths.append(path)
        attacks[attack] = attacks.get(attack, 0) + 1

    unique_ips = len(set(ips))
    top_path = max(set(paths), key=paths.count) if paths else None

    ip_freq = {}
    for ip in ips:
        ip_freq[ip] = ip_freq.get(ip, 0) + 1
    top_ips = sorted(ip_freq.items(), key=lambda x: x[1], reverse=True)[:5]

    return {
        "total_hits": total_hits,
        "unique_ips": unique_ips,
        "top_path": top_path,
        "top_ips": top_ips,
        "attack_summary": attacks
    }
