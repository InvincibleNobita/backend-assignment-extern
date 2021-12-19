from django.http import response
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
import os
import requests
from googleapiclient.discovery import build

API_KEY = 'AIzaSyAiilfIk3MTGXGaJp-YVWYjqL7y4yUhIpo'

youtube=build('youtube', 'v3', developerKey=API_KEY)



# Create your views here.
API_URL=f"https://www.googleapis.com/youtube/v3/videos?id=7lCDEYXw3mM&key={API_KEY}&part=snippet,contentDetails,statistics,status"
def call(request):
    req = youtube.channels().list(
            part="video"
        )
    return JsonResponse(req.json())


