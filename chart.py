import json
import numpy
import urllib2

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
def main():


    url = "http://api.openweathermap.org/data/2.5/forecast?q=barueri&units=metric&mode=json&appid=1497c0f0e51ef524d3be4fc373d72bd1"
    data= json.load(urllib2.urlopen(url))
    count =1
    x2=[]
    y2=[]
    for value in data["list"]:
        y2.append(value["main"]["temp"])
        x2.append(count)
        count = count +1


    #plt.subplot(5, 1, 2)
    #plt.plot(x2, y2, '.-')
    #plt.axis("off")
   # plt.fill()
   # plt.savefig("test.png")

    x = np.arange(data["cnt"])
    plt.axis("off")
    plt.bar(x, y2, color="black")
    plt.xticks(x, x2)
    plt.savefig("test.png", bbox_inches='tight', orientation="landscape",transparent=True, frameon=True )


if __name__ == "__main__":
    main()
