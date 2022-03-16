import os

web = input("enter unblock website  >")
web_ = "wget "+web

os.system(web_)