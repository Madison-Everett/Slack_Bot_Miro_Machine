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
				"text": "Miro Minute :stopwatch: - June 13th",
				
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
				"text": "Here's your Miro Tip for the day! "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":arrow_down_small:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Miro allows you to *lock* an object in place on any board! :lock:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Simply right click on any object and select *Lock*."
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "This will stop anyone from moving an object accidentally :no_entry_sign:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "This can be helpful when creating a presentation :heads-down:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*or*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "when you are collaborating with people who aren't familiar with Miro :question:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":arrow_up_small:"
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
		
}]}
                
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
