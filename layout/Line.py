from layout.Resource import Resource


class Line(Resource):
    def __init__(self, name, xy=None, fill=None, width=0):
        Resource.__init__(self, name)
        self.mXY = xy
        self.mFill = fill
        self.mWidth = width

    @property
    def xy(self):
        return self.mXY

    @xy.setter
    def xy(self, value):
        self.mXY = value

    @property
    def fill(self):
        return self.mFill

    @fill.setter
    def fill(self, value):
        self.mFill = value

    @property
    def width(self):
        return self.mWidth

    @width.setter
    def width(self, value):
        self.mWidth = value

    def createview(self, layout):
        super(Line, self).createview(layout)
        if {"x", "y", "x1", "y1"}.issubset(set(layout)):
            self.xy = (layout["x"], layout["y"], layout["x1"], layout["y1"])

        if "fill" in layout:
            self.fill = layout["fill"]

        if "width" in layout:
            self.width = layout["width"]

        self.parent.draw.line(self.xy, self.fill, self.width)
