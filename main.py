import os
import http.server
import socketserver
import re

print("openView is open-source! get it at github.com/felixhume/openView")
PORT = 8080
web = input("enter unblock website  >")
web_ = "wget "+web
urltype = 0
#0: unknown
#1: https://
#2: /css/general.css
os.system(web_)

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    httpd.serve_forever()
    with open("index.html") as file:
        for line in file:
            urls_https = re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", line)
            print(urls_https)
            for url in urls_https:
                if url[:8] == "https://":
                    urltype = 1
                elif url[1] == "/":
                    urltype = 2
                else:
                    urltype = 0
                print(urltype, "type")
                #download the extra files
                if urltype == 2:#need to create folders
                    os.system("wget "+url)
                elif urltype == 1:
                    os.system("wget "+url)
                os.system("wget "+url)


