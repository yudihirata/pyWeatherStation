# -*- coding: utf-8 -*-
# Waveshare 2,7inch SPI ePaper display
#

from PIL import Image
#import epd7in5
import R
from Frame1 import Frame1
from Frame2 import Frame2
from model import ForecastFive
from model.AccuWeather import City
from model.Weather import Weather
from presenter import OpenWeatherMap
from presenter.AccuWeather import AccuWeather


def main():
    R.init()
    accuweather = AccuWeather()
    # print "{0}".format(accuweather.city.datetime);
    # current = accuweather.getcurrent()
    # print "{0}".format(current.icon);

 #    presenter = OpenWeatherMap()
 #    #epd = epd7in5.EPD()
 #    #epd.init()
 #    current = Weather(presenter.getcurrent())
    frame1 = Frame1(accuweather)
    frame1.save('frame1.bmp')
 #
 #    forecast = ForecastFive(presenter.getforecastfive())
 #    frame2 = Frame2(current, forecast)
 #    frame2.save('frame2.bmp')
 #
 #    image = Image.open('frame1.bmp')
 # #   buffer = epd.get_frame_buffer(image)
 #    image2 = Image.open('frame2.bmp')
 #  #  buffer2 = epd.get_frame_buffer(image2)
 #   # epd.display_frame(buffer)
 #    #epd.display_frame(buffer2)


if __name__ == "__main__":
    main()


