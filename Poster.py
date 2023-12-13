import json as jsn
import Textbox as tb
import Title as t
import Track as tr
class Poster:



    def __init__(self, title, artist, tot_len, tracklist, info, cover, cover_colors, spotify_code):
        self.title = title  # Title of the album
        self.artist = artist # Artist of the album
        self.tot_len = tot_len # Total length of the album
        self.tracklist = tracklist # List of tracks in the album, is a list of Track objects
        self.info = info # Information about the album, Includes genre, year, and label
        self.cover = cover # Cover art of the album
        self.cover_colors = cover_colors # List of Hexadecimal values of the colors in the cover art (<= 6)
        self.spotify_code = spotify_code # Spotify code for the album

    def __str__(self):
        return "Title: " + str(self.title) + "\nArtist: " + str(self.artist) + "\nTotal Length: " + str(self.tot_len) + "\nTracklist: " + str(self.tracklist) + "\nInfo: " + str(self.info) + "\nCover: " + str(self.cover) + "\nCover Colors: " + str(self.cover_colors) + "\nSpotify Code: " + str(self.spotify_code)

class JSONReader:

        def readJSON(self, filename):
            """
            :returns a list of Poster objects from a JSON file
            :param filename: name of the file to read from
            """

            with open(filename, "r") as f:
                data = jsn.load(f)
                posters = []
                for poster_data in data:
                    title = t.Title(poster_data["album"])
                    artist = tb.Textbox(poster_data["artist"], (50, 1500), 48)
                    tot_len = tb.Textbox(poster_data["length"], (50, 1500), 66)
                    tracklist = []
                    for track in poster_data["tracklist"]:
                        tracklist.append(tr.Track(track, (50, 1500)))
                    album_info = poster_data["album_info"]

                    info = tb.Textbox(str(album_info["publisher"] + ", " + album_info["genre"] + ", " + album_info["release_date"]), (50, 1500), 66)
                    cover = poster_data["cover_art"]
                    cover_colors = poster_data["cover_colors"]
                    spotify_code = poster_data["spotify_code"]
                    posters.append(Poster(title, artist, tot_len, tracklist, info, cover, cover_colors, spotify_code))
                return posters

        def getPoster(self, *index):
            """
            :returns a Poster object at a given index
            :param index: index of the Poster object to return
            """
            if len(index) == 1:
                return self.POSTERS[index[0]]
            else:
                return self.POSTERS[index[0]:index[1]]

