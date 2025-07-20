import ipaddress
import subprocess
import socket
import re

# Function to get default gateway using "ip route"
def get_gateway():
    result = subprocess.getoutput("ip route | grep default")
    gateway = result.split()[2]
    return gateway

# Function to ping a range of IPs (Host Discovery)
def discover_hosts(subnet):
    print(f"\nScanning subnet: {subnet} for active hosts...")
    for ip in ipaddress.IPv4Network(subnet, strict=False):
        try:
            result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)],
                                    stdout=subprocess.DEVNULL)
            if result.returncode == 0:
                print(f"Host {ip} is UP")
        except Exception as e:
            print(f"Error pinging {ip}: {e}")

# Function to determine IP class based on first octet
def ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    else:
        return "Class E (Experimental)"

# Main program
gateway_ip = get_gateway()
print(f"Default Gateway: {gateway_ip}")
print(f"Gateway IP Class: {ip_class(gateway_ip)}")

# You can change this subnet based on your network
subnet = gateway_ip + "/24"
discover_hosts(subnet)
