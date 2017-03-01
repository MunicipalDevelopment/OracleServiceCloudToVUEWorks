# Oracle Service Cloud To VUEWorks
Move data from Oracle Service Cloud to Service Requests in VUEWorks. Contains Classes for Oracle and VUEWorks which could be used for other integrations or applications.
# How to Use Oracle to VUEWorks

### VUEWorks
Creates a VUEWorks object that can query and create Service Requests.
```python
>>> import vueworks as vw
>>> v=vw.VUEWorks()
>>> invw = v.checkVUEWorks(345492)
>>> invw['in']
True
>>> invw['data']
u'<?xml version="1.0" encoding="utf-8"?>\r\n<string xmlns="http://www.vueworks.c
om/webservices/">&lt;Results&gt;&lt;Data&gt;&lt;Table0&gt;&lt;Incident_ID&gt;277
8&lt;/Incident_ID&gt;&lt;Asset_Type_Code&gt;&lt;/Asset_Type_Code&gt;&lt;LinkedLa
yer_ID&gt;&lt;/LinkedLayer_ID&gt;&lt;LinkedAsset_ID&gt;&lt;/LinkedAsset_ID&gt;&l
t;CreatedBy&gt;313&lt;/CreatedBy&gt;&lt;CustomerName&gt;&lt;/CustomerName&gt;&lt
;CustomerPhone&gt;&lt;/CustomerPhone&gt;&lt;Street&gt;UNIVERSITY BLVD NE|I40 WES
TBOUND NE|New Mexico|Albuquerque|87102</string>'

>>> notinvw = v.checkVUEWorks(34549222222222222)
>>> notinvw
{'data': 'None', 'in': False}

>>> sr=v.createSR(99,35,-106)
>>> sr
u'2781'
>>> int(sr)
2781
```
### Oracle
Initializes by grabbing all the incidents for DMD as JSON. Incidents have an ID that can be used to get data for each - getIncidentData().
```python
>>> import oracle as o
>>> O=o.Oracle()
>>> for x in O.incidents['items']:
...    print x['id']
346193
346124
345632

>>> incident = O.getIncidentData(346193)
>>> incident
{u'smartSenseStaff': None, u'links': [{u'href': 

>>> incident['customFields']['c']['latitude']
u'35.037293590652226'


```
