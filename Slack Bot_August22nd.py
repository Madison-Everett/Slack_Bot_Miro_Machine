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
				"text": "Miro Minute :stopwatch: - Aug 22th"
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
				"text": "Did you know you can create your own color palette in Miro? :artist: "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "First, create a shape and select the *Fill Color* on the shape toolbar."
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "From here, you can click and drag colors off of the mini window to remove them :recycle:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Or you can click the :heavy_plus_sign: button and use the color tool or the eyedropper tool to make up your own color palette!:art:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Your color palette will stay the same between Miro boards, so there’s no need to duplicate your efforts! :partying_face:"
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
