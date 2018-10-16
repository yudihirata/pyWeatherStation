import json

from singleton.Configuration import Configuration


class Resources:
    __instance = None
    values = None

    @staticmethod
    def get_instance():
        if Resources.__instance is None:
            Resources()
        return Resources.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Resources.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            if Configuration.get_instance().LANGUAGE != "default":
                resource = "res/values-{0}/strings.json".format(Configuration.get_instance().LANGUAGE)
            else:
                resource = "res/values/strings.json"
            with open(resource) as f:
                data = json.load(f)
            Resources.values = data["tokens"]

            for attr in self.values:
                setattr(self, unicode(attr.upper()), data["tokens"][attr])

            Resources.__instance = self

    def translate(self, value):
        if value.upper() in self.values:
            return self.values[value.upper()]
        else:
            return value