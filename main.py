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
    httpd.serve_forever()
    with open(web+"\index.html") as file:
        for line in file:
            urls = re.findall('href=', line)
            print(urls)
            for url in urls:
                os.system("wget -output-document="+web+"/"+url)