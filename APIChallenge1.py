import requests
import json

#Initialize varliables 
web = 'http://challenge.code2040.org/api/register'
token = 'af9b409be63eedf2b016a42e76ad2253'
registration = 'https://github.com/Adespinoza/CODE2040'

#Create a form object to pass to JSON
form = {'github': registration, 'token': token}

#Send request posts
req = requests.post(web, json=form)