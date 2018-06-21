from layout.Resource import Resource


class Line(Resource):
    def __init__(self, name, xy=None, fill=None, width=0):
        Resource.__init__(self, name)
        self.mXY = xy
        self.mFill = fill
        self.mWidth = width
        self.mDashedline = False

    @property
    def xy(self):
        return self.mXY

    @property
    def dashedline(self):
        return self.mDashedline

    @dashedline.setter
    def dashedline(self, value):
        self.mDashedline = (value.lower() == "true")

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

    def load_layout(self, layout):
        super(Line, self).load_layout(layout)
        if {"x", "y", "x1", "y1"}.issubset(set(layout)):
            self.xy = (layout["x"], layout["y"], layout["x1"], layout["y1"])

        if "fill" in layout:
            self.fill = layout["fill"]

        if "width" in layout:
            self.width = layout["width"]

        if "dashedline" in layout:
            self.dashedline = layout["dashedline"]

    def create_view(self):
        if self.dashedline is True:
            x = 0
            width = self.xy[2] - self.xy[0]
            for index in range(width / 5):
                self.parent.draw.line((x, self.xy[1], x + 5, self.xy[3]), width=self.width)
                x = x + 10
        else:
            self.parent.draw.line(self.xy, self.fill, self.width)
