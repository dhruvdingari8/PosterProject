import json
import Poster as Pstr
import Textbox as tb
import Track as tr
import Title as ttl

def readJSON(filename):
    """
    :returns a list of Poster objects from a JSON file
    :param filename: name of the file to read from
    """

    with open(filename, "r") as f:
        data = json.load(f)
        posters = []
        for poster_data in data:
            title = ttl.Title(poster_data["album"])
            artist = tb.Textbox(poster_data["artist"], (50, 1500), 66)
            tot_len = tb.Textbox(poster_data["length"], (50, 1500), 66)
            tracklist = []
            for track in poster_data["tracklist"]:
                tracklist.append(tr.Track(track, (50, 1500)))
            info = tb.Textbox(poster_data["album_info"], (50, 1500), 66)
            cover = poster_data["cover_art"]
            cover_colors = poster_data["cover_colors"]
            spotify_code = poster_data["spotify_code"]
            posters.append(Pstr.Poster(title, artist, tot_len, tracklist, info, cover, cover_colors, spotify_code))
        return posters


readJSON("input.json")