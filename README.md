# 🛠️ Network Scanning Tools Collection  

This repository contains a collection of network scanning and discovery tools developed for learning, practice, and demonstration purposes.  
Each tool focuses on a different aspect of network reconnaissance.  

---

## ✅ Tools Included  

### 1️⃣ Port Scanner (Without Nmap)  
A Python-based custom port scanner that uses raw sockets to check open ports on a given host.  
🔹 **Key Feature:** Simple TCP connection scanning without relying on external tools.  

**Usage:**  
```bash
python3 port_scanner.py --ip 192.168.1.1 --ports 1-100

python3 nmap_port_scanner.py --ip 192.168.1.1 --ports 1-100

python3 host_discovery.py --ip-range 192.168.1.0/24

bash nmap_scan.sh 192.168.1.1 default-scripts
