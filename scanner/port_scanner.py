import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.6)
        result = s.connect_ex((target, port))
        s.close()
        return port, ("OPEN" if result == 0 else "CLOSED")
    except:
        return port, "CLOSED"

def scan_many_ports(target, ports):
    results = {}

    with ThreadPoolExecutor(max_workers=60) as executor:
        for port, status in executor.map(lambda p: scan_port(target, p), ports):
            results[port] = status

    return results
