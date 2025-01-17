import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR UNIQUE CLIENT ID,
        client_secret=YOUR UNIQUE CLIENT SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=YOUR SPOTIFY DISPLAY NAME, 
    )
)

user_id = sp.current_user()["id"]


date = input("Which year music do you want to listen? Type in this Format YYYY-MM-DD: ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url= url, headers= header)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.select("li ul li h3")
for names in titles:
    song_name = names.getText().strip()



song_uris = []

year = date.split("-")[0]
for song in song_name:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
