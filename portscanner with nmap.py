import nmap

# Create nmap object
nm = nmap.PortScanner()

# Input target IP or hostname
target = input("Enter target IP or Hostname: ")

# Scan target for ports 1-1000
print(f"\nScanning {target} for ports 1-1000...\n")

nm.scan(hosts=target, arguments='-p 1-1000')

# Loop through discovered hosts
for host in nm.all_hosts():
    print(f"Host: {host} ({nm[host].hostname()})")
    print(f"State: {nm[host].state()}")

    # Loop through protocols (usually 'tcp')
    for proto in nm[host].all_protocols():
        print(f"\nProtocol: {proto}")

        # Get list of open ports
        ports = nm[host][proto].keys()
        for port in sorted(ports):
            print(f"Port {port}: {nm[host][proto][port]['state']}")

print("\nScan Completed.")
