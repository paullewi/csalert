#!/bin/sh
#API call to get client count from CMX


VAR=$(curl -s -X GET -H "Authorization: Basic bGVhcm5pbmc6bGVhcm5pbmc=" "https://msesandbox.cisco.com:8081/api/location/v2/clients/count" )

echo $VAR > CMXResponse.txt

python CMX.py