import json

global values


def init(language=None):
    resource = "res/values/strings.json"
    with open('config.json') as f:
        config = json.load(f)
    global values
    if config["language"] != "default":
        resource = "res/values-{0}/strings.json".format(config["language"])
    with open(resource) as f:
        values = json.load(f)
    values = values["strings"]
