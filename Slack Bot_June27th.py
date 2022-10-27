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
				"text": "Miro Minute :stopwatch: - June 27th "
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
				"text": "Did you know you can transform text in Excel to sticky notes in Miro:interrobang::"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "1) Copy a row or column of data from an Excel Spreadsheet :clipboard:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "2) Paste it in a Miro board :placard:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Each individual cell will become a sticky note in Miro that you can move around as you wish! :exploding_head:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "This is great for making data easier to read, group, and analyze! :chart_with_upwards_trend:"
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
