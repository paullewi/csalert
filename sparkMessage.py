#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

#variables
url = 'https://api.ciscospark.com/v1/messages'
payload = {"roomId" : "Y2lzY29zcGFyazovL3VzL1JPT00vMTNmY2VmNjAtNmM5MS0xMWU2LTkyZWUtZjFkNjY3OTc1NjFl","text" : "Staff Member please report to isle X, pronto!"}
headers = {'content-type': 'application/json', 'authorization':'Bearer NTJiMTQyZjUtZTZlZC00N2I1LThjNTgtYWNmMjgyMDJhZmMyYzExYzY3YjQtNTdl'}

#API POST to create Spark Room
r = requests.post(url, data=json.dumps(payload), headers=headers)
