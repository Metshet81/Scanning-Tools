import socket
target = input("Enter target IP or Hostname: ")
ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]

print(f"\nScanning target: {target}")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Timeout after 1 second
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    sock.close()

print("\nScan Completed.")
