# sample youtube video url
video_url = "https://www.youtube.com/watch?v=-5B858LWJD0"
# init an HTML Session
# get the html content
session = requests.Session()
response = session.get(video_url)

# get meta data of the youtube video
bs.find_all("meta")

#get Title of video
name=bs.find("meta", itemprop="name")["content"]

#get number of views
count=bs.find("meta", itemprop="interactionCount")['content']

#get description
desc=bs.find("meta", itemprop="description")['content']

print("Title of the video is: ",name, "\nNumber of views are: ",count, "\nDescription of video is: ", desc)
