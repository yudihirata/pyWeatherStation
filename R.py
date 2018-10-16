from singleton.Configuration import Configuration
from singleton.Resources import Resources

class R:
    PORTRAIT = "portrait"
    LANDSCAPE = "landscape"
    config = None
    strings = None
    __instance = None

    @staticmethod
    def get_instance():
        return R.__instance

    @staticmethod
    def init():
        R()

    def __init__(self):
        """ Virtually private constructor. """
        if R.config is not None:
            raise Exception("This class is a singleton!")
        else:
            R.config = Configuration.get_instance()
            R.strings = Resources.get_instance()
            R.__instance = self

    @staticmethod
    def translate(value):
        return R.strings.translate(value)