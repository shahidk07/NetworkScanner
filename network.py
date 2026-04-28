import socket

'''def banner_parser(banner):
    result = {
        "protocol": "unknown",
        "service": "unknown"
    }

    if not banner:
        return result

    b = banner.lower()

    # 🔹 HTTP detection
    if "http" in b:
        result["protocol"] = "HTTP"

        if "express" in b or "node" in b:
            result["service"] = "Node.js Server"
        elif "python" in b:
            result["service"] = "Python HTTP Server"
        elif "apache" in b:
            result["service"] = "Apache"
        elif "nginx" in b:
            result["service"] = "Nginx"
        else:
            result["service"] = "HTTP Server"

    # 🔹 SSH detection
    elif "ssh" in b:
        result["protocol"] = "SSH"

        if "openssh" in b:
            result["service"] = "OpenSSH"
        else:
            result["service"] = "SSH Server"

    # 🔹 FTP detection
    elif "ftp" in b:
        result["protocol"] = "FTP"
        result["service"] = "FTP Server"

    # 🔹 MySQL detection
    elif "mysql" in b:
        result["protocol"] = "SQL"
        result["service"] = "MySQL"

    # 🔹 MongoDB (no banner usually → fallback by hint)
    elif "mongo" in b:
        result["protocol"] = "Database"
        result["service"] = "MongoDB"

    return result
'''
#function for getting a banner which includes protocol name and sometimes app name
def get_banner(ip,port):
    s=None
    try:
        s=socket.socket()
        s.settimeout(1)
        s.connect((ip,port))
        try:
            banner=s.recv(1024).decode(errors="ignore")
            if banner:
                return banner.strip()
        except:
            pass
    
        try:
            #b means text represents sequence of bytes 
            s.send(b"GET / HTTP/1.0\r\n\r\n")
            banner=s.recv(1024).decode(errors="ignore")
            return banner.strip()
        except:
            pass
        
        return "unknown"
    except:
        return "unknown"
    
    finally:
        s.close()
            
        
def scanIP():
    targetIP = input("Enter the IP address you want to scan:")
    scanRange = int(input("Enter the range of ports for scanning:"))

    count = 0
    services = {}

    for port in range(scanRange):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        try:
            s.connect((targetIP, port))
            count += 1


             #service_info=banner_parser(get_banner(targetIP, port))
            service_info=get_banner(targetIP, port)
            services[port] = service_info

        except:
            pass
        finally:
            s.close()

    print("total open ports:", count)

    for port in services:
        print(port, ":", services[port])


scanIP()