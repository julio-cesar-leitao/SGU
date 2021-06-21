# -*- coding: utf-8 -*-
import requests
#payload = {'name': 'Anthony', 'job':'Programmer'}

import cv2
import base64

img = cv2.imread('./public/img300x250.jpeg')
encoded_string = base64.b64encode(img).decode('utf-8')

payload =          {
           "time": "13:44:33",
           "temp": "40",
           "mascara": "sim",
           "img": "imgnova4"
       }



r = requests.put('http://localhost:3000/eventos/1', json=payload)
