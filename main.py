import os

web = input("enter unblock website  >")

print(os.system("wget", web))