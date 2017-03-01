import ConfigParser
import requests
import json


class Oracle(object):
    """A class for handling the Oracle Service Cloud API. Currently accepts no Params. May be extended in the future."""

    def __init__(self):
        """Return an Oracle object with login credential and JSON of incidents for DMD."""
        defaults = ConfigParser.RawConfigParser()
        defaults.read('configfile.txt')
        self.key = defaults.get('OracleSecurity', 'pass')
        self.user = defaults.get('OracleSecurity', 'user')
        self.incidentURLbase = defaults.get('OracleURLS','incidentURL')
        self.queryURL = defaults.get('OracleURLS','queryURL')
        self.getCountData = requests.get(self.queryURL,auth=(self.user,self.key)).text
        self.countData = json.loads(self.getCountData)
        self.totalURL = self.queryURL + "&limit=" + str(self.countData["totalResults"])
        self.totalIncidents = requests.get(self.totalURL,auth=(self.user,self.key)).text
        self.incidents = json.loads(self.totalIncidents)

    def getIncidentData(self,refid):
        iurl=self.incidentURLbase+str(refid)
        incidentresponse = requests.get(iurl,auth=(self.user,self.key)).text
        fields=json.loads(incidentresponse)
        return fields

