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
				"text": "Miro Minute :stopwatch: - July 11th "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Happy Monday!! @channel :wave:"
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
				"text": "Did you know you can export Stickies on your Miro board to a CSV file :interrobang:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "1) Click and drag over all the Stickies you want to export :three_button_mouse:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "2) Click the 3 dots on the far right of the pop-up toolbar :hammer_and_pick:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "3) Click ' Export to CSV (Excel) ' :memo:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "This triggers a download of a CSV, which contains all of the stickies in cells! :spiral_note_pad: "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Great for taking many ideas, concepts, or data and organizing them! :bulb: "
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
