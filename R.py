import json

global values
global strings
global code


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


def init(language=None):
    resource = "res/values/strings.json"
    with open('config.json') as f:
        config = json.load(f)
    global values
    global strings
    strings = Resources()

    if config["language"] != "default":
        resource = "res/values-{0}/strings.json".format(config["language"])
    with open(resource) as f:
        values= json.load(f)
        values = values["strings"]
