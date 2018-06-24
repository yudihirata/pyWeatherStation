from abc import ABCMeta, abstractmethod


class Resource(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.mName = name
        self.mParent = None
        self.mX = None
        self.mY = None
        self.mLayout_toRightOf = None
        self.mLayout_toTopOf = None

    @property
    def name(self):
        return self.mName

    @name.setter
    def name(self, value):
        self.mName = value

    @property
    def x(self):
        if self.mX is None and self.parent is not None and self.layout_to_left_of is not None and \
                self.layout_to_left_of in self.parent.children:
            resource = self.parent.children[self.layout_to_left_of]
            self.mX = resource.x
        return self.mX

    @x.setter
    def x(self, value):
        self.mX = value

    @property
    def y(self):
        if self.mY is None and self.parent is not None and self.layout_to_top_of is not None and \
                self.layout_to_top_of in self.parent.children:
            resource = self.parent.children[self.layout_to_top_of]
            self.mY = resource.y
        return self.mY

    @y.setter
    def y(self, value):
        self.mY = value

    @property
    def layout_to_left_of(self):
        return self.mLayout_toRightOf

    @layout_to_left_of.setter
    def layout_to_left_of(self, value):
        self.mLayout_toRightOf = value

    @property
    def layout_to_top_of(self):
        return self.mLayout_toTopOf

    @layout_to_top_of.setter
    def layout_to_top_of(self, value):
        self.mLayout_toTopOf = value

    @y.setter
    def y(self, value):
        self.mY = value

    @classmethod
    def getClassName(cls):
        return cls.__name__

    @property
    def parent(self):
        return self.mParent

    @parent.setter
    def parent(self, value):
        self.mParent = value

    @abstractmethod
    def create_view(self, layout):
        pass

    def load_layout(self, layout):
        self.layout_to_left_of = layout["layout_to_left_of"] if "layout_to_left_of" in layout else None
        self.layout_to_top_of = layout["layout_to_top_of"] if "layout_to_top_of" in layout else None
        self.x = layout["x"] if "x" in layout else None
        self.y = layout["y"] if "y" in layout else None
