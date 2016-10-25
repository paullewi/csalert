## CS-Alert (CMX-Spark Alert)
This is an application designed to take input from CMX and send triggered alerts to Spark.

**The Challenge** - We need the ability to use the location analytics provided by CMX to analyze retail floor congestion and automatically alert employees to help customers.

**The Solution** - Create an application that will query CMX for the current connected devices count (how many customers are in that area of the store) and send an alert to the floor manager's spark room when the store became too congested.

Our goal was to combine two Cisco products via APIs and scripting to automate a new capability for customers.

### [DEMO LINK](https://www.youtube.com/watch?v=sFghP0lqdv4 "DEMO")
__________________________________________________________________________________________________


This repo includes the following resources:

### Repo Information
    • README.md
		○ This document
	• .gitignore
		○ Standard gitignore file to prevent commiting unneeded or security risk files
        
### CICD Build Configuration	
    • .drone.yml
		○ CICD Build instructions for Drone Server
	• drone_secrets_sample.yml
		○ template for the secrets file that will be used to encrypt credentials
	• Dockerfile
		○ Docker build file for applicaiton container
	• requirements.txt
		○ pip installation requirements
        
### Application Files	
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


##  Application Flow
__________________________________________________________________________________________________

![app flow](https://github.com/paullewi/csalert/blob/master/Screen%20Shot%202016-10-25%20at%2011.25.52%20AM.png)



##  Installation
__________________________________________________________________________________________________

### Prerequisites

A Cisco Spark account: developer.ciscospark.com. You will need the token from this account.

If you want to change the MSE server you will need the IP and authentication credentials of that device. 

You will need the email contact for the alert. 

Python 2.7+
virtualenv
Git
Terminal access
Optional: Docker (to run from a container)

### Downloading

Pull down the Repo Files:
    
**git clone https://github.com/imapex/csalert**
    

## Running
__________________________________________________________________________________________________

1) Open Terminal
2) Change directories to the repo
3) Run the application

    	python appstart.py
4) Enter Spark Token: (spark token)
5) Enter Email: (email@email.com)
6) Enter Floor Capacity: (0 - 9999999)


![variables](https://github.com/paullewi/csalert/blob/master/Screen%20Shot%202016-10-25%20at%2011.51.31%20AM.png)

7) Hit Enter and the application will now continuously make API queries to the MSE for the device count. The MSE will return the following format to the application:

![request](https://github.com/paullewi/csalert/blob/master/Screen%20Shot%202016-10-25%20at%2011.56.03%20AM.png)

8) When the device count reaches the limit, a spark room will be created and the contact will be added to the room. An alert will be sent. 

![spark output](https://github.com/paullewi/csalert/blob/master/Screen%20Shot%202016-10-25%20at%2011.56.59%20AM.png)

9) Ctrl+C to end the application (runs in background every five minutes by default). 

## Custimization
__________________________________________________________________________________________________

The application has a number of customizable elements to tailor to your requirements. 

**Input Variables**

You can customize the three main variables when you run the application. These three prompts can be edited in the "variables.py" file. You can also choose to hardcode the variables in this file as well by replacing the raw_input prompt with the value. 

**Room Name**

To edit the room name displayed in the Spark Room, simply edit the text after "title:" in the "sparkRoom.py" file:

    payload = {
        'title': 'Department Team Room'
    }

**Alert Message**

To edit the message displayed in the Spark Room, simply edit the text after "text:" in the "sparkMesage.py" file:

	"text" : "The floor is getting congested. Please assist the shoppers in isle X, pronto!"
    
**API Request Timer**

To edit how often the application checks the MSE for the device count, simply change the sleep value in the "appstart.py" file to the number of seconds you want between requests. 

            execute.runApp()
            time.sleep(x)


ENJOY!



