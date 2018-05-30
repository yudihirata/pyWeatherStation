# coding: utf-8
from layout.Resource import Resource


class Ellipse(Resource):

    def __init__(self, name, xy=None, fill=None, outline=None):
        Resource.__init__(self, name)
        self.mFill = fill
        self.mOutline = outline

    @property
    def fill(self):
        return self.mFill

    @fill.setter
    def fill(self, value):
        self.mFill = value

    @property
    def outline(self):
        return self.mOutline

    @outline.setter
    def outline(self, value):
        self.mOutline = value

    def createview(self, layout):
        super(Ellipse, self).createview(layout)