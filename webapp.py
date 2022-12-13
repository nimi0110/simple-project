import SimpleHTTPServer
import SocketServer

PORT = 8000
server = SockerServer.TCPServer(("", PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)
server.serve_forever()
