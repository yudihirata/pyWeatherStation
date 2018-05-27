from layout.Form import Form
from layout.Icon import Icon
from layout.Label import Label
from weathercurrent import WeatherCurrent

class Frame1(Form):

    def __init__(self, weather):
        Form.__init__(self, "Frame1", 640, 384 )
        degree_sign = u'\N{DEGREE SIGN}'
        icon_direction = Icon("iconDirection", 'res/Direction-West-icon.png')
        icon_direction.rotate(weather.wind_degrees)
        self.add(Icon("iconCondition", "res/01d.png"))
        self.add(icon_direction)
        self.add(Label("labelDate", weather.date))
        self.add(Label("labelDescription", weather.description))
        self.add(Label("labelSunrise", weather.sunrise))
        self.add(Label("labelSunset", weather.sunset))
        self.add(Label("labelCity", weather.city_name))
        self.add(Icon("iconSunrise", 'images/Sunrise.png'))
        self.add(Icon("iconSunset", 'images/Sunset.png'))
        self.add(Label("labelTemperature", str(weather.temperature) + degree_sign + 'c'))
        self.add(Label("labelMinTemperature",str(weather.min_temperature) + degree_sign + 'c'))
        self.add(Label("labelMaxTemperature",str(weather.max_temperature) + degree_sign + 'c'))
        self.add(Label("labelTime", weather.time))
        self.add(Label("labelHumidity", "Humidity"))
        self.add(Label("labelHumidityValue", str(weather.humidity) + '%'))
        self.add(Label("labelPressure", "Pressure"))
        self.add(Label("labelPressureValue", "{0}{1}".format(weather.pressure, weather.pressure_unit)))
        self.add(Label("labelDegress", weather.wind_degrees_description))
        self.add(Label("labelSpeed", "{0}{1}".format(weather.wind_speed, weather.wind_speed_unit)))
        # separator line
        self.draw.line((100, 0, 100, 110), fill=0, width=3)
        #top line
        self.draw.line((0, 110, 640, 110), fill=0, width=3)
        # bottom line
        self.draw.line((180, 165, 260, 165), fill=0, width=3)

