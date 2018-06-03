#https://openweathermap.org/forecast5

class ForecastFive(object):

    def __init__(self, data):
        self.mData = data

    @property
    def data(self):
        return self.mData

    @property
    def code(self):
        return self.data["code"]

    @property
    def message(self):
        return self.data["message"]

    @property
    def city(self):
        return self.data["city"]

    @property
    def list(self):
        return self.data["list"]

    @property
    def count(self):
        """
        :return Number of lines returned by this API call:
        """
        return self.data["cnt"]

