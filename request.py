# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:51:19 2020

@author: Soham Ghosh
"""


import requests
url='http://localhost:8000/predict'
r=requests.post(url,json={})
