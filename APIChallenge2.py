import requests
import json

web = 'http://challenge.code2040.org/api/reverse'
validationWeb = 'http://challenge.code2040.org/api/reverse/validate'

#Initialize string received 
string = requests.post(web, data = {'token':'af9b409be63eedf2b016a42e76ad2253'})

# Reverse the string 
stringReversed = string.text[::-1]

#Send request to server
req = requests.post(validationWeb, data={'token': 'af9b409be63eedf2b016a42e76ad2253' , 'string' : stringReversed})

