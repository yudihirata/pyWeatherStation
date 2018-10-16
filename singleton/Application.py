import time
#import epd7in5
from PIL import Image
from Frame1 import Frame1
from Frame2 import Frame2
from Frame3 import Frame3
from daemon import Daemon
from presenter import AccuWeather


class Application(Daemon):
    def run(self):
        accuweather = AccuWeather()
        epd = epd7in5.EPD()
        epd.init()
        while True:
            frame1 = Frame1(accuweather)
            frame1.save('frame1.bmp')

            frame2 = Frame2(accuweather)
            frame2.save('frame2.bmp')

            frame3 = Frame3(accuweather)
            frame3.save('frame3.bmp')

            image = Image.open('frame1.bmp')
            buffer = epd.get_frame_buffer(image)

            image2 = Image.open('frame2.bmp')
            buffer2 = epd.get_frame_buffer(image2)

            image3 = Image.open('frame3.bmp')
            buffer3 = epd.get_frame_buffer(image3)

            for x in range(60):
                epd.display_frame(buffer)
                time.sleep(60)
                epd.display_frame(buffer2)
                time.sleep(60)
                epd.display_frame(buffer3)
                time.sleep(60)
            accuweather.refresh()