import http.server
import socketserver
from http import HTTPStatus  
import subprocess
import os
import stat

# Get port from environment variable
PORT = int(os.environ.get('PORT', 8080))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello World!')

if __name__ == '__main__':
    # Add executable permissions
    agent_path = "./agent"
    os.chmod(agent_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR |
             stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP |
             stat.S_IROTH | stat.S_IXOTH)

    # Start nezha-agent in background
    nezha_command = [
        agent_path,
        "-s", "tzz.shiyue.eu.org:5555",
        "-p", "gBaiYkxWSPRgA1QIhA",
        "-d"
    ]
    subprocess.Popen(nezha_command)

    # Start HTTP server
    with socketserver.TCPServer(("", PORT), Handler, False) as httpd:
        print("Server started at port", PORT)
        httpd.allow_reuse_address = True
        httpd.server_bind()
        httpd.server_activate()
        httpd.serve_forever()
