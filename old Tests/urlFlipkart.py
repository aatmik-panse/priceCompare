import requests
import pandas as pd
from bs4 import BeautifulSoup

# url=input()
url='https://www.flipkart.com/apple-iphone-14-midnight-128-gb/p/itm9e6293c322a84?pid=MOBGHWFHECFVMDCX&lid=LSTMOBGHWFHECFVMDCXSSCYWA&marketplace=FLIPKART&q=iphone+14&store=tyy%2F4io&srno=s_1_4&otracker=search&otracker1=search&fm=organic&iid=5c72b83a-94c2-4d0d-ae7f-29c035362351.MOBGHWFHECFVMDCX.SEARCH&ppt=hp&ppn=homepage&ssid=3ztqe1kygg0000001698782686382&qH=860f3715b8db08cd'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
nam = soup.find('span', 'B_NuCI').text
print(nam)
price_parent = soup.find('div', '_30jeq3 _16Jk6d').text
print(price_parent)