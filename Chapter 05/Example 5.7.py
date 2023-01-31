# importing the libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#Defining an empty dictionary result in which the properties and their values will be stored 
result={}

html = urlopen('https://www.youtube.com/watch?v=-5B858LWJD0')

# Parsing HTML code
soup = BeautifulSoup(html, 'html.parser')

# sample youtube video url
video_url = "https://www.youtube.com/watch?v=-5B858LWJD0"
session = requests.Session()
response = session.get(video_url)

# video title
result["title"] = soup.find("meta", itemprop="name")['content']

# video views (converted to integer)
result["views"] = result["views"] = soup.find("meta", itemprop="interactionCount")['content']

# video description
result["description"] = soup.find("meta", itemprop="description")['content']

# date published
result["date_published"] = soup.find("meta", itemprop="datePublished")['content']

# get the duration of video in minutes and seconds
result["duration"]= soup.find("meta", itemprop="duration")['content']

#print results, assume I is the key, following traverses through entire dictionary and prints keys and corresponding values
for i in result:
    print(i, ":", result[i])
    print("\n")

