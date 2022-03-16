import os
import http.server
import socketserver
PORT = 8080
web = input("enter unblock website  >")
web_ = "wget "+web

os.system(web_)
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    httpd.serve_forever()