from layout.Form import Form


class Frame1(Form):

    def __init__(self, weather):
        Form.__init__(self, "Frame1", 640, 384)
        icon_direction = self.children["iconDirection"]
        icon_direction.angle = weather.winddegrees
        self.children["iconCondition"].file = weather.icon
        self.children["labelDate"].text = weather.date
        self.children["labelDescription"].text = weather.description
        self.children["labelSunrise"].text = weather.sunrise
        self.children["labelSunset"].text = weather.sunset
        self.children["labelCity"].text = weather.cityname
        self.children["labelTemperature"].text = str(weather.temperature) + weather.temperatureunit
        self.children["labelMinTemperature"].text = str(weather.min_temperature) + weather.temperatureunit
        self.children["labelMaxTemperature"].text = str(weather.max_temperature) + weather.temperatureunit
        self.children["labelHumidityValue"].text = str(weather.humidity) + '%'
        self.children["labelPressureValue"].text = "{0}{1}".format(weather.pressure, weather.pressureunit)
        self.children["labelDirection"].text = weather.winddegreesdescription
        self.children["labelDegress"].text = str(weather.winddegrees) + u"\N{DEGREE SIGN}"
        self.children["labelSpeed"].text = "{0}{1}".format(weather.windspeed, weather.windspeedunit)
        self.createview()