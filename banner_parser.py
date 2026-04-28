def banner_parser(banner, port):
    result = {
        "protocol": "unknown",
        "service": "unknown"
    }

    if not banner:
        banner = ""

    b = banner.lower()

    # 🌐 HTTP
    if "http" in b:
        result["protocol"] = "HTTP"

        if "express" in b or "x-powered-by" in b:
            result["service"] = "Node.js Server"
        elif "python" in b:
            result["service"] = "Python HTTP Server"
        elif "apache" in b:
            result["service"] = "Apache"
        elif "nginx" in b:
            result["service"] = "Nginx"
        elif "iis" in b:
            result["service"] = "Microsoft IIS"
        else:
            result["service"] = "Generic HTTP Server"

    # 🔐 SSH
    elif "ssh" in b:
        result["protocol"] = "SSH"
        if "openssh" in b:
            result["service"] = "OpenSSH"
        else:
            result["service"] = "SSH Server"

    # 📁 FTP
    elif "ftp" in b:
        result["protocol"] = "FTP"
        result["service"] = "FTP Server"

    # 📧 SMTP (mail)
    elif "smtp" in b:
        result["protocol"] = "SMTP"
        result["service"] = "Mail Server"

    # 🗄️ MySQL (rare banner)
    elif "mysql" in b:
        result["protocol"] = "SQL"
        result["service"] = "MySQL"

    # 🗄️ PostgreSQL
    elif "postgres" in b:
        result["protocol"] = "SQL"
        result["service"] = "PostgreSQL"

    # 🧠 Redis
    elif "redis" in b:
        result["protocol"] = "Database"
        result["service"] = "Redis"

    # 🧠 MongoDB (rare)
    elif "mongo" in b:
        result["protocol"] = "Database"
        result["service"] = "MongoDB"

    # 🔥 Fallback using port (IMPORTANT)
    if result["protocol"] == "unknown":
        if port == 80 or port == 8080 or port == 3000:
            result = {"protocol": "HTTP", "service": "Generic HTTP Server"}
        elif port == 22:
            result = {"protocol": "SSH", "service": "SSH Server"}
        elif port == 21:
            result = {"protocol": "FTP", "service": "FTP Server"}
        elif port == 3306:
            result = {"protocol": "SQL", "service": "MySQL"}
        elif port == 5432:
            result = {"protocol": "SQL", "service": "PostgreSQL"}
        elif port == 6379:
            result = {"protocol": "Database", "service": "Redis"}
        elif port == 27017:
            result = {"protocol": "Database", "service": "MongoDB"}

    return result