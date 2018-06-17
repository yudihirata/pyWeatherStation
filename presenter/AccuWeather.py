import json
import urllib2


class AccuWeather(object):

    def __init__(self):
        self.mConfig = None

    @property
    def config(self):
        if self.mConfig is None:
            with open('config.json') as f:
                self.mConfig = json.load(f)
        return self.mConfig["accuweather"]

    @property
    def api_key(self):
        return self.config["api_key"]

    @property
    def current(self):
        return self.config["current"]

    @property
    def forecastfive(self):
        return self.config["forecastfive"]

    @property
    def unit(self):
        return self.config["unit"]

    @property
    def city(self):
        return self.config["city"]

    def getcurrent(self):
        """
        Current weather data
        https://openweathermap.org/current

        :return:
        """
        url = "{0}?q={1}&units={2}&mode=json&appid={3}".format(self.current, self.city, self.unit, self.api_key)
        return json.load(urllib2.urlopen(url))

    def getforecastfive(self):
        url = "{0}?q={1}&units={2}&mode=json&appid={3}".format(self.forecastfive, self.city, self.unit, self.api_key)
        return json.load(urllib2.urlopen(url))