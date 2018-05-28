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

        resource.Parent = self
        if x is not None:
            resource.x = x
        if y is not None:
            resource.y = y
        self.children.update({resource.name: resource})

    def create(self):
        for name in self.children:
            if name in self.layout:
                resource = self.children[name]
                resource.x = self.layout[name]["x"]
                resource.y = self.layout[name]["y"]
                if resource.getClassName() == "Icon":
                    resource.resize(self.layout[name]["width"], self.layout[name]["height"])
                    self.mask.paste(resource.Image, (resource.x, resource.y), resource.Image)
                elif resource.getClassName() == "Label":
                    if self.layout[name]["font"] is None:
                        resource.font = ImageFont.truetype("res/FreeMonoBold.ttf", 12)
                    else:
                        resource.font = ImageFont.truetype("res/{0}.ttf".format(self.layout[name]["font"]["name"]),
                                                           self.layout[name]["font"]["size"])
                    self.draw.text((resource.x, resource.y), resource.text, font=resource.font,
                                   fill=resource.Fill)
                elif resource.getClassName() == "Line":
                    self.draw.line(resource.xy, resource.fill, resource.width )

    def save(self, output):
        out = self.mask.rotate(0)
        out.save(output, "bmp")
