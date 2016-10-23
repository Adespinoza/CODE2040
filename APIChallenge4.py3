import requests
import json

web = 'http://challenge.code2040.org/api/prefix'
validationWeb = 'http://challenge.code2040.org/api/prefix/validate'

prefixRequest = requests.post(web, json={'token':'af9b409be63eedf2b016a42e76ad2253'})
prefixRequest = prefixRequest.json()

#Parse the request object
thePrefix = prefixRequest['prefix']
fullArray = prefixRequest['array']

notPrefixArr = []

#Loop through the given array 
for i in range(0,len(fullArray)):
	if fullArray[i].startswith(thePrefix):		
		pass
	else :
		#Append into array of non-matching
		notPrefixArr.append(fullArray[i])

r = requests.post(validationWeb, json= {'token':'af9b409be63eedf2b016a42e76ad2253', 'array': notPrefixArr})