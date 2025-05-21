import requests
import os
from dotenv import load_dotenv
from base64 import b64encode

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

def get_spotify_token():
    auth = b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}"
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    return response.json().get("access_token")

def get_playlist_tracks(playlist_url, token):
    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    print(f"🎯 Playlist ID: {playlist_id}")

    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    response = requests.get(url, headers=headers)

    print(f"📡 Primeira requisição status: {response.status_code}")
    data = response.json()
    print(f"📥 Cabeçalho da resposta: {list(data.keys())}")

    if "error" in data:
        print("❌ Erro na resposta:", data["error"])
        return []


    print(f"🔵 Spotify API status: {response.status_code}")
    data = response.json()
    print(f"📥 JSON recebido: {data}")
    

    items = data.get("tracks", {}).get("items", [])
    print(f"🔄 Página inicial: {len(items)} músicas")


    songs = []
    for item in items:
        track = item["track"]
        title = track["name"]
        artist = track["artists"][0]["name"]
        album = track["album"]["name"]
        print(f"🎵 Música encontrada: {title} - {artist}")
        songs.append({"title": title, "artist": artist, "album": album})
    return songs
