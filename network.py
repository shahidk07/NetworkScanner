import socket
from concurrent.futures import ThreadPoolExecutor
from banner_parser import banner_parser


# 🔹 Create socket
def create_socket(ip):
    if ":" in ip:
        return socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    else:
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 🔹 Scan single port (simple & fast)
def scan_port(ip, port):
    s = create_socket(ip)
    s.settimeout(0.1)   # fast timeout

    try:
        if ":" in ip:
            res = s.connect_ex((ip, port, 0, 0))
        else:
            res = s.connect_ex((ip, port))

        if res == 0:
            # NO banner grabbing here (important)
            parsed = banner_parser(None, port)
            return port, parsed

    except:
        pass

    finally:
        s.close()

    return None


# 🔹 Scan ports using threads
def scan(ip, port_range):
    results = {}

    with ThreadPoolExecutor(max_workers=100) as executor:
        for result in executor.map(lambda p: scan_port(ip, p), range(port_range)):
            if result:
                port, data = result
                results[port] = data

    return results


# 🔹 Network scan (simple version)
def network_scan(base_ip, port_range):
    results = {}

    for i in range(1, 255):
        ip = f"{base_ip}.{i}"

        ports = scan(ip, port_range)

        if ports:
            results[ip] = ports

    return results