# youtube_utils.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def search_youtube_video(query):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "key": YOUTUBE_API_KEY,
        "maxResults": 1,
        "type": "video"
    }
    print(f"🔍 YouTube search: {query}")

    r = requests.get(url, params=params)

    print(f"📡 YouTube status: {r.status_code}")
    print(f"📥 YouTube response: {r.json()}")

    items = r.json().get("items")
    if not items:
        return None

    item = items[0]
    video_id = item["id"]["videoId"]
    return {
        "youtube_link": f"https://www.youtube.com/watch?v={video_id}",
        "thumbnail": item["snippet"]["thumbnails"]["high"]["url"]
    }
