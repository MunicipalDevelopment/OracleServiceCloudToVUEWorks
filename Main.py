import oracle as o
import vueworks as vw

v=vw.VUEWorks()
O=o.Oracle()

for x in O.incidents['items']:
    invw = v.checkVUEWorks(x['id'])
    if invw['in']:
        incident = O.getIncidentData(x['id'])
        if incident["customFields"]["c"]["latitude"] is not None and incident["customFields"]["c"]["longitude"] is not None:
            result = v.createSR(x['id'],incident["customFields"]["c"]["latitude"],incident["customFields"]["c"]["longitude"])
            print "created Service Request: " + result
    else:
        print "In VUEWorks already"
