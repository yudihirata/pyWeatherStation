import json
# https://openweathermap.org/current
import time
import math
from datetime import datetime

import R

class Weather:
    """
    coord
        coord.lon City geo location, longitude
        coord.lat City geo location, latitude
    weather (more info Weather condition codes)
        weather.id Weather condition id
        weather.main Group of weather parameters (Rain, Snow, Extreme etc.)
        weather.description Weather condition within the group
        weather.icon Weather icon id
    base Internal parameter
    main
        main.temp Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
        main.pressure Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa
        main.humidity Humidity, %
        main.temp_min Minimum temperature at the moment. This is deviation from current temp that is possible for large
        cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric:
        Celsius, Imperial: Fahrenheit.
        main.temp_max Maximum temperature at the moment. This is deviation from current temp that is possible for large
        cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric:
         Celsius, Imperial: Fahrenheit.
        main.sea_level Atmospheric pressure on the sea level, hPa
        main.grnd_level Atmospheric pressure on the ground level, hPa
    wind
        wind.speed Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
        wind.deg Wind direction, degrees (meteorological)
    clouds
        clouds.all Cloudiness, %
    rain
        rain.3h Rain volume for the last 3 hours
    snow
        snow.3h Snow volume for the last 3 hours
    dt Time of data calculation, unix, UTC
    sys
        sys.type Internal parameter
        sys.id Internal parameter
        sys.message Internal parameter
        sys.country Country code (GB, JP etc.)
        sys.sunrise Sunrise time, unix, UTC
        sys.sunset Sunset time, unix, UTC
    id City ID
    name City name
    cod Internal parameter
    """
    mData = {}
    # http://erikflowers.github.io/weather-icons/
    # $pi.openweathermap.org/data/2.5/weather?q={city name}
    # api.openweathermap.org/data/2.5/weather?q={city name},{country code}
    def __init__(self, data):
        self.mConfig = None
        self.mDateformat = "%A %d %B"
        self.data = data

    @property
    def config(self):
        if self.mConfig is None:
            with open('config.json') as f:
                self.mConfig = json.load(f)
        return self.mConfig

    @property
    def unit(self):
        return self.config["unit"]

    @property
    def datetime(self):
        """Current Date + time"""
        return unicode(time.strftime("%a %d %B") + "  " + time.strftime("%H:%M"), 'UTF-8').title()

    @property
    def dateformat (self):
        return self.mDateformat

    @dateformat.setter
    def dateformat(self, value):
        self.mDateFormat = value

    @property
    def date(self):
        """Current Date"""
        return self.getdate(self.dateformat)

    def getdate(self, format="%A %d %B"):
        """Current Date"""
        return unicode(time.strftime(format), 'UTF-8').title()

    @property
    def time(self):
        """Current Date"""
        return time.strftime("%H:%M")

    @property
    def data(self):
        return self.mData

    @data.setter
    def data(self, value):
        self.mData = value

    @property
    def longitude(self):
        """ City geo location, longitude """
        return self.data["coord"]["lon"]

    @property
    def latitude(self):
        """ City geo location, latitude """
        return self.data["coord"]["lat"]

    @property
    def weather(self):
        return self.data["weather"]

    @property
    def icon(self):
        return "res/drawable/{0}.png".format(self.data["weather"][0]["icon"])
        # return "http://openweathermap.org/img/w/{0}.png".format(self.Data["weather"][0]["icon"])

    @property
    def description(self):
        #return unicode(R.values[str(self.data["weather"][0]["id"])].title())
        return unicode(R.strings.code[str(self.data["weather"][0]["id"])].title())

    @property
    def base(self):
        """ Internal parameter """
        return self.data["base"]

    @property
    def temperature(self):
        """ Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."""
        return int(self.data["main"]["temp"])

    @property
    def temperatureunit(self):
        """ Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."""
        degree_sign = u'\N{DEGREE SIGN}'
        return degree_sign + 'C' if self.unit == "metric" else degree_sign + 'F'

    @property
    def pressure(self):
        """  Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data),
        hPa """
        return self.data["main"]["pressure"]

    @property
    def pressureunit(self):
        return "hPa"

    @property
    def humidity(self):
        """ Humidity, %  """
        return self.data["main"]["humidity"]

    @property
    def mintemperature(self):
        """ Minimum temperature at the moment. This is deviation from current temp that is possible
        for large cities and megalopolises geographically expanded (use these parameter optionally).
        Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit. """
        return int(self.data["main"]["temp_min"])

    @property
    def maxtemperature(self):
        """ Maximum temperature at the moment. This is deviation from current temp that is possible
        for large cities and megalopolises geographically expanded (use these parameter optionally).
        Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit. """
        return int(self.data["main"]["temp_max"])

    @property
    def sea_level(self):
        """ Atmospheric pressure on the sea level, hPa """
        if "sea_level" in self.data["main"]:
            return self.data["main"]["sea_level"]
        return None

    @property
    def ground_level(self):
        """ Atmospheric pressure on the ground level, hPa """
        if "grnd_level" in self.data["main"]:
            return self.data["main"]["grnd_level"]
        return None

    @property
    def windspeed(self):
        """ Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour. """
        return self.data["wind"]["speed"]

    @property
    def windspeedunit(self):
        return "m/s" if self.unit == "metric" else "mi/h"

    @property
    def winddegrees(self):
        """ Wind direction, degrees (meteorological). """
        if "deg" in self.data["wind"]:
            return int(self.data["wind"]["deg"])
        return 0

    @property
    def winddegreesdescription(self):
        """ Wind direction, degrees (meteorological). """
        if "deg" in self.data["wind"]:
            direction = [" N ", "NNE", "NE ", "ENE", " E ", "ESE", "SE ", "SSE", " S ", "SSW", "SW ", "WSW",
                         " W ", "WNW", "NW ", "NNW", " N "]
            winddir = self.data["wind"]["deg"]
            compassdir = int(round((math.fmod(winddir, 360)) / 22.5, 0) + 1)
            # return direction[compassdir]
            if compassdir >= len(direction):
                compassdir = 16
            return direction[compassdir]
        return "N"

    @property
    def cloudiness(self):
        """ Cloudiness, % """
        return self.data["clouds"]["all"]

    @property
    def rain(self):
        """ Rain volume for the last 3 hours """
        if "rain" in self.data:
            return self.data["rain"]["3h"]
        return None

    @property
    def snow(self):
        """ Snow volume for the last 3 hours """
        if "snow" in self.data:
            return self.data["snow"]["3h"]
        return None

    @property
    def dt(self):
        """  Time of data calculation, unix, UTC """
        return self.data["dt"]

    def getdt(self, format="%a %d %B %H:%M"):
        """  Time of data calculation, unix, UTC """
        return R.strings.translate(unicode(datetime.fromtimestamp(self.data["dt"]).strftime(format)).title())

    @property
    def country(self):
        """  Country code (GB, JP etc.) """
        return self.data["sys"]["country"]

    @property
    def sunrise(self, format="%H:%M"):
        """  Sunrise time, unix, UTC """
        stime = time.gmtime(int(self.data["sys"]["sunrise"]))
        return unicode(time.strftime(format, stime), 'UTF-8')

    @property
    def sunset(self, format="%H:%M"):
        """ Sunset time, unix, UTC """
        stime = time.gmtime(int(self.data["sys"]["sunset"]))
        return unicode(time.strftime(format, stime), 'UTF-8')

    @property
    def cityid(self):
        """  City ID """
        return self.data["id"]

    @property
    def cityname(self):
        """  City name """
        if "name" in self.data:
            return self.data["name"].title()
        return None
