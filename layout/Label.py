#coding: utf-8
from layout.Resource import Resource
from PIL import ImageFont
class Label(Resource):
    def __init__(self, name, text=None, font=None, fill=0):
        """
        :param: text - Text to be drawn. If it contains any newline characters
        :param: x - Top of the text
        :param: y - Left corner of the text
        :param: fill  – Color to use for the fill  """
        Resource.__init__(self, name)
        self.mText = text
        self.mFill = fill
        if font is None:
            self.mFont = ImageFont.truetype("res/fonts/FreeMonoBold.ttf", 12)
        else:
            self.mFont = font

    @property
    def text(self):
        return self.mText

    @text.setter
    def text(self, value):
        self.mText = value
    @property
    def Fill(self):
        return self.mFill

    @Fill.setter
    def Fill(self, value):
        self.mFill = value

    @property
    def font(self):
        return self.mFont

    @font.setter
    def font(self, value):
        self.mFont = value

    def createview(self, layout):
        super(Label, self).createview(layout)
        if layout["font"] is None:
            self.font = ImageFont.truetype("res/fonts/FreeMonoBold.ttf", 12)
        else:
            self.font = ImageFont.truetype("res/fonts/{0}.ttf".format(layout["font"]["name"]), layout["font"]["size"])
        self.parent.draw.text((self.x, self.y), self.text, font=self.font, fill=self.Fill)