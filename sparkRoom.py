#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import variables


### Create the Room ###
def createRoom():

    url = 'https://api.ciscospark.com/v1/rooms'
    payload = {
        'title': 'TEST ROOM2'
    }
    headers = {'content-type': 'application/json', 'authorization':'Bearer ' + variables.token}

    r = requests.post(url, data=json.dumps(payload), headers=headers)

def getRoomID():

    global roomID

    url = 'https://api.ciscospark.com/v1/rooms/'
    headers = {'content-type': 'application/json', 'authorization':'Bearer ' + variables.token}

    r = requests.get(url, headers=headers)

    print r.text
    roomID = r.text[17:93]

    return roomID


getRoomID()