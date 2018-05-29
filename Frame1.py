from layout.Form import Form
from layout.Icon import Icon
from layout.Label import Label
from layout.Line import Line

class Frame1(Form):

    def __init__(self, weather):
        Form.__init__(self, "Frame1", 640, 384)
        degree_sign = u'\N{DEGREE SIGN}'
        icon_direction = Icon("iconDirection", 'res/Direction-West-icon.png')
        icon_direction.rotate(weather.winddegrees)
        self.add(Icon("iconCondition", "res/01d.png"))
        self.add(icon_direction)
        self.add(Label("labelDate", weather.date))
        self.add(Label("labelDescription", weather.description))
        self.add(Label("labelSunrise", weather.sunrise))
        self.add(Label("labelSunset", weather.sunset))
        self.add(Label("labelCity", weather.cityname))
        self.add(Icon("iconSunrise", 'images/Sunrise.png'))
        self.add(Icon("iconSunset", 'images/Sunset.png'))
        self.add(Label("labelTemperature", str(weather.temperature) + weather.temperatureunit))
        self.add(Label("labelMinTemperature", str(weather.min_temperature) + weather.temperatureunit))
        self.add(Label("labelMaxTemperature", str(weather.max_temperature) + weather.temperatureunit))
        self.add(Label("labelTime", weather.time))
        self.add(Label("labelHumidity", "Humidity"))
        self.add(Label("labelHumidityValue", str(weather.humidity) + '%'))
        self.add(Label("labelPressure", "Pressure"))
        self.add(Label("labelPressureValue", "{0}{1}".format(weather.pressure, weather.pressure_unit)))
        self.add(Label("labelDegress", weather.winddegreesdescription))
        self.add(Label("labelSpeed", "{0}{1}".format(weather.wind_speed, weather.wind_speed_unit)))
        # separator line
        self.add(Line("LineSeparator"))
        # top line
        self.add(Line("LineTop"))
        # bottom line
        self.add(Line("LineBottom"))