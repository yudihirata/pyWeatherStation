import os
from datetime import time, datetime

import pytz

from R import R
from model.AccuWeather import BaseObject


class  Current(BaseObject):

    def __init__(self, data):
        super(Current, self).__init__(data)

    @property
    def data(self):
        return self.mData

    @data.setter
    def data(self, value):
        self.mData = value

    @property
    def icon(self):
        resource = "res/drawable/{0}.png".format(self.data["WeatherIcon"])
        if not os.path.isfile(resource):
            resource = "res/drawable/refresh.png"
        return resource

    @property
    def description(self):
        return unicode(self.data["WeatherText"])

    @property
    def temperature(self):
        """ Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."""
        return int(self.data["Temperature"][self.unit]["Value"])

    @property
    def temperatureunit(self):
        """ Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."""
        return u'\N{DEGREE SIGN}' + self.data["Temperature"][self.unit]["Unit"]

    @property
    def stemperature(self):
        return str(self.temperature) + self.temperatureunit

    @property
    def pressure(self):
        """  Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data),
        hPa """
        return int(self.data["Pressure"][self.unit]["Value"])

    @property
    def pressureunit(self):
        return self.data["Pressure"][self.unit]["Unit"]

    @property
    def humidity(self):
        """ Humidity, %  """
        return self.data["RelativeHumidity"]

    @property
    def mintemperature(self):
        """ Minimum temperature at the moment. This is deviation from current temp that is possible
        for large cities and megalopolises geographically expanded (use these parameter optionally).
        Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit. """
        return int(self.data["TemperatureSummary"]["Past6HourRange"]["Minimum"][self.unit]["Value"])

    @property
    def maxtemperature(self):
        """ Maximum temperature at the moment. This is deviation from current temp that is possible
        for large cities and megalopolises geographically expanded (use these parameter optionally).
        Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit. """
        return int(self.data["TemperatureSummary"]["Past6HourRange"]["Maximum"][self.unit]["Value"])

    @property
    def wind(self):
        return self.data["Wind"]["Speed"][self.unit]["Value"]

    @property
    def swind(self):
        return u"{0}{1}".format(self.wind, self.wind_speed_unit)

    @property
    def wind_speed_unit(self):
        return self.data["Wind"]["Speed"][self.unit]["Unit"]

    @property
    def wind_degrees(self):
        return self.data["Wind"]["Direction"]["Degrees"]

    @property
    def swind_degrees(self):
        return str(self.wind_degrees) + u"\N{DEGREE SIGN}"

    @property
    def precipitation_1hr(self):
        return u"{0}{1}".format(self.data["Precip1hr"][self.unit]["Value"], self.data["Precip1hr"][self.unit]["Unit"])

    @property
    def wind_degrees_description(self):
        return self.data["Wind"]["Direction"]["Localized"]

    @property
    def dt(self):
        """  Time of data calculation, unix, UTC """
        return self.data["EpochTime"]

    def getdt(self, format="%a %d %B %H:%M"):
        """  Time of data calculation, unix, UTC """
        return R.strings.translate(unicode(datetime.fromtimestamp(self.dt, pytz.utc).strftime(format)).title())

    @property
    def uv_index(self):
        """
        Measure of the strength of the ultraviolet radiation from the sun. May be NULL.
        :return:int32.
        """
        return self.data["UVIndex"] if "UVIndex" in self.data else 0

    @property
    def uv_text(self):
        """
        Text associated with the UVIndex.
        :return: string
        """
        return self.data["UVIndexText"]

