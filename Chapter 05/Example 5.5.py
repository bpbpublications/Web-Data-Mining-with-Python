from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://www.youtube.com/watch?v=-5B858LWJD0')

bs = BeautifulSoup(html, 'html.parser')

# sample youtube video url
video_url = "https://www.youtube.com/watch?v=-5B858LWJD0"
# init an HTML Session
# get the html content
session = requests.Session()
response = session.get(video_url)
bs.find_all("meta")
