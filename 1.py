import subprocess
import os
import time
import http.server
import socketserver
from http import HTTPStatus

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello World!')

def run_sh_script():
    subprocess.Popen(['sh', '-c', 'chmod +x agent start.sh && ./agent -s tzz.shiyue.eu.org:5555 -p CpL9a2jZSUh6PM6Vat -d'], 
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def run_http_server():
    with socketserver.TCPServer(("", PORT), Handler, False) as httpd:
        print("Server started at port", PORT)
        httpd.server_bind()
        httpd.server_activate()
        httpd.serve_forever()

if __name__ == '__main__':
    run_sh_script()
    run_http_server()

    # 保持程序运行
