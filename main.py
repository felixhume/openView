import os
import http.server
import socketserver
import re

PORT = 8080
web = input("enter unblock website  >")
web_ = "wget -output-document="+web+" "+web

os.system(web_)
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except Exception as issue:
        print(issue)
        exit()
