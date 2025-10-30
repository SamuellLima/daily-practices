import os
from datetime import datetime

def analyze_access_logs(logs):
    failed_attemps = {}
    
    for log in logs:
        if log["success"] is False:
            ip = log["ip"]
            if ip not in failed_attemps:
                failed_attemps[ip] = 0
            failed_attemps[ip] +=1

            if failed_attemps.get(ip) >= 3:
                print(f"I SEE YOUUUU {ip} \n\ \n\
                            ░░░░░░███████ ]▄▄▄▄▄▄▄▄▃\n\
                            ▂▄▅█████████▅▄▃▂\n\
                            I███████████████████].\n\
                            <<===||==||==||==||==>>")
                

                path = os.path.abspath(__file__).replace("solution.py", "suspicious_ips.log")
                timestamp = datetime.today().isoformat() + "Z"
                with open(path, "a") as f:
                    f.write(f"{timestamp} Suspicious IP detected: {ip}\n")
                
                break
                
logs = [
        {"user": "admin", "ip": "192.168.0.10", "success": True},
        {"user": "samuel", "ip": "10.0.0.2", "success": True},
        {"user": "admin", "ip": "177.92.13.55", "success": False},
        {"user": "root", "ip": "177.92.13.55", "success": False},
        {"user": "admin", "ip": "177.92.13.55", "success": False},
        {"user": "root", "ip": "177.92.13.55", "success": False},
    ]

analyze_access_logs(logs)
