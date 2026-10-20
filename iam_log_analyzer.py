import csv

# 1. The file we want to analyze
log_file = "signin_logs.csv"

print("[*] Starting Entra ID Sign-in Log Analysis...")
print("-" * 50)

suspicious_count = 0

# 2. Open the CSV file and read it
with open(log_file, mode='r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        user = row['User']
        ip = row['IP_Address']
        location = row['Location']
        status = row['Status']
        risk = row['Risk_Level']
        
        # 3. The Logic: Flag bad logins
        if status == "Failure":
            print(f"[!] ALERT: Failed login for {user} from {location} (IP: {ip})")
            suspicious_count += 1
            
        elif risk in ["High", "Medium"]:
            print(f"[!] ALERT: {risk} risk login for {user} from {location}")
            suspicious_count += 1

print("-" * 50)
print(f"[+] Analysis complete. Found {suspicious_count} suspicious events.")
