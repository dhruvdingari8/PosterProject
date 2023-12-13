

class Textbox:

    def __init__(self, text, posn, size, color = "Black", font = "Bree Serif"):
        self.text = text
        self.posn = posn
        self.size = size
        self.color = color
        self.font = font

    def __str__(self):
        return self.text, "at", self.posn, "with size", self.size, "and color", self.color, "and font", self.font


