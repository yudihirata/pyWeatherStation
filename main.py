# -*- coding: utf-8 -*-
# Waveshare 2,7inch SPI ePaper display
#

from PIL import Image
#import epd7in5
from Frame1 import Frame1
from weathercurrent import WeatherCurrent

def main():
    current = WeatherCurrent("Barueri")
    frame1 = Frame1(current)
    frame1.oncreateview()
    frame1.save('frame1.bmp')
    image = Image.open('frame1.bmp')
 #   epd = epd7in5.EPD()
 #   epd.init()
 #   epd.display_frame(epd.get_frame_buffer(image))


if __name__ == "__main__":
    main()


