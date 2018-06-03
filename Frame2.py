from layout.Form import Form
from model import Weather


class Frame2(Form):

    def __init__(self, forecastfive):
        weather = Weather(forecastfive.list[0])
        Form.__init__(self, "Frame2", 640, 384)
        self.children["labelCity"].text = forecastfive.city["name"]
        self.children["labelDay"].text = weather.date
        self.children["iconCondition"].file = weather.icon
        self.children["labelTemperature"].text = str(weather.temperature) + weather.temperatureunit
        self.children["labelHumidity"].text ="Humidity: {0}%".format(weather.humidity)
        self.children["labelPressure"].text ="Pressure: {0}{1} ".format(weather.pressure, weather.pressureunit)
        self.children["labelWind"].text ="Wind: {0} {1} ".format(weather.windspeed, weather.windspeedunit)
        self.createview()
