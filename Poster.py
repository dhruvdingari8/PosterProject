import json as jsn
import Textbox
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

