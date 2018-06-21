from datetime import datetime

import pytz

from model.AccuWeather import BaseObject
from model.AccuWeather.Day import Day


class DailyForecast(BaseObject):
    def __init__(self, data):
        super(DailyForecast, self).__init__(data)
        self.mDay = None

    @property
    def epoch_date(self):
        return self.data["EpochDate"]

    def get_date(self, format="%a %d %B %H:%M"):
        """  Time of data calculation, unix, UTC """
        return datetime.fromtimestamp(self.data["EpochDate"], pytz.utc).strftime(format)

    @property
    def sunrise(self, format="%H:%M"):
        return datetime.fromtimestamp(self.data["Sun"]["EpochRise"], pytz.utc).strftime(format)

    @property
    def sunset(self, format="%H:%M"):
        return datetime.fromtimestamp(self.data["Sun"]["EpochSet"], pytz.utc).strftime(format)

    @property
    def moonrise(self, format="%H:%M"):
        return datetime.fromtimestamp(self.data["Moon"]["EpochRise"], pytz.utc).strftime(format)

    @property
    def moonset(self, format="%H:%M"):
        return datetime.fromtimestamp(self.data["Moon"]["EpochSet"], pytz.utc).strftime(format)

    @property
    def min_temperature(self):
        return self.data["Temperature"]["Minimum"]["Value"]

    @property
    def max_temperature(self):
        return self.data["Temperature"]["Maximum"]["Value"]

    @property
    def min_real_feel_temp(self):
        return self.data["RealFeelTemperature"]["Minimum"]["Value"]

    @property
    def max_real_feel_temp(self):
        return self.data["RealFeelTemperature"]["Maximum"]["Value"]

    @property
    def hours_of_sun(self):
        return '{0:02.0f}:{1:02.0f}'.format(*divmod(self.data["HoursOfSun"] * 60, 60)) \
            if "HoursOfSun" in self.data else None

    @property
    def degree_day_summary(self):
        return self.data["DegreeDaySummary"]

    @property
    def air_and_pollen(self):
        return self.data["AirAndPollen"]

    @property
    def day(self):
        if self.mDay is None:
            self.mDay = Day(self.data["Day"])
        return self.mDay