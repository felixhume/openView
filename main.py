import os

web = input("enter unblock website  >")
web_ = "wget", web
print(os.system(web_))