import os
import http.server
import socketserver
import re

print("openView is open-source! get it at github.com/felixhume/openView")
PORT = 8080
web = input("enter unblock website  >")
web_ = "wget "+web

os.system(web_)

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    httpd.serve_forever()
    with open("index.html") as file:
        for line in file:
            urls_hs = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            print(urls_hs)
            for url in urls_hs:
                os.system("wget "+url)