from datetime import datetime

import R
from layout.Form import Form
from model import Weather


class Frame2(Form):

    def __init__(self, forecastfive):
        weather = Weather(forecastfive.list[0])
        Form.__init__(self, "Frame2")
        self.children["labelCity"].text = forecastfive.city["name"]
        self.children["labelDate"].text = weather.date
        self.children["labelDescription"].text = weather.description
        self.children["iconCondition"].file = weather.icon
        self.children["labelOthers"].text = ""
        if weather.rain is not None:
            self.children["labelOthers"].text = u"{0}:{1:.2f} mm/hour".format(R.strings.RAIN, weather.rain)
        self.children["labelTemperature"].text = str(weather.temperature) + weather.temperatureunit
        self.children["labelHumidity"].text = "{0}:{1}%".format(R.strings.HUMIDITY, weather.humidity)
        self.children["labelPressure"].text = u"{0}:{1}{2} ".format(R.strings.PRESSURE, weather.pressure,
                                                                    weather.pressureunit)
        self.children["labelWind"].text = "{0}:{1} {2} ".format(R.strings.WIND, weather.windspeed,
                                                                weather.windspeedunit)
        self.children["labelLastUpdated"].text = u"{0}:{1} ".format(R.strings.LAST_UPDATED,
                                                                   weather.getdate("%m/%d %H:%M"))
        forecastfive.createchart("forecast.png")

        self.children["iconChart"].file = "forecast.png"
        availableicon = 5
        nextday = weather.getdate("%d")
        for data in forecastfive.list:
            day = datetime.fromtimestamp(data["dt"]).strftime('%d')
            if nextday != day:
                nextday = day
                weather = Weather(data)
                availableicon = availableicon - 1
                self.children["label{0}".format(5 - availableicon)].text = weather.getdt("%a")
                self.children["iconCondition{0}".format(5 - availableicon)].file = weather.icon
                temp = u"{0}\N{DEGREE SIGN}/"u"{1}\N{DEGREE SIGN}".format(weather.mintemperature,
                                                                          weather.maxtemperature)
                # Forces the field to be centered within the available space.
                self.children["label{0}minmax".format(5 - availableicon)].text = u"{:^9}".format(temp)
            if availableicon == 0:
                break
        self.createview()
