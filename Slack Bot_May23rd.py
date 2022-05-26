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
                "text": "Miro Minute :stopwatch: - May 23rd",
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
                "text": "The *Bring everyone to me* feature is helpful when collaborating on a board :mag:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "1: Click on the profile pictures in the top right corner of the board :three_button_mouse: "
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "2: Select *Bring everyone to me*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Now everyone you are collaborating with will see what you want to share without having to navigate to your view"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "(P.S. You can see what someone else is viewing by selecting their name after clicking on the profile pictures! :sleuth_or_spy:)"
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
