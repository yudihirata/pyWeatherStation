import os

from model.AccuWeather import BaseObject


class Day(BaseObject):
    def __init__(self, data):
        super(Day, self).__init__(data)
        self.mWind = None

    @property
    def icon(self):
        """"
        int32	Numeric value representing an icon that matches the forecast.
        """
        resource = "res/drawable/{0}.png".format(self.data["Icon"])
        if not os.path.isfile(resource):
            resource = "res/drawable/refresh.png"
        return resource

    @property
    def icon_phrase(self):
        """"
        string	Phrase description of the icon.
        """
        return self.data["IconPhrase"]

    @property
    def short_phrase(self):
        """"
        string	Phrase description of the forecast. (AccuWeather attempts to keep this phrase under 30 characters in
        length, but some languages/weather events may result in a phrase exceeding 30 characters.
        """
        return self.data["ShortPhrase"]

    @property
    def long_phrase(self):
        """"
        Phrase description of the forecast. (AccuWeather attempts to keep this phrase under 100 characters in length,
        but some languages/weather events may result in a phrase exceeding 100 characters.
        """
        return self.data["LongPhrase"]

    @property
    def precipitation_probability(self):
        """"
        int32 Percent representing the probability of precipitation. May be NULL.
        """
        return self.data["PrecipitationProbability"] if "PrecipitationProbability" in self.data else None

    @property
    def thunderstorm_probability(self):
        """"
        int32	Percent representing the probability of a thunderstorm. May be NULL.
        """
        return self.data["ThunderstormProbability"] if "ThunderstormProbability" in self.data else None

    @property
    def rain_probability(self):
        """"
        int32	Percent representing the probability of rain. May be NULL.
        """
        return self.data["RainProbability"] if "RainProbability" in self.data else None

    @property
    def snow_probability(self):
        """"
        int32	Percent representing the probability of snow. May be NULL.
        """
        return self.data["SnowProbability"] if "SnowProbability" in self.data else None

    @property
    def ice_probability(self):
        """"
        int32	Percent representing the probability of snow. May be NULL.
        """
        return self.data["IceProbability"] if "IceProbability" in self.data else None

    @property
    def wind(self):
        """"
        int32	Percent representing the probability of snow. May be NULL.
        """
        if "Wind" in self.data and "Speed" in self.data["Wind"]:
            return u"{0}{1}".format(self.data["Wind"]["Speed"]["Value"], self.data["Wind"]["Speed"]["Unit"])
        return ""