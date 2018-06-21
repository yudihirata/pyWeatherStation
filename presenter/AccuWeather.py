import json
import os
import urllib2

import R
from model.AccuWeather import City, Current
from model.AccuWeather.Forecast import Forecast


class AccuWeather(object):

    def __init__(self):
        self.mCity = None

    @property
    def city(self):
        if self.mCity is None:
            filename = "{0}.json".format(R.config.ACCUWEATHER["city"])
            data ={}
            if not os.path.isfile(filename):
                url = "{0}?apikey={1}&q={2}&language={3}&details=True".format(R.config.ACCUWEATHER["citysearch"],
                                                                              R.config.ACCUWEATHER["api_key"],
                                                                              R.config.ACCUWEATHER["city"],
                                                                              R.config.ACCUWEATHER["language"])
                data = json.load(urllib2.urlopen(url))
                self.mCity = City(data[0])
                with open(filename, 'w') as outfile:
                    json.dump(data, outfile)
            else:
                with open(filename) as f:
                    data = json.load(f)
                self.mCity = City(data[0])

        return self.mCity

    def getcurrent(self):
        """
        Current weather data

        :return:
        """
        url = "{0}/{1}?apikey={2}&details=true".format(R.config.ACCUWEATHER["current"], self.city.key,
                                                       R.config.ACCUWEATHER["api_key"])
        data = json.load(urllib2.urlopen(url))
        return Current(data[0])

    # def getforecastfive(self):
    #     url = "{0}?q={1}&units={2}&mode=json&appid={3}".format(self.forecastfive, self.city, self.unit, self.api_key)
    #     return json.load(urllib2.urlopen(url))

    def getforecast(self):
        metric = "true" if R.config.ACCUWEATHER["unit"].lower() == "metric" else "false"
        url = "{0}/{1}?apikey={2}&details=true&metric={3}".format(R.config.ACCUWEATHER["forecastone"], self.city.key,
                                                       R.config.ACCUWEATHER["api_key"], metric)
        data = json.load(urllib2.urlopen(url))
        return Forecast(data)