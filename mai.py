import requests
import json
from googleapiclient.discovery import build

API_KEY = 'AIzaSyAiilfIk3MTGXGaJp-YVWYjqL7y4yUhIpo'

youtube=build('youtube', 'v3', developerKey=API_KEY)


# API_KEY = 'AIzaSyAiilfIk3MTGXGaJp-YVWYjqL7y4yUhIpo'


# Create your views here.
# https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q=YOURKEYWORD&type=video&key=YOURAPIKEY
API_URL=f"https://www.googleapis.com/youtube/v3/videos?id=7lCDEYXw3mM&key={API_KEY}&part=snippet,contentDetails,statistics,status"
def call():
   
    # data=requests.get(API_URL)
    # print(data.json())
    requ = youtube.search().list(
            part="snippet",
            maxResults=5,
            q="free fire",
            type="video",
            order="date" ,
            publishedAfter="2021-01-01T00:00:00Z"
        )
    resu=requ.execute()
    items=resu["items"]
    for res in items:

        vT=res["snippet"]["title"]
        des=res["snippet"]["description"]
        thumbn=res["snippet"]["thumbnails"]["default"]["url"]
        pat=res["snippet"]["publishedAt"]
        print(vT," ", des, " ",thumbn," ",pat,end="\n" )
    return (resu)
    
call()
