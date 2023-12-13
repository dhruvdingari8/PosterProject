import Textbox

TRACK_SIZE = 66
class Track(Textbox):

    def __init__(self, text, posn):
        super().__init__(text, posn, TRACK_SIZE)