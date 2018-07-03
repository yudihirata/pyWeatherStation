# pyWeatherStation

The pyWeatherStationis an e-ink weather station written in Python. 
<br />
<br />
<img align="right" width="192" height="320" src="https://raw.githubusercontent.com/yudihirata/weatherstation/master/doc/portrait1.bmp">
It uses Accuweather API to fetch the weather Information.
  - Current condition
  - 5 Days of Daily Forecasts
  - 12 Hours of Hourly Forecasts

###  Images and open source fonts
  - The open source icons of [http://weathericons.io](http://weathericons.io) for weather symbols
  - The FreeMonoBold.ttf font can be retrieved everywhere on the internet as here on [gnu-freefont_freemono](http://weathericons.io)
<br />
<br />
<br />
<br />
<img align="right" width="192" height="320" src="https://raw.githubusercontent.com/yudihirata/weatherstation/master/doc/portrait2.bmp">

### Hardware requirements
Your weather station should meet or exceed these hardware requirements:
- Raspberry pi
- [Waveshare 7.5inch E-Ink display HAT for Raspberry Pi](https://www.waveshare.com/product/modules/oleds-lcds/e-paper/7.5inch-e-paper-hat.htm)
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<img align="right" width="192" height="320" src="https://raw.githubusercontent.com/yudihirata/weatherstation/master/doc/portrait3.bmp">

### Prerequisites
pyWeatherStation requires [Python libraries for Waveshare e-paper series](https://github.com/soonuse/epd-library-python)  to run. 
Before you download the source code, unsure your system meets the following requirements. 
-  OS: Raspbian
-  [Pillow](https://pypi.org/project/Pillow/2.2.1/) (Python Imaging Library)
-  [Matplotlib](https://matplotlib.org/)
-  [Accuweather](https://developer.accuweather.com/) API Key(the Limited Trial is enough)

### Installation
 Pyllow
 Run the following:
```sh
$ sudo apt-get build-dep python-imaging
$ sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev
$ sudo pip install Pillow
```
Matplotlib
It is easiest to use your system package manager to install the dependencies.
If you are on Debian/Ubuntu, you can get all the dependencies required to build 

```sh
$ sudo apt-get build-dep python-matplotlib
```

### Configure
In order to use Accuweather APIs, you’ll need to Register at developer.accuweather.com and get limited 
free access to a sampling of AccuWeather API endpoints, including Locations, Current Conditions, 
and Daily and Hourly Forecasts.

Before you run it, you must change the following settings:
-  orientation: portrait or landscape
-  city: your city
-  api_key: your previously registered API key

```json
{
  "language":"default",
  "unit":"metric",
  "orientation":"portrait",
  "width":640,
  "height":384,
  "accuweather":{
    "city":"barueri",
    "api_key":"paste here Secret API Key from your Accuweather account",
    "unit":"metric",
    "current":"http://dataservice.accuweather.com/currentconditions/v1",
    "forecastfive":"http://dataservice.accuweather.com/forecasts/v1/daily/5day",
    "twelvehours":"http://dataservice.accuweather.com/forecasts/v1/hourly/12hour",
    "citysearch":"http://dataservice.accuweather.com/locations/v1/cities/search",
    "language":"en-us"
  }
}
```


### Run
```sh
$ cd pyWeatherStation
$ python wseinkd.py start
```