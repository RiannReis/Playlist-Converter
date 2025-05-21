from flask import render_template, request, jsonify
from main import app
import time
from utils.spotify import get_spotify_token, get_playlist_tracks
from utils.youtube import search_youtube_video


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/convert", methods=["POST"])
def convert():
    data = request.json
    playlist_url = data.get("url")
    print(f"🎯 URL recebida: {playlist_url}")


    if not playlist_url or not playlist_url.startswith("https://open.spotify.com/playlist/"):
        return jsonify({"error": "Invalid playlist URL."}), 400

    try:
        token = get_spotify_token()
        print(f"🟢 Token gerado: {token[:10]}...")

        tracks = get_playlist_tracks(playlist_url, token)
        print(f"📋 Total de músicas: {len(tracks)}")

        results = []
        for track in tracks:
            query = f"{track['title']} {track['artist']}"
            print(f"🔍 Buscando no YouTube: {query}")

            yt_data = search_youtube_video(query)
            time.sleep(0.2)

            if yt_data:
                results.append({
                    "title": track["title"],
                    "artist": track["artist"],
                    "album": track["album"],
                    "thumbnail": yt_data["thumbnail"],
                    "youtube_link": yt_data["youtube_link"]
                })
            else:
                print(f"❌ Não encontrado no YouTube: {query}")

        print(f"✅ Total de resultados finais: {len(results)}")

        return jsonify({"results": results})

    except Exception as e:
        print(f"🔥 Erro: {e}")

        return jsonify({"error": str(e)}), 500