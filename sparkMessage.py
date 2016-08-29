#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import variables
import sparkRoom

def addMessage():
    url = 'https://api.ciscospark.com/v1/messages'
    payload = {
        "roomId" : sparkRoom.roomID,
        "text" : "The floor is getting congested. Please assist the shoppers in isle X, pronto!",
    }
    headers = {'content-type': 'application/json', 'authorization':'Bearer ' + variables.token}

    r = requests.post(url, data=json.dumps(payload), headers=headers)

