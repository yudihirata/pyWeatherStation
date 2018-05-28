import json

global values


def init(language=None):
    resource = "res/values/strings.json"
    global values
    if language is not None:
        resource = "res/values-{0}/strings.json".format(language)
    with open(resource) as f:
        values = json.load(f)
    values = values["strings"]
