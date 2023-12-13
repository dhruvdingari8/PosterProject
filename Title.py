import Textbox as tb

TITLE_SIZE = 66
TITLE_POSITION = (50, 1500) # (0, 0) is the top left corner of the image, reference point of textbox is top left corner.

class Title(tb.Textbox):

    def __init__(self, text):
        super().__init__(text, TITLE_POSITION, TITLE_SIZE)
