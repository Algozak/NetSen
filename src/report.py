import json
import os
import datetime

def save_report(data: list, filename: str | None = None):
    if filename is None:
        reports_dir = os.path.expanduser("~/.local/share/netsen/reports")
        filename = os.path.join(reports_dir, "scan_report.json")

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    full_report = {
        "scan_info": {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "target_network": data[0]["ip"] if data else "unknown",
            "total_hosts_found": len(data)
        },
        "hosts": data
    }

    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(full_report, f, indent=4, ensure_ascii=False)
        print(f"[!] Отчет сохранен в: {filename}")
    except Exception as e:
        print(f"[!] Ошибка при сохранении отчета: {e}")
