import json
import os
import urllib2
from datetime import datetime

import matplotlib

from R import R
from model.AccuWeather import City, Current
from model.AccuWeather.Forecasts import Forecasts

matplotlib.use('Agg')
import matplotlib.pyplot as plt


class AccuWeather(object):

    def __init__(self):
        self.mCity = None
        self.mForecasts = None
        self.mTwelveHours = None

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
            url = "{0}/{1}?apikey={2}&details=true&metric={3}".format(R.config.ACCUWEATHER["forecastfive"],
                                                                      self.city.key,
                                                                      R.config.ACCUWEATHER["api_key"], metric)

            if "mode" in R.config.ACCUWEATHER and R.config.ACCUWEATHER["mode"] == "debug":
                data = self.get_cache("forecast5.json", url)
            else:
                data = json.load(urllib2.urlopen(url))
            self.mForecasts = Forecasts(data)

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

    def refresh(self):
        del self.mForecasts
        self.mForecasts = None
        self.mTwelveHours = None

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

    @property
    def twelve_hours(self):
        metric = "true" if R.config.ACCUWEATHER["unit"].lower() == "metric" else "false"
        url = "{0}/{1}?apikey={2}&details=true&metric={3}".format(R.config.ACCUWEATHER["twelvehours"], self.city.key,
                                                                  R.config.ACCUWEATHER["api_key"], metric)
        if self.mTwelveHours is None:
            if "mode" in R.config.ACCUWEATHER and R.config.ACCUWEATHER["mode"] == "debug":
                self.mTwelveHours = self.get_cache("twelve.json", url)
            else:
                self.mTwelveHours = json.load(urllib2.urlopen(url))
        return self.mTwelveHours

    def createchart(self, filename):
        x = []
        y = []
        xlabel = []
        ylabel = []

        count = 1

        for hour in self.twelve_hours:
            temp = hour["Temperature"]["Value"]
            y.append(int(temp))
            x.append(count)
            ylabel.append(int(temp))
            xlabel.append(datetime.fromtimestamp(hour["EpochDateTime"]).strftime("%H"))
            count = count + 1

        ax = plt.subplot(2, 1, 1)
        ax.grid(linewidth=1, linestyle="--")
        plt.xticks(x, xlabel, size=11, weight='bold')
        plt.yticks(y, ylabel, size=11, weight='bold')
        plt.plot(x, y, 'o-', linewidth=2)
        # plt.setp(ax.spines.values(), linewidth=2)
        # ax.get_yaxis().set_visible(False)

        # Hide the right and top spines
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['left'].set_visible(False)

        # for s, d in zip(x, y):
        #     plt.annotate(int(d), xy=(s,d), weight='bold', size=14)
        plt.savefig(filename, bbox_inches='tight', orientation="landscape", transparent=True, frameon=True)
        plt.clf()
