#!/bin/python3

import socket

target = input("Enter IP or hostname: ")

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning {target}...\n")

for port in range(start_port, end_port + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")

        s.close()

    except KeyboardInterrupt:
        print("\nScan stopped by user")
        break

    except socket.gaierror:
        print("\nHostname could not be resolved")
        break

    except socket.error:
        print("\nCould not connect to server")
        break