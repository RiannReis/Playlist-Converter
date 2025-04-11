async function convertPlaylist() {
  const url = document.getElementById("playlistInput").value.trim();
  const errorBox = document.getElementById("errorBox");
  const results = document.getElementById("results");

  errorBox.classList.add("hidden");
  results.innerHTML = "";

  if (!url.startsWith("https://open.spotify.com/playlist/")) {
    showError("Invalid Spotify playlist URL.");
    return;
  }

  try {
    const res = await fetch("/api/convert", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });

    const data = await res.json();

    if (!res.ok) {
      showError(data.error || "Unexpected error");
      return;
    }

    if (data.results.length === 0) {
      showError("No results found.");
      return;
    }

    data.results.forEach(item => {
      const itemDiv = document.createElement("div");
      itemDiv.className = "result-item";

      const thumbnail = document.createElement("img");
      thumbnail.src = item.thumbnail;
      thumbnail.alt = item.title;
      thumbnail.className = "thumbnail";

      const detailsDiv = document.createElement("div");
      detailsDiv.className = "result-details";

      const title = document.createElement("h4");
      title.textContent = item.title;

      const metaDiv = document.createElement("div");
      metaDiv.className = "result-meta";

      const leftDiv = document.createElement("div");
      leftDiv.className = "meta-left";

      const artist = document.createElement("p");
      artist.textContent = `Artist: ${item.artist}`;

      const album = document.createElement("p");
      album.textContent = `Album: ${item.album}`;

      leftDiv.appendChild(artist);
      leftDiv.appendChild(album);

      const rightDiv = document.createElement("div");
      rightDiv.className = "meta-right";

      const link = document.createElement("a");
      link.href = item.youtube_link;
      link.textContent = "Watch on YouTube";
      link.target = "_blank";
      link.rel = "noopener noreferrer";

      rightDiv.appendChild(link);

      metaDiv.appendChild(leftDiv);
      metaDiv.appendChild(rightDiv);

      detailsDiv.appendChild(title);
      detailsDiv.appendChild(metaDiv);

      itemDiv.appendChild(thumbnail);
      itemDiv.appendChild(detailsDiv);

      results.appendChild(itemDiv);
    });

    const createBtn = document.createElement("button");
    createBtn.textContent = "Create Playlist";
    createBtn.style.marginTop = "20px";

    const playlistLinkDiv = document.createElement("div");
    playlistLinkDiv.id = "playlistLink";
    playlistLinkDiv.style.marginTop = "15px";
    playlistLinkDiv.className = "hidden";

    createBtn.onclick = () => {
      const mockPlaylistUrl = "https://youtube.com/playlist?list=PL123456789";
      playlistLinkDiv.innerHTML = `<a href="${mockPlaylistUrl}" target="_blank" rel="noopener noreferrer">${mockPlaylistUrl}</a>`;
      playlistLinkDiv.classList.remove("hidden");
    };

    results.appendChild(createBtn);
    results.appendChild(playlistLinkDiv);
z

  } catch (err) {
    showError("Failed to convert playlist.");
  }
}

function showError(message) {
  const errorBox = document.getElementById("errorBox");
  errorBox.textContent = message;
  errorBox.classList.remove("hidden");
}