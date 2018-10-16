from datetime import datetime

from R import R
from layout.Form import Form
import pytz


class Frame3(Form):

    def __init__(self, accuweather):
        Form.__init__(self, "Frame3")
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
        self.children["labelMinTemperature"].text = u"{0}{1}".format(int(forecast.min_temperature),
                                                                     weather.temperatureunit)
        self.children["labelMaxTemperature"].text = u"{0}{1}".format(int(forecast.max_temperature),
                                                                     weather.temperatureunit)
        self.children["labelHumidity"].text = "{0}:{1}%".format(R.strings.HUMIDITY, weather.humidity)
        self.children["labelPressure"].text = u"{0}:{1}{2} ".format(R.strings.PRESSURE, weather.pressure,
                                                                    weather.pressureunit)
        self.children["labelWind"].text = "{0}:{1}".format(R.strings.WIND, weather.swind)
        self.children["labelLastUpdated"].text = u"{0}:{1} ".format(R.strings.LAST_UPDATED,
                                                                    weather.get_date("%m/%d %H:%M"))
        data = accuweather.twelve_hours
        for i in range(0, 5):
            hour = data[i]
            self.children["label{0}".format(i + 1)].text = datetime.fromtimestamp(hour["EpochDateTime"])\
                .strftime("%H:%M")
            self.children["label{0}Temp".format(i + 1)].text = u"{0}{1}{2}".format(int(hour["Temperature"]["Value"]),
                                                                                  hour["Temperature"]["Unit"],
                                                                                  u'\N{DEGREE SIGN}')
            self.children["label{0}RealFeel".format(i + 1)].text = u"{0}{1}{2}"\
                .format(int(hour["RealFeelTemperature"]["Value"]),hour["RealFeelTemperature"]["Unit"],
                        u'\N{DEGREE SIGN}')

            self.children["label{0}WindSpeed".format(i + 1)].text = "{0}{1}".format(int(hour["Wind"]["Speed"]["Value"]),
                                                                                     hour["Wind"]["Speed"]["Unit"])
            self.children["iconCondition{0}".format(i + 1)].file = "res/drawable/{0}.png".format(hour["WeatherIcon"])
        self.create_view()
