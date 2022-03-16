import os
import http.server
import socketserver
PORT = 8080
web = input("enter unblock website  >")
web_ = "wget "+web

os.system(web_)
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()