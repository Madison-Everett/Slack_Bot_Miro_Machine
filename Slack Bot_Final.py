import json
import sys
import random
import requests
if __name__ == '__main__':
    url =   "private"                    
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
				"text": "Final Miro Minute :stopwatch: "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Hey everyone @channel!! :wave:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "It was such a joy :hugging_face: to bring you all new tips and tricks each week!"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "But since things are now picking up and getting busy, its time for me to say goodbye for now! :pleading_face:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Thanks for being apart of the Miro Minute Summer Series and I hope you all enjoyed it as much as I did!"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "You can find any past tip from the last three months in the Miro Quick Tips and Tricks Confluence page linked below. :CONFETTI_BALL: "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*MIRO MACHINE OUT* :V:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://devops.app.vanderbilt.edu/confluence/display/EMOS/Miro+Quick+Tips+and+Tricks+-+Courtesy+of+Miro+Machine|:book: *Once Again! Happy Miro-ing! :blush:*> "
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "mrkdwn",
					"text": "*Madison* and *James* have approved this message.:nerd_face:"
				}
			]
		}
	]
}
                
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
