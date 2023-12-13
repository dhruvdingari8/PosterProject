import Textbox as tb

TRACK_SIZE = 66
class Track(tb.Textbox):

    def __init__(self, text, posn):
        super().__init__(text, posn, TRACK_SIZE)