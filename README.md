# Automated-Network-Scanner

This project is a beginner-friendly cybersecurity tool that automates
network scanning using Python and Nmap.

## Tools Used
- Python
- Nmap
- Kali Linux / Parrot OS
- Metasploitable2

## Features
- Automated port scanning
- Service and version detection
- Report generation

## Usage
python3 scanner.py

## Legal Notice
This tool is intended for educational use on authorized systems only.

## Project Flow
1. Verify target IP (Metasploitable2)
2. Confirm network connectivity
3. Execute automated Nmap scan using Python
4. Capture open ports and service versions
5. Save scan output to a report file

## Key Findings
- Multiple insecure services exposed
- Legacy protocols such as FTP and Telnet detected
- Web and database services running outdated versions
- System vulnerable to enumeration and exploitation

## Legal Disclaimer
This project is strictly for educational purposes.
All testing was conducted in a controlled lab environment
(Metasploitable2). Unauthorized scanning of systems is illegal.

## Risk Overview
| Service | Port | Risk |
|------|----|----|
| FTP | 21 | High |
| Telnet | 23 | High |
| HTTP | 80 | Medium |
| MySQL | 3306 | High |
