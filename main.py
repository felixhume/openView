import os
import http.server
import socketserver
import re

print("""
                         __    _                                   
                    _wr""        "-q__                             
                 _dP                 9m_     
               _#P                     9#_                         
              d#@                       9#m                        
             d##                         ###                       
            J###                         ###L                      
            {###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\g          ""M##m            
 J#@"             0L  "*##     ##@"  J#              *#K           
 #"               `#    "_gmwgm_~    dF               `#_          
7F                 "#_   ]#####F   _dK                 JE          
]                    *m__ ##### __g@"                   F          
                       "PJ#####LP"                                 
 `                       0######_                      '           
                       _0########_                                   
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""                    




                          ____   ____.__               
  ____ ______   ____   ___\   \ /   /|__| ______  _  __
 /  _ \\____ \_/ __ \ /    \   Y   / |  |/ __ \ \/ \/ /
(  <_> )  |_> >  ___/|   |  \     /  |  \  ___/\     / 
 \____/|   __/ \___  >___|  /\___/   |__|\___  >\/\_/  
       |__|        \/     \/                 \/        

(openView is open-source! get it at github.com/felixhume/openView)
(thanks for using!)

""")
PORT = 8080
web = input("enter unblock website  >")
web_ = "wget -output-document="+web+" "+web

os.system(web_)

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    httpd.serve_forever()
    with open(web+"\index.html") as file:
        for line in file:
            urls_hs = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            print(urls_hs)
            for url in urls_hs:
                os.system("wget web+"/"+url")