# -*- coding: utf-8 -*-
# Waveshare 2,7inch SPI ePaper display
#

from PIL import Image
#import epd7in5
from Frame1 import Frame1
from Frame2 import Frame2
from model import ForecastFive
from model.Weather import Weather
from presenter import OpenWeatherMap


def main():
    presenter = OpenWeatherMap()

    #current = Weather(presenter.getcurrent())
    #frame1 = Frame1(current)
    #frame1.save('frame1.bmp')

    forecast = ForecastFive(presenter.getforecastfive())
    frame2 = Frame2(forecast)
    frame2.save('frame2.bmp')

    image = Image.open('frame2.bmp')
 #   epd = epd7in5.EPD()
 #   epd.init()
 #   epd.display_frame(epd.get_frame_buffer(image))


if __name__ == "__main__":
    main()


