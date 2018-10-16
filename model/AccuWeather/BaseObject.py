import time

from R import R


class BaseObject(object):

    def __init__(self, data):
        self.mDateformat = "%A %d %B"
        self.mData = data

    @property
    def data(self):
        return self.mData

    @data.setter
    def data(self, data):
        self.mData = data

    @property
    def datetime(self):
        """Current Date + time"""
        return unicode(time.strftime("%a %d %B") + "  " + time.strftime("%H:%M"), 'UTF-8').title()

    @property
    def dateformat(self):
        return self.mDateformat

    @dateformat.setter
    def dateformat(self, value):
        self.mDateFormat = value

    @property
    def date(self):
        """Current Date"""
        return self.get_date(self.dateformat)

    def get_date(self, format="%A %d %B"):
        """Current Date"""
        return unicode(time.strftime(format), 'UTF-8').title()

    @property
    def time(self):
        """Current Date"""
        return time.strftime("%H:%M")

    @property
    def unit(self):
        return R.config.ACCUWEATHER["unit"].title()
