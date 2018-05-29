import PIL
from PIL import Image
from layout.Resource import Resource
class Icon(Resource):
    def __init__(self, name, filePath, width=None, height= None):
        Resource.__init__(self, name)
        self.mFile = filePath
        self.mImage = Image.open(filePath)
        #self.resize(width, height)

    @property
    def Height(self):
        return self.Image.height

    @property
    def Width(self):
        return self.Image.width

    @property
    def Image(self):
        return self.mImage

    def resize(self, width, height):
        if width is not None and height is not None:
            self.mImage = self.mImage.resize((width, height))

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
       self.mImage = self.mImage.rotate(angle, resample, expand)
    def createview(self, layout):
        super(Icon, self).createview(layout)
        self.resize(layout["width"], layout["height"])
        self.parent.mask.paste(self.Image, (self.x, self.y), self.Image)