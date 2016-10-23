import requests
import json

web = 'http://challenge.code2040.org/api/haystack'
validationWeb = 'http://challenge.code2040.org/api/haystack/validate'

needleInHay = requests.post(web, json={'token':'af9b409be63eedf2b016a42e76ad2253'})

# .json() raises an exception 
needleInHay = needleInHay.json()

#Seperate the values into components 
theNeedle = needleInHay['needle']
theHaystack = needleInHay['haystack']

#Run through the list to find index
for x in range(0, len(theHaystack)):
	if theHaystack[x] == theNeedle:
		r = requests.post(validationWeb, json= {'token':'af9b409be63eedf2b016a42e76ad2253', 'needle': x})



		