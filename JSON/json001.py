# -*- coding: utf-8 -*-
import requests
#payload = {'name': 'Anthony', 'job':'Programmer'}
payload =    {
    "id": 1,
    "firstName": "patrick geraldo",
    "lastName": "Kent",
    "job": "Reporter",
    "roll": 20
  }



r = requests.put('http://localhost:3000/person/1', json=payload)

#r = requests.post('https://reqres.in/api/users', json=payload)


print(r.text)