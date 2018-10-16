# -*- coding: utf-8 -*-
import sys
from Frame1 import Frame1
from Frame2 import Frame2
from Frame3 import Frame3
from presenter.AccuWeather import AccuWeather
from R import R
from singleton.Application import Application


def main():
    accuweather = AccuWeather()
    frame1 = Frame1(accuweather)
    frame1.save('frame1.bmp')

    frame2 = Frame2(accuweather)
    frame2.save('frame2.bmp')

    frame3 = Frame3(accuweather)
    frame3.save('frame3.bmp')


if __name__ == "__main__":
    R.init()
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg in ('start', 'stop', 'restart'):
            d = Application('weather.pid', verbose=0)
            getattr(d, arg)()
