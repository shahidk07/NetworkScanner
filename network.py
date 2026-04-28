import socket
        

# network_scan()    → scans ports on those devices
def network_scan(base_ip, port_range):
    results = {}

    for i in range(1, 255):
        ip = f"{base_ip}.{i}"

        ports = scan(ip, port_range)

        if ports:  # host exists
            results[ip] = ports

    return results


#function to create ipv6 and ipv4 addresses
def create_socket(ip):
    if ":" in ip:  # IPv6 detection
        return socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    else:
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
def get_banner(ip, port):
    s = None
    try:
        s = create_socket(ip)
        s.settimeout(1)

        if ":" in ip:
            res = s.connect_ex((ip, port, 0, 0))
        else:
            res = s.connect_ex((ip, port))

        # ❗ IMPORTANT: check connection success
        if res != 0:
            return None

        # Try immediate banner
        try:
            banner = s.recv(1024).decode(errors="ignore")
            if banner:
                return banner.strip()
        except:
            pass

        # Try HTTP request
        try:
            s.send(b"GET / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024).decode(errors="ignore")
            if banner:
                return banner.strip()
        except:
            pass

        return None

    except:
        return None

    finally:
        if s:
            s.close()



#function to scan the ports
def scan(ip, port_range):
    results = {}

    for port in range(port_range):
        s = create_socket(ip)
        s.settimeout(0.3)

        try:
            if s.connect_ex((ip, port)) == 0:
                banner = get_banner(ip, port)
                
                from banner_parser import banner_parser
                parsed = banner_parser(banner, port)
                results[port] = parsed
        except:
            pass
        finally:
            s.close()

    return results