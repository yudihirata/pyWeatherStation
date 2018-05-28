import json
import urllib2
# https://openweathermap.org/current
import time
import math
import tokens

# $pi.openweathermap.org/data/2.5/weather?q={city name}
# api.openweathermap.org/data/2.5/weather?q={city name},{country code}
SERVER = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "1497c0f0e51ef524d3be4fc373d72bd1"


class WeatherCurrent:
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
        main.temp_min Minimum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
        main.temp_max Maximum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
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
    # https://openweathermap.org/weather-conditions
    mConditionCodes = {200: "thunderstorm with light rain",
                       201: "thunderstorm with rain",
                       202: "thunderstorm with heavy rain",
                       210: "light thunderstorm",
                       211: "thunderstorm",
                       212: "heavy thunderstorm",
                       221: "ragged thunderstorm",
                       230: "thunderstorm with light drizzle",
                       231: "thunderstorm with drizzle",
                       232: "thunderstorm with heavy drizzle",
                       300: "light intensity drizzle",
                       301: "drizzle",
                       302: "heavy intensity drizzle",
                       310: "light intensity drizzle rain",
                       311: "drizzle rain",
                       312: "heavy intensity drizzle rain",
                       313: "shower rain and drizzle",
                       314: "heavy shower rain and drizzle",
                       321: "shower drizzle",
                       500: "light rain",
                       501: "moderate rain",
                       502: "heavy intensity rain",
                       503: "very heavy rain",
                       504: "extreme rain",
                       511: "freezing rain",
                       520: "light intensity shower rain",
                       521: "shower rain",
                       522: "heavy intensity shower rain",
                       531: "ragged shower rain",
                       600: "light snow",
                       601: "snow",
                       602: "heavy snow",
                       611: "sleet",
                       612: "shower sleet",
                       615: "light rain and snow",
                       616: "rain and snow",
                       620: "light shower snow",
                       621: "shower snow",
                       622: "heavy shower snow",
                       701: "mist",
                       711: "smoke",
                       721: "haze",
                       731: "sand, dust whirls",
                       741: "fog",
                       751: "sand",
                       761: "dust",
                       762: "volcanic ash",
                       771: "squalls",
                       781: "tornado",
                       800: "clear sky",
                       801: "few clouds",
                       802: "scattered clouds",
                       803: "broken clouds",
                       804: "overcast clouds"
                       }

    def __init__(self, city, units="metric"):
        url = "{0}q={1}&units={2}&appid={3}".format(SERVER, city, units, API_KEY)
        self.data = json.load(urllib2.urlopen(url))

    @property
    def date_time(self):
        """Current Date + time"""
        return unicode(time.strftime("%a %d %B") + "  " + time.strftime("%H:%M"), 'UTF-8').title()

    @property
    def date(self):
        """Current Date"""
        return unicode(time.strftime("%a %d %B"), 'UTF-8').title()

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
        return "res/{0}.png".format(self.data["weather"][0]["icon"])
        # return "http://openweathermap.org/img/w/{0}.png".format(self.Data["weather"][0]["icon"])

    @property
    def description(self):
        return tokens.values[str(self.data["weather"][0]["id"])].title()

    @property
    def base(self):
        """ Internal parameter """
        return self.data["base"]

    @property
    def temperature(self):
        """ Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."""
        return int(self.data["main"]["temp"])

    @property
    def pressure(self):
        """  Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data),
        hPa """
        return self.data["main"]["pressure"]

    @property
    def pressure_unit(self):
        # TODO Dynamic unit
        return "hPa"

    @property
    def humidity(self):
        """ Humidity, %  """
        return self.data["main"]["humidity"]

    @property
    def min_temperature(self):
        """ Minimum temperature at the moment. This is deviation from current temp that is possible
        for large cities and megalopolises geographically expanded (use these parameter optionally).
        Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit. """
        return int(self.data["main"]["temp_min"])

    @property
    def max_temperature(self):
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
    def wind_speed(self):
        """ Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour. """
        return self.data["wind"]["speed"]

    @property
    def wind_speed_unit(self):
        # TODO
        return "m/s"

    @property
    def wind_degrees(self):
        """ Wind direction, degrees (meteorological). """
        if "deg" in self.data["wind"]:
            return int(self.data["wind"]["deg"])
        return 0

    @property
    def wind_degrees_description(self):
        """ Wind direction, degrees (meteorological). """
        if "deg" in self.data["wind"]:
            Direction = ["N  ", "NNE", " NE ", "ENE", "E  ", "ESE", "SE ", "SSE", "S  ", "SSW", "SW ", "WSW",
                         "W  ", "WNW", "NW ", "NNW", "N  "]
            WindDir = self.data["wind"]["deg"]
            CompassDir = int(round((math.fmod(WindDir, 360)) / 22.5, 0) + 1)
            return Direction[CompassDir]
        return "?"

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

    ##### SYS #####
    @property
    def country(self):
        """  Country code (GB, JP etc.) """
        return self.data["sys"]["country"]

    @property
    def sunrise(self):
        """  Sunrise time, unix, UTC """
        sTime = time.gmtime(int(self.data["sys"]["sunrise"]))
        return unicode(time.strftime("%H:%M", sTime), 'UTF-8')

    @property
    def sunset(self):
        """ Sunset time, unix, UTC """
        sTime = time.gmtime(int(self.data["sys"]["sunset"]))
        return unicode(time.strftime("%H:%M", sTime), 'UTF-8')

    ##### ID #####
    @property
    def city_id(self):
        """  City ID """
        return self.data["id"]

    ##### NAME #####
    @property
    def city_name(self):
        """  City name """
        if "name" in self.data:
            return self.data["name"].title()
        return None
