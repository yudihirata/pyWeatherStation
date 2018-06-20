from datetime import datetime

import pytz

from model.AccuWeather import BaseObject
from model.AccuWeather.Day import Day


class Forecast(BaseObject):
    def __init__(self, data):
        super(Forecast, self).__init__(data)
        self.mDay = None

    @property
    def daily_forecasts(self):
        return self.data["DailyForecasts"][0]

    @property
    def headline(self):
        return self.data["Headline"]

    @property
    def epoch_date(self):
        return self.daily_forecasts["EpochDate"]

    def get_date(self, format="%a %d %B %H:%M"):
        """  Time of data calculation, unix, UTC """
        return datetime.fromtimestamp(self.daily_forecasts["EpochDate"], pytz.utc).strftime(format)

    @property
    def sunrise(self, format="%H:%M"):
        return datetime.fromtimestamp(self.daily_forecasts["Sun"]["EpochRise"], pytz.utc).strftime(format)

    @property
    def sunset(self, format="%H:%M"):
        return datetime.fromtimestamp(self.daily_forecasts["Sun"]["EpochSet"], pytz.utc).strftime(format)

    @property
    def moonrise(self, format="%H:%M"):
        return datetime.fromtimestamp(self.daily_forecasts["Moon"]["EpochRise"], pytz.utc).strftime(format)

    @property
    def moonset(self, format="%H:%M"):
        return datetime.fromtimestamp(self.daily_forecasts["Moon"]["EpochSet"], pytz.utc).strftime(format)

    @property
    def min_temperature(self):
        return self.daily_forecasts["Temperature"]["Minimum"]["Value"]

    @property
    def max_temperature(self):
        return self.daily_forecasts["Temperature"]["Maximum"]["Value"]

    @property
    def min_real_feel_temp(self):
        return self.daily_forecasts["RealFeelTemperature"]["Minimum"]["Value"]

    @property
    def max_real_feel_temp(self):
        return self.daily_forecasts["RealFeelTemperature"]["Maximum"]["Value"]

    @property
    def hours_of_sun(self):
        return self.daily_forecasts["HoursOfSun"]

    @property
    def degree_day_summary(self):
        return self.daily_forecasts["DegreeDaySummary"]

    @property
    def air_and_pollen(self):
        return self.daily_forecasts["AirAndPollen"]

    @property
    def day(self):
        if self.mDay is None:
            self.mDay = Day(self.daily_forecasts["Day"])
        return self.mDay