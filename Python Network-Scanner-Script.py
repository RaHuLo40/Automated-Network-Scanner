import subprocess

target_ip = input("Enter target IP: ")
output_file = "scan_results.txt"

print("[+] Scanning target:", target_ip)

command = ["nmap", "-sV", "-Pn", target_ip]

result = subprocess.run(command, capture_output=True, text=True)

with open(output_file, "w") as file:
    file.write(result.stdout)

print("[+] Scan completed")
print("[+] Results saved to scan_results.txt")
