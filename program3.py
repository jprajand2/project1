from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8080

Handler = SimpleHTTPRequestHandler

with TCPServer(("", PORT), Handler) as httpd:
    print("THIS IS THE LINE YOU WILL SEE IN BROWSER", PORT)
    httpd.serve_forever()