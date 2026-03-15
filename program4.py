from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello JP ! This is Version v1.0</h1>")

server = HTTPServer(("0.0.0.0", PORT), MyHandler)

print("Server running at http://localhost:8080")
server.serve_forever()