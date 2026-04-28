import socket


#function to create ipv6 and ipv4 addresses
def create_socket(ip):
    if ":" in ip:  # IPv6 detection
        return socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    else:
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    #function to receive banner from ports
def get_banner(ip, port):
    s = None
    try:
        s = create_socket(ip)

        if ":" in ip:
            s.connect((ip, port, 0, 0))
        else:
            s.connect((ip, port))
        s.settimeout(1)
        if ":" in ip:
            s.connect((ip, port, 0, 0))  # IPv6
        else:
            s.connect((ip, port))        # IPv4

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