import json
import Poster as Pstr
import Textbox as tb
import Track as tr
import Title as ttl

class PosterMaker:
    POSTERS = []

    def __init__(self):
        pass

    def setPosters(self, posters):
        """
        Sets the POSTERS list to a given list of Poster objects
        :param posters: list of Poster objects
        """
        self.POSTERS = posters

    def readJSON(self, filename):
        """
        :returns a list of Poster objects from a JSON file
        :param filename: name of the file to read from
        """

        with open(filename, "r") as f:
            data = json.load(f)
            posters = []
            for poster_data in data:
                title = ttl.Title(poster_data["album"])
                artist = tb.Textbox(poster_data["artist"], (50, 1500), 48)
                tot_len = tb.Textbox(poster_data["length"], (50, 1500), 66)
                tracklist = []
                for track in poster_data["tracklist"]:
                    tracklist.append(tr.Track(track, (50, 1500)))
                info = tb.Textbox(poster_data["album_info"], (50, 1500), 66)
                cover = poster_data["cover_art"]
                cover_colors = poster_data["cover_colors"]
                spotify_code = poster_data["spotify_code"]
                posters.append(Pstr.Poster(title, artist, tot_len, tracklist, info, cover, cover_colors, spotify_code))
            POSTERS = posters

    def getPoster(self, *index):
        """
        :returns a Poster object at a given index
        :param index: index of the Poster object to return
        """
        if len(index) == 1:
            return self.POSTERS[index[0]]
        else:
            return self.POSTERS[index[0]:index[1]]



