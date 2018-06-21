from model.AccuWeather import BaseObject
from model.AccuWeather.DailyForecast import DailyForecast


class Forecasts(BaseObject):

    def __init__(self, data):
        super(Forecasts, self).__init__(data)

    @property
    def headline(self):
        return self.data["Headline"]


    def get_dailyforecasts(self, day):
        """
        :return: DailyForecast
        """
        return DailyForecast(self.data["DailyForecasts"][day])
