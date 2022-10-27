import json
import sys
import random
import requests
if __name__ == '__main__':
    url =  "private"                        
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
				"text": "Miro Minute :stopwatch: - Aug 1st"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Happy Monday @channel!! :wave:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Here's your Miro Tip for the day!"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "In a meeting :virtual-meeting: and want to create a quick Miro board? "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Open up your favorite browser and type *miro.new* in the address bar and press enter to create a new Miro Board. :enter-key2: "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Great for fast-paced meetings! :running:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "For more tips, tricks, and tutorials, check out Miro's Confluence page by clicking the link below :arrow_down::"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "<https://devops.app.vanderbilt.edu/confluence/display/EMOS/Miro|:book: *Happy Miro-ing!*> "
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
