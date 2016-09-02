#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import variables


### Create the Spark Room ###
def createRoom():

    url = 'https://api.ciscospark.com/v1/rooms'
    payload = {
        'title': 'Department Team Room'
    }
    headers = {'content-type': 'application/json', 'authorization':'Bearer ' + variables.token}

    r = requests.post(url, data=json.dumps(payload), headers=headers)

### pulls out the roomID for adding person and message ###
def getRoomID():

    global roomID

    url = 'https://api.ciscospark.com/v1/rooms/'
    headers = {'content-type': 'application/json', 'authorization':'Bearer ' + variables.token}

    r = requests.get(url, headers=headers)

    roomID = r.text[17:93]

    return roomID


