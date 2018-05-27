class Resource(object):
    def __init__(self, name):
        self.mName = name
        self.mParent = None
        self.mX = None
        self.mY = None

    @property
    def name(self):
        return self.mName

    @property
    def x(self):
        return self.mX

    @x.setter
    def x(self, value):
        self.mX = value

    @property
    def y(self):
        return self.mY

    @y.setter
    def y(self, value):
        self.mY = value

    @classmethod
    def getClassName(cls):
        return cls.__name__

    @property
    def Parent(self):
        return self.mParent

    @Parent.setter
    def Parent(self, value):
        self.mParent = value
