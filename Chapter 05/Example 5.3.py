##storing images in the current directory
import requests
from bs4 import BeautifulSoup
import os
 
url='https://rubikscode.net/'
r=requests.get(url)
soup=BeautifulSoup(r.text, 'html.parser')
images=soup.find_all('img')
 
fl=0
 
for image in images:
    link=image['src']
    fl=int(fl)+1
    with open('file'+str(fl)+'.jpg','wb') as f:
        in=requests.get(link)
f.write(in.content)
