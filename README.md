CS-Alert (CMX-Spark Alert)
This is an application designed to take input from CMX and send triggered alerts to Spark.

The Challenge - We need the ability to use the location analytics provided by CMX to analyze retail floor congestion and automatically alert employees to help customers.
The Solution - Create an application that will query CMX for the current connected devices count (how many customers are in that area of the store) and send an alert to the floor manager's spark room when the store became too congested.
Our goal was to combine two Cisco products via APIs and scripting to automate a new capability for customers.
This repo includes the following resources:
Repo Information
	• README.md
		○ This document
	• .gitignore
		○ Standard gitignore file to prevent commiting unneeded or security risk files
CICD Build Configuration
	• .drone.yml
		○ CICD Build instructions for Drone Server
	• drone_secrets_sample.yml
		○ template for the secrets file that will be used to encrypt credentials
	• Dockerfile
		○ Docker build file for applicaiton container
	• requirements.txt
		○ pip installation requirements
Application Files
	• appstart.py
		○ This kicks off the application. It kicks off the CMX API request, writes the response to a text file and parses that file for the current devices count. It will then ask the user for input, and compare the device count to the threshold. It will continuously ping CMX and kick off the spark scripts if the threshold is crossed.
	• variables.py
		○ This is the script that will ask the user for their spark token, the floor manager's email, and the customer capacity (threshold) of the store floor.
	• CMXRequest.sh
		○ API request to the MSE for the current device count.
	• CMXResponse.txt
		○ API response from the MSE of the current device count.
	• execute.py
		○ Python file with a function that kicks off the spark scripts in order.
	• sparkRoom.py
		○ Creates a Spark room.
	• sparkMember.py
		○ Adds the floor manager to the Spark room.
	• sparkMessage.py
		○ Sends a message to the Spark room.

