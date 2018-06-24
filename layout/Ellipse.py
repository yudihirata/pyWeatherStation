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

    def load_layout(self, layout):
        super(Ellipse, self).load_layout(layout)
        self.x1 = layout["x1"] if "x1" in layout else None
        self.y1 = layout["y1"] if "y1" in layout else None
        self.xy = (self.x, self.y, self.x1, self.y1)

        if "fill" in layout:
            self.fill = layout["fill"]

        if "outline" in layout:
            self.outline = layout["outline"]

    def create_view(self):
        self.parent.draw.ellipse(self.xy, fill=self.fill, outline=self.outline)