#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import variables
import sparkRoom

### adds floor manager to Spark Room ###
def addMember():
    url = 'https://api.ciscospark.com/v1/memberships'
    payload = {
        "roomId": sparkRoom.roomID,
        "personEmail": variables.email,
        "isModerator": "false"
    }
    headers = {'content-type': 'application/json', 'authorization':'Bearer ' + variables.token}

    r = requests.post(url, data=json.dumps(payload), headers=headers)

