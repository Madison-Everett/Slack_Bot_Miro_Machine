import json
import sys
import random
import requests
if __name__ == '__main__':
    url = "private"                            
    title = (f"Miro Minute :stopwatch:")
    slack_data = {
        "username": "Miro Machine",
        "icon_emoji": ":robot_face:",
        #"channel" : "#James Hale",
        "blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Intro to Miro Minute",
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Welcome to Miro Minute!"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "I am a helpful bot that will give you tips in Miro every Monday starting next week!"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "It's so nice to meet you! I hope we get along! :smiley:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "For more info on getting started with Miro, check the Miro Basics Confluence Page below:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://devops.app.vanderbilt.edu/confluence/display/EMOS/Miro+Basics|:large_green_circle: Miro Basics :large_green_circle:>"
			}
		}
	]
	
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
