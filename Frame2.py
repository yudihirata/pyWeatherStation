from layout.Form import Form
from model import Weather
import R


class Frame2(Form):

    def __init__(self, forecastfive):
        weather = Weather(forecastfive.list[0])
        Form.__init__(self, "Frame2")
        self.children["labelCity"].text = forecastfive.city["name"]
        self.children["labelDay"].text = weather.date
        self.children["iconCondition"].file = weather.icon
        self.children["labelTemperature"].text = str(weather.temperature) + weather.temperatureunit
        self.children["labelHumidity"].text = "{0}: {1}%".format(R.strings.HUMIDITY, weather.humidity)
        self.children["labelPressure"].text = "{0}: {1}{2} ".format(R.strings.PRESSURE, weather.pressure,
                                                                    weather.pressureunit)
        self.children["labelWind"].text = "{0}: {1} {2} ".format(R.strings.WIND, weather.windspeed,
                                                                 weather.windspeedunit)
        forecastfive.createchart("forecast.png")
        self.children["iconChart"].file  = "forecast.png"

        self.createview()
