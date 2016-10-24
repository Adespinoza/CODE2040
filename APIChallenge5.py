import requests
import json
#import iso8601
import datetime 
from datetime import timedelta 

#Set variables from web URLs 
web = 'http://challenge.code2040.org/api/dating'
validationWeb = 'http://challenge.code2040.org/api/dating/validate'

dateObject = requests.post(web, json={'token':'af9b409be63eedf2b016a42e76ad2253'})
dateObject = dateObject.json()

#Initialize variables from dateObject 
dateStamp = dateObject['datestamp']
intervalToAdd = dateObject['interval']

#Convert interval to add in to seconds 
intervalToAdd = timedelta(seconds=intervalToAdd)

#Converts string into the form, looked up form 
timePeriod = datetime.datetime.strptime(dateStamp, '%Y-%m-%dT%H:%M:%SZ')

#Add two times together 
totalTime = timePeriod + intervalToAdd

#Convert back time period given
totalTime = totalTime.strftime('%Y-%m-%dT%H:%M:%SZ')

#Send requests post
r = requests.post(validationWeb, json= {'token':'af9b409be63eedf2b016a42e76ad2253', 'datestamp': totalTime})