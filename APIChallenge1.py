import requests
import json

web = 'http://challenge.code2040.org/api/register'
token = 'af9b409be63eedf2b016a42e76ad2253'
registration = 'https://github.com/Adespinoza/CODE2040'

form = {'github': registration, 'token': token}

req = requests.post(web, json=form)