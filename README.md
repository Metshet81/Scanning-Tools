# 🛠️ Network Scanning Tools Collection  

This repository contains a collection of network scanning and discovery tools developed for learning, practice, and demonstration purposes.  
Each tool focuses on a different aspect of network reconnaissance.  

---

# Host Discovery
Host discovery is the first step in mapping a network’s attack surface. It reveals which machines are alive, reachable, and responding, helping security analysts understand the real structure behind an environment. By combining techniques like ICMP probing, ARP scanning, and port-based detection, host discovery transforms an unknown network into a clear, actionable map — making every later phase of enumeration faster, smarter, and more accurate.

---
# nmap

This project delivers the power of Nmap through a clean, Python-based interface. By automating scanning tasks with Python, it transforms complex Nmap operations into simple, reusable functions — making host discovery, port scanning, and service enumeration faster and more efficient. Perfect for learning, scripting, and building larger security tools on top of Nmap’s capabilities.

---
# Bash Based nmap

This project brings the power of Nmap into a simple, Bash-based automation tool. It streamlines network scanning by wrapping essential Nmap commands into an easy workflow, allowing users to perform fast host discovery, port scanning, and service enumeration with a single script. Designed for learning, speed, and convenience, this tool helps beginners and professionals run reliable scans without memorizing long command strings.

---
# Port Scanner

A port scanner is a lightweight, fast tool designed to reveal which doors are open on a networked system. By probing ports and identifying their state, it helps uncover active services, potential attack vectors, and the overall security posture of a machine. Simple but powerful, a port scanner is the foundation of every penetration test — turning raw network data into clear, actionable insights.

---


# 🔧 **Usage Guide (From Cloning to Scanning)**

Follow these steps to use all scanning tools included in this repository.

---

## 📥 **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/Scanning-Tools.git
cd Scanning-Tools
```

---

## 🧹 **2. Ensure Files Have No Spaces (Optional Cleanup)**

If files had spaces before, rename them (example):

```bash
mv "host discovery.py" host_discovery.py
mv "port scanner.py" port_scanner.py
```

---

## 🛠️ **3. Install Python Requirements (If Any)**

```bash
pip install -r requirements.txt
```

*(Skip if your project doesn’t need extra libraries.)*

---

# 🚀 **4. Run Each Scanning Tool**

---

## 🟢 **Host Discovery Tool (Python)**

Used to identify alive hosts on a network.

### **Command**

```bash
python3 host_discovery.py <target-range>
```

### **Example**

```bash
python3 host_discovery.py 192.168.1.0/24
```

---

## 🔵 ** Port Scanner (Python)**

Scans a target for open ports within a given range.

### **Command**

```bash
python3 port_scanner.py <target-ip> <start-port> <end-port>
```

### **Example**

```bash
python3 port_scanner.py 10.49.181.21 1 1024
```

---

## 🟣 **C. Nmap Automation Tool (Python-Based)**

Wrapper for automated Nmap scans via Python.

### **Command**

```bash
python3 nmap_tool.py <target-ip> <scan-type>
```

### **Examples**

Service version scan:

```bash
python3 nmap_tool.py 10.49.181.21 sV
```

OS detection:

```bash
python3 nmap_tool.py 10.49.181.21 O
```

Aggressive scan:

```bash
python3 nmap_tool.py 10.49.181.21 A
```

---

## 🟠 **Nmap Automation Script (Bash)**

Execute Nmap scans through a Bash script.

### **Give Execute Permission**

```bash
chmod +x nmap.bash
```

### **Run the Script**

```bash
bash nmap.bash <target-ip>
```

### **Example**

```bash
bash nmap.bash 10.49.181.21
```

