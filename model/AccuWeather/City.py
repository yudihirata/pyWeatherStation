import json
import os
import urllib2

import R
from model.AccuWeather import BaseObject


class City(BaseObject):
    def __init__(self, data):
        super(City, self).__init__(data)

    @property
    def key(self):
        return self.data["Key"]

    @property
    def localizedname(self):
        return self.data["LocalizedName"]

    @property
    def region(self):
        return self.data["Region"]

    @property
    def country(self):
        return self.data["Country"]

    @property
    def administrativearea(self):
        return self.data["AdministrativeArea"]

    @property
    def timezone(self):
        return self.data["TimeZone"]

    @property
    def geoposition(self):
        return self.data["GeoPosition"]

    @property
    def parentcity(self):
        return self.data["ParentCity"]

    @property
    def supplementaladminareas(self):
        return self.data["SupplementalAdminAreas"]

    @property
    def datasets(self):
        return self.data["DataSets"]

    @property
    def details(self):
        return self.data["Details"]

