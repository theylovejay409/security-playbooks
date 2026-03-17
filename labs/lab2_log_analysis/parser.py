import json
from pathlib import Path

LOG_FILES = [
    Path("../../examples/malware_log_example.txt"),
    Path("../../examples/powershell_log_example.txt"),
    Path("../../examples/phishing_log_example.txt"),
]

def parse_log_line(line: str) -> dict | None:
    line = line.strip()
    if not line:
        return None
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        return None

def process_log_file(log_file: Path) -> None:
    if not log_file.exists():
        print(f"[!] Log file not found: {log_file}")
        return

    print(f"\n[+] Parsing log file: {log_file}")
    suspicious = []

    with log_file.open("r", encoding="utf-8") as f:
        for line in f:
            entry = parse_log_line(line)
            if not entry:
                continue

            if entry.get("severity") == "high":
                suspicious.append(entry)

    print(f"[+] Found {len(suspicious)} suspicious entries")
    for s in suspicious:
        print(f"- {s.get('timestamp')} | {s.get('event')} | {s.get('severity')}")

def main() -> None:
    for log_file in LOG_FILES:
        process_log_file(log_file)

if __name__ == "__main__":
    main()
