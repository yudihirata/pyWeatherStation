import json
class Configuration:
    __instance = None

    @staticmethod
    def get_instance():
        if Configuration.__instance is None:
            Configuration()
        return Configuration.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Configuration.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            with open('config.json') as f:
                config = json.load(f)
                for attr in config:
                    setattr(self, unicode(attr.upper()), config[attr])
            Configuration.__instance = self
