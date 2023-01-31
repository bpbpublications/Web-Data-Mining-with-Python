import requests
from bs4 import BeautifulSoup
import os
 
url='https://rubikscode.net/'
 
ur=requests.get(url)
 
soup=BeautifulSoup(ur.text, 'html.parser')
 
images=soup.find_all('img')
 
for image in images:
    print(image['src'])
