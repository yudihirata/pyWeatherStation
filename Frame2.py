from datetime import datetime

import R
from layout.Form import Form
from model import Weather
import pytz


class Frame2(Form):

    def __init__(self, accuweather):

        Form.__init__(self, "Frame2")
        city = accuweather.city
        weather = accuweather.get_current()
        forecast = accuweather.get_dailyforecast(0)
        self.children["labelCity"].text = city.localizedname
        self.children["labelDate"].text = weather.date
        self.children["labelDescription"].text = weather.description
        self.children["iconCondition"].file = weather.icon
        self.children["labelUV"].text = u"{0}:{1}".format(R.strings.INDEX_UV, weather.uv_index)
        self.children["labelHoursOfSun"].text = u"{0}:{1}".format(R.strings.HOURS_OF_SUN, forecast.hours_of_sun)
        self.children["labelTemperature"].text = str(weather.temperature) + weather.temperatureunit
        self.children["labelHumidity"].text = "{0}:{1}%".format(R.strings.HUMIDITY, weather.humidity)
        self.children["labelPressure"].text = u"{0}:{1}{2} ".format(R.strings.PRESSURE, weather.pressure,
                                                                    weather.pressureunit)
        self.children["labelWind"].text = "{0}:{1}".format(R.strings.WIND, weather.swind)
        self.children["labelLastUpdated"].text = u"{0}:{1} ".format(R.strings.LAST_UPDATED,
                                                                    weather.get_date("%m/%d %H:%M"))
        accuweather.createchart("forecast.png")

        self.children["iconChart"].file = "forecast.png"

        for i in range(0, accuweather.forecasts.size):
            forecast = accuweather.get_dailyforecast(i)
            self.children["label{0}".format(i+1)].text = forecast.get_date("%a")
            temp = u"{0:.0f}\N{DEGREE SIGN}/"u"{1:.0f}\N{DEGREE SIGN}".format(forecast.min_temperature,
                                                                              forecast.max_temperature)
            # Forces the field to be centered within the available space.
            self.children["label{0}minmax".format(i+1)].text = u"{:^9}".format(temp)
            self.children["iconCondition{0}".format(i+1)].file = forecast.day.icon
        self.create_view()
