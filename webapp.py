import http.server
import socketserver

PORT = 8000
server = socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler)
server.serve_forever()
