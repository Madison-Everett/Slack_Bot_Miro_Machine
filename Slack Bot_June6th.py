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
				"text": "Miro Minute :stopwatch: - June 6th "
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
				"text": "There are a ton of quick keyboard shortcuts to make your Miroing easier while you are working in your Whiteboard:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Press *V* for the Select tool :three_button_mouse:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Press *H* for the Hand tool :raised_hand_with_fingers_splayed:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Press *P* for the Pen Tool :black_nib:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Press *S* for the Shape Tool :large_blue_square:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Press *F* for Frame Tool :frame_with_picture:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Press *N* for Sticky Notes :spiral_note_pad:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Press *D* for Cards :placard:"
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
