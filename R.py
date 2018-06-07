import json

global values
global strings
global code
global config

HORIZONTAL = "horizontal"
LANDSCAPE = "landscape"
class Resources:
    def __init__(self):
        resource = "res/values/strings.json"
        with open('config.json') as f:
            self.mConfig = json.load(f)
        if self.mConfig["language"] != "default":
            resource = "res/values-{0}/strings.json".format(self.mConfig["language"])
        with open(resource) as f:
            self.mValues= json.load(f)

        for attr in self.mValues["tokens"]:
            setattr(self, unicode(attr.upper()), self.mValues["tokens"][attr] )

    @property
    def code(self):
        return self.mValues["strings"]

    @property
    def values(self):
        return self.mValues["tokens"]

    def translate(self, value):
        if value in self.mValues["tokens"]:
            return self.mValues["tokens"][value]
        else:
            return value

class Configuration:
    def __init__(self):
        with open('config.json') as f:
            config = json.load(f)
            for attr in config:
                setattr(self, unicode(attr.upper()), config[attr])



def init(language=None):
    global values
    global strings
    global config
    resource = "res/values/strings.json"


    strings = Resources()
    config = Configuration()
    if config.LANGUAGE != "default":
        resource = "res/values-{0}/strings.json".format(config["language"])
    with open(resource) as f:
        values= json.load(f)
        values = values["strings"]
