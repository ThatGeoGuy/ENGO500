import sys
request = open('D:\Temporary\DBtest01.json').read()

import httplib
# use httplib2...
"""
webservice = httplib.HTTP('demo.student.geocens.ca:8080')
webservice.putrequest("POST", "/SensorThings_V1.0/Things")
webservice.putheader("Host", "demo.student.geocens.ca:8080")
webservice.putheader("User-Agent", "Python turbocat post")
webservice.putheader("Content-type", "application/json")
webservice.putheader("Content-length", "%d" % len(request))
webservice.endheaders()
statuscode, statusmessage, header = webservice.getreply()
print statuscode, statusmessage, header
"""


connection = httplib.HTTPConnection("demo.student.geocens.ca:8080")
connection.request("POST", "/SensorThings_V1.0/Things")
result = connection.getresponse()
print result.status, result.reason

 
