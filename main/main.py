from flask import render_template, request, jsonify
from main import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/convert", methods=["POST"])
def convert():
    data = request.json
    playlist_url = data.get("url")

    if not playlist_url or not playlist_url.startswith("https://open.spotify.com/playlist/"):
        return jsonify({"error": "Invalid playlist URL."}), 400

    # mock:
    return jsonify({
        "results": [
            {
                "title": "Song 1",
                "artist": "Artist A",
                "album": "Album X",
                "thumbnail": "https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg",
                "youtube_link": "https://youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "title": "Song 2",
                "artist": "Artist B",
                "album": "Album Y",
                "thumbnail": "https://img.youtube.com/vi/9bZkp7q19f0/0.jpg",
                "youtube_link": "https://youtube.com/watch?v=9bZkp7q19f0"
            },{
                "title": "Song 1",
                "artist": "Artist A",
                "album": "Album X",
                "thumbnail": "https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg",
                "youtube_link": "https://youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "title": "Song 2",
                "artist": "Artist B",
                "album": "Album Y",
                "thumbnail": "https://img.youtube.com/vi/9bZkp7q19f0/0.jpg",
                "youtube_link": "https://youtube.com/watch?v=9bZkp7q19f0"
            },{
                "title": "Song 1",
                "artist": "Artist A",
                "album": "Album X",
                "thumbnail": "https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg",
                "youtube_link": "https://youtube.com/watch?v=dQw4w9WgXcQ"
            },
            {
                "title": "Song 2",
                "artist": "Artist B",
                "album": "Album Y",
                "thumbnail": "https://img.youtube.com/vi/9bZkp7q19f0/0.jpg",
                "youtube_link": "https://youtube.com/watch?v=9bZkp7q19f0"
            }
        ]
    })