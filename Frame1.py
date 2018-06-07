import R
from layout.Form import Form


class Frame1(Form):

    def __init__(self, weather):
        Form.__init__(self, "Frame1")
        icon_direction = self.children["iconDirection"]
        icon_direction.angle = weather.winddegrees
        self.children["iconCondition"].file = weather.icon
        self.children["labelDate"].text = weather.date
        self.children["labelDescription"].text = weather.description
        self.children["labelSunrise"].text = weather.sunrise
        self.children["labelSunset"].text = weather.sunset
        self.children["labelCity"].text = weather.cityname
        self.children["labelTemperature"].text = str(weather.temperature) + weather.temperatureunit
        self.children["labelMinTemperature"].text = str(weather.mintemperature) + weather.temperatureunit
        self.children["labelMaxTemperature"].text = str(weather.maxtemperature) + weather.temperatureunit
        self.children["labelHumidity"].text = u"{0}:{1}%".format(R.strings.HUMIDITY, str(weather.humidity))
        self.children["labelPressure"].text = u"{0}:{1}{2}".format(R.strings.PRESSURE, weather.pressure,
                                                                   weather.pressureunit)
        # Forces the field to be centered within 4 spaces.
        self.children["labelDirection"].text = u"{:^4}".format(weather.winddegreesdescription)
        # Forces the field to be centered within 4 spaces.
        self.children["labelDegress"].text = u"{:^4}".format(str(weather.winddegrees) + u"\N{DEGREE SIGN}")
        self.children["labelSpeed"].text = "{0}:{1}{2}".format(R.strings.WIND, weather.windspeed, weather.windspeedunit)
        self.createview()
