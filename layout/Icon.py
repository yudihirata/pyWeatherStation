import PIL
from PIL import Image
from layout.Resource import Resource


class Icon(Resource):
    def __init__(self, name, filepath=None, width=None, height=None):
        Resource.__init__(self, name)
        self.mFile = filepath
        self.mImage = None
        self.resize(width, height)
        self.mAngle = None
        self.mHeight = None
        self.mWidth = None


    def loadlayout(self, layout):
        if "text" in layout:
            self.text = layout["text"]
        if "x" in layout:
            self.x = layout["x"]
        if "y" in layout:
            self.y = layout["y"]

        if "image" in layout:
            self.file = layout["image"]

        if {"width", "height"}.issubset(set(layout)) :
            self.width = layout["width"]
            self.height = layout["height"]

        if "angle" in layout:
            self.angle = int(layout["angle"])

    @property
    def file(self):
        return self.mFile

    @file.setter
    def file(self, value):
        self.mFile = value

    @property
    def angle(self):
        return self.mAngle

    @angle.setter
    def angle(self, value):
        self.mAngle = value

    @property
    def height(self):
        return self.mHeight

    @height.setter
    def height(self, value):
        self.mHeight = value

    @property
    def width(self):
        return self.mWidth

    @width.setter
    def width(self, value):
        self.mWidth = value

    @property
    def image(self):
        if self.file is not None and self.mImage is None:
            self.mImage = Image.open(self.file)
        self.width = self.mImage.width
        self.height = self.mImage.height
        return self.mImage

    @image.setter
    def image(self, value):
        self.mImage = value

    def resize(self, width, height):
        if width is not None and height is not None:
            newimage = self.image.resize((width, height))
            self.image = newimage
            self.width = self.image.width
            self.height = self.image.height

    def rotate(self, angle, resample=PIL.Image.NEAREST, expand=0, center=None,
               translate=None):
        """
       Returns a rotated copy of this image.  This method returns a
       copy of this image, rotated the given number of degrees counter
       clockwise around its centre.

       :param angle: In degrees counter clockwise.
       :param resample: An optional resampling filter.  This can be
          one of :py:attr:`PIL.Image.NEAREST` (use nearest neighbour),
          :py:attr:`PIL.Image.BILINEAR` (linear interpolation in a 2x2
          environment), or :py:attr:`PIL.Image.BICUBIC`
          (cubic spline interpolation in a 4x4 environment).
          If omitted, or if the image has mode "1" or "P", it is
          set :py:attr:`PIL.Image.NEAREST`. See :ref:`concept-filters`.
       :param expand: Optional expansion flag.  If true, expands the output
          image to make it large enough to hold the entire rotated image.
          If false or omitted, make the output image the same size as the
          input image.  Note that the expand flag assumes rotation around
          the center and no translation.
       :param center: Optional center of rotation (a 2-tuple).  Origin is
          the upper left corner.  Default is the center of the image.
       :param translate: An optional post-rotate translation (a 2-tuple).
       """
        if angle is not None:
            self.mImage = self.mImage.rotate(angle*-1, resample, expand)

    def loadlayout(self, layout):
        super(Icon, self).loadlayout(layout)
        if "image" in layout:
            self.file = layout["image"]
        if "width" in layout:
            self.width = layout["width"]

        if "height" in layout:
            self.height = layout["height"]

        if "angle" in layout:
            self.angle = layout["angle"]
            self.image = self.image.rotate(self.angle)

    def createview(self):
        self.resize(self.width, self.height)
        self.rotate(self.angle)
        self.parent.mask.paste(self.image, (self.x, self.y), self.image)
