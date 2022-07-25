#dcb5c90f5eb940e4801725021e0038f74c209964
import bitly_api
import requests
import tkinter as tk
#my token number
banner= """
(made Harun)
██████╗ ██╗████████╗██╗  ██╗   ██╗                        
██╔══██╗██║╚══██╔══╝██║  ╚██╗ ██╔╝                        
██████╔╝██║   ██║   ██║   ╚████╔╝                         
██╔══██╗██║   ██║   ██║    ╚██╔╝                          
██████╔╝██║   ██║   ███████╗██║                           
╚═════╝ ╚═╝   ╚═╝   ╚══════╝╚═╝                           
███████╗██╗  ██╗ ██████╗ ██████╗ ████████╗███████╗██████╗ 
██╔════╝██║  ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
███████╗███████║██║   ██║██████╔╝   ██║   █████╗  ██████╔╝
╚════██║██╔══██║██║   ██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
███████║██║  ██║╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
"""
print(banner)
print("\n")
Access_Token = "dcb5c90f5eb940e4801725021e0038f74c209964"

connection = bitly_api.Connection(access_token=Access_Token)
url = input("URL GİRİN: ")
shorten_url = connection.shorten(url)

print("URL: ",shorten_url.get("url"))

