import http.server
import socketserver
import os
import subprocess
from urllib.parse import urlparse, parse_qs

ipaddr = '10.9.3.102'  # Change to the actual IP address of your server
port = 4201          # Change to the desired port

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            parsed = urlparse(self.path)
            if parsed.path == '/commander/run':
                command = parse_qs(parsed.query)['command'][0]
                result = self.run_command(command)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(result.encode())
            else:
                self.send_error(404, 'Not Found')

        except Exception as e:
            print(f"Error: {e}")
            self.send_error(500, 'Internal Server Error')

    def run_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            return output
        except subprocess.CalledProcessError as e:
            return f"Error: {e.output}"

if __name__ == '__main__':
    handler = MyHandler
    with socketserver.TCPServer((ipaddr, port), handler) as httpd:
        print(f"Server started at http://{ipaddr}:{port}")
        httpd.serve_forever()
