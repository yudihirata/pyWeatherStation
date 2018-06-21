import json
import os
import urllib2

import R
from model.AccuWeather import City, Current
from model.AccuWeather.DailyForecast import DailyForecast
from model.AccuWeather.Forecasts import Forecasts


class AccuWeather(object):

    def __init__(self):
        self.mCity = None
        self.mForecasts = None

    @property
    def city(self):
        if self.mCity is None:
            filename = "{0}.json".format(R.config.ACCUWEATHER["city"])
            url = "{0}?apikey={1}&q={2}&language={3}&details=True".format(R.config.ACCUWEATHER["citysearch"],
                                                                          R.config.ACCUWEATHER["api_key"],
                                                                          R.config.ACCUWEATHER["city"],
                                                                          R.config.ACCUWEATHER["language"])
            data = self.get_cache(filename, url)
            self.mCity = City(data[0])
        return self.mCity

    @property
    def forecasts(self):
        if self.mForecasts is None:
            metric = "true" if R.config.ACCUWEATHER["unit"].lower() == "metric" else "false"
            url = "{0}/{1}?apikey={2}&details=true&metric={3}".format(R.config.ACCUWEATHER["forecastfive"], self.city.key,
                                                                      R.config.ACCUWEATHER["api_key"], metric)

            if "mode" in R.config.ACCUWEATHER and R.config.ACCUWEATHER["mode"] == "debug":
                data = self.get_cache("forecast5.json", url)
            else:
                data = json.load(urllib2.urlopen(url))
            self.mForecasts = Forecasts(data)
        else:
            return self.mForecasts

    def get_current(self):
        """
        Current weather data

        :return:
        """
        url = "{0}/{1}?apikey={2}&details=true".format(R.config.ACCUWEATHER["current"], self.city.key,
                                                       R.config.ACCUWEATHER["api_key"])

        if "mode" in R.config.ACCUWEATHER and R.config.ACCUWEATHER["mode"] == "debug":
            data = self.get_cache("current.json", url)
        else:
            data = json.load(urllib2.urlopen(url))

        return Current(data[0])

    # def getforecastfive(self):
    #     url = "{0}?q={1}&units={2}&mode=json&appid={3}".format(self.forecastfive, self.city, self.unit, self.api_key)
    #     return json.load(urllib2.urlopen(url))
    def refresh(self):
        del self.mForecasts
        self.mForecasts = None

    def get_dailyforecast(self, day):
        return self.forecasts.get_dailyforecasts(day)

    def get_cache(self, filename, url):
        if not os.path.isfile(filename):
            data = json.load(urllib2.urlopen(url))
            with open(filename, 'w') as outfile:
                json.dump(data, outfile)
        else:
            with open(filename) as f:
                data = json.load(f)
        return data