from layout.Resource import Resource


class Line(Resource):
    def __init__(self, name, xy, fill=None, width=0):
        Resource.__init__(self, name)
        self.mXY = xy
        self.mFill = fill
        self.mWidth = width

    @property
    def xy(self):
        return self.mXY

    @property
    def fill(self):
        return self.mFill

    @property
    def width(self):
        return self.mWidth
