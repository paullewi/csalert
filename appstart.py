#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import variables
import execute
import sys
import subprocess
import time

### parses API response for client count ###
def getCount():



    global numlist

    with open('CMXResponse.txt', 'r') as myfile:                      #opens txt file with API response
        data=myfile.read().replace('\n', '')                     #turns txt file into string
        numlist = map(int, re.findall('\d+', data))              #pulls out digits and converts to list

    return numlist



### turns client count into integer ###
def magic(numlist):

    global count

    s = ''.join(map(str, numlist))
    count = int(s)

    return count



### checks user input "threshold" against client count integer ###
def compare():

    while True:
        subprocess.call("./CMXRequest.sh", shell=True)
        getCount()
        magic(numlist)

        if count >= variables.threshold:
            print "There are currently",count,"customers in this department. We are sending an alert to the Manager."
            execute.runApp()
            time.sleep(300)
        else:
            print "There are currently",count,"customers. The floor is operating smoothly."
            time.sleep(300)

compare()



