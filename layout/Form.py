import json
from collections import OrderedDict

from PIL import Image
from PIL import ImageDraw

import R
from layout.Resource import Resource

from pydoc import locate


class Form(Resource):
    def __init__(self, name):
        Resource.__init__(self, name)
        R.init()  # Initialize resources
        # https://pillow.readthedocs.io/en/3.1.x/handbook/concepts.html#concept-modes
        # 1 (1-bit pixels, black and white, stored with one pixel per byte)
        # L (8-bit pixels, black and white)
        # P (8-bit pixels, mapped to any other mode using a colour palette)
        if R.config.ORIENTATION == R.LANDSCAPE:
            self.mMask = Image.new('P', (R.config.WIDTH, R.config.HEIGHT), 255)
        else:
            self.mMask = Image.new('P', (R.config.HEIGHT, R.config.WIDTH), 255)

        self.mDraw = None
        self.mLayout = None
        self.mChildren = OrderedDict()
        self.load_layout(self.layout)

    @property
    def layout(self):
        if self.mLayout is None:
            if R.config.ORIENTATION == R.LANDSCAPE:
                resource = "res/layout/{0}.json".format(self.name)
            else:
                resource = "res/layout-portrait/{0}.json".format(self.name)

            with open(resource) as f:
                input_data = f.read()
            self.mLayout = json.loads(input_data.decode('utf-8'), object_pairs_hook=OrderedDict)
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

    def load_layout(self, layout):
        # locate classes from layout and create their instances dynamically
        for resource in layout:
            classname = layout[resource]["class"]
            obj = locate(classname)(resource)
            if "load_layout" in dir(obj):
                self.add(obj)
                obj.load_layout(layout[resource])


    def create_view(self):
        for name in self.children:
            if name in self.layout:
                resource = self.children[name]
                resource.create_view()

    def save(self, output):
        if R.config.ORIENTATION == R.PORTRAIT:
            out = self.mask.rotate(-90, expand=True)
        else:
            out = self.mask.rotate(0, expand=True)
        out.convert("P")
        out.save(output, "bmp", quality=100)
