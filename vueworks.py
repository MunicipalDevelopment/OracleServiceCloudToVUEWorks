import ConfigParser
import requests
import json
import re

class VUEWorks(object):
    """A class for handling the VUEWorks API. Currently accepts no Params. Hardcoded to Project Albuquerque NM for the Service Request Module. May be extended in the future."""

    def __init__(self):
        """Return a VW object with login credential and project populated."""
        defaults = ConfigParser.RawConfigParser()
        defaults.read('configfile.txt')
        self.key = defaults.get('VWSecurity', 'pass')
        self.get = defaults.get('VWURLS', 'get')
        self.create = defaults.get('VWURLS', 'create')
        self.projectName = "Albuquerque NM"


    def checkVUEWorks(self,refid):
        """Check if a referenceID is already in VUEWorks. If exists, returns True and data. Else, returns False and NONE"""
        response = requests.post(self.get,data={"AppAuthKey":self.key,"ProjectName":self.projectName,"RefReportID":refid})
        if "Incident_ID" in response.text:
            return {"in":True,"data":response.text}
        else:
            return {"in":False,"data":"None"}



    def createSR(self,rid,lat,lng):
        """Creates a Service Requests and returns string. Returns ID - internal ID to be used with GetRequestDataByID endpoint."""
        srequest = requests.post(self.create,data={"AppAuthKey":self.key,"ProjectName":self.projectName,"RefReportID":rid,"IssueID":"43","Description":"TEST BY PAUL","FirstName":"Paul","LastName":"Crickard","Email":"pcrickard@cabq.gov","Phone":"505-366-4020","Latitude":lat,"Longitude":lng,"Location":"Paul St"})
        theID = re.search('<ID>(.+?)</ID>',srequest.text)
        if theID:
            return theID.group(1)
        else:
            return srequest.text #shouldnt be able to error. But might as well make sure.
