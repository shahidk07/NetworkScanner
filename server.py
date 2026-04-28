from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json
import os

from network import scan

class Handler(SimpleHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)

        # 🔥 API endpoint
        if parsed.path == "/scan":
            params = parse_qs(parsed.query)

            ip = params.get("ip", [""])[0]
            port_range = int(params.get("range", [100])[0])

            result = scan(ip, port_range)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(result).encode())

        else:
            # Serve frontend files
            if self.path == "/":
                self.path = "/frontend/index.html"
            else:
                self.path = "/frontend" + self.path

            return super().do_GET()


# Run server
PORT = 8000
server = HTTPServer(("localhost", PORT), Handler)

print(f"Server running at http://localhost:{PORT}")
server.serve_forever()