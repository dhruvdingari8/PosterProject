import Textbox as tb

TRACK_SIZE = 66
class Track(tb.Textbox):

    def __init__(self, track, posn):
        track_text = track["title"] + " - " + track["length"]
        super().__init__(track_text, posn, TRACK_SIZE)