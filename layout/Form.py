from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import json
import tokens

from layout.Resource import Resource


class Form(Resource):
    def __init__(self, name, height, width):
        Resource.__init__(self, name)
        # https://pillow.readthedocs.io/en/3.1.x/handbook/concepts.html#concept-modes
        # L (8-bit pixels, black and white)
        self.mMask = Image.new('1', (height, width), 255)
        self.mDraw = None
        self.mLayout = None
        self.mChildren = dict()
        tokens.init()  # Initialize tokens

    @property
    def layout(self):
        if self.mLayout is None:
            with open("res/layout/{0}.json".format(self.name)) as f:
                self.mLayout = json.load(f)
        return self.mLayout[self.name]

    @layout.setter
    def layout(self, value):
        self.mLayout = value

    @property
    def children(self):
        return self.mChildren

    @property
    def mask(self):
        return self.mMask

    @mask.setter
    def mask(self, value):
        self.mMask = value

    @property
    def draw(self):
        if self.mDraw is None:
            self.mDraw = ImageDraw.Draw(self.mask)
        return self.mDraw

    def add(self, resource, x=None, y=None):

        resource.parent = self
        if x is not None:
            resource.x = x
        if y is not None:
            resource.y = y
        self.children.update({resource.name: resource})

    def oncreateview(self):
        for name in self.children:
            if name in self.layout:
                resource = self.children[name]
                resource.createview(self.layout[name])


    def save(self, output):
        out = self.mask.rotate(0)
        out.save(output, "bmp")
