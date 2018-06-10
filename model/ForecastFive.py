#https://openweathermap.org/forecast5
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class ForecastFive(object):

    def __init__(self, data):
        self.mData = data

    @property
    def data(self):
        return self.mData

    @property
    def code(self):
        return self.data["code"]

    @property
    def message(self):
        return self.data["message"]

    @property
    def city(self):
        return self.data["city"]

    @property
    def list(self):
        return self.data["list"]

    @property
    def count(self):
        """
        :return Number of lines returned by this API call:
        """
        return self.data["cnt"]

    def createchart(self, filename):
        x2 = []
        tmax = []
        tmin = []
        count =1
        for value in self.list:
            tmax.append(value["main"]["temp_max"])
            tmin.append(value["main"]["temp_min"])
            x2.append(count)
            count = count + 1
        plt.bar(x2, tmax, color="black")
        plt.bar(x2, tmin, color="gray")
        plt.axis("off")
        plt.savefig(filename, bbox_inches='tight', orientation="landscape", transparent=True, frameon=False, dpi=300)