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
                "text": "Miro Minute :stopwatch: - June 20th",
                
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
                "text": "Every object on a Miro board has a hyperlink of its own! :link:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "These links can be accessed using the following steps:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "1: Select an object or frame and click on the three dots that appear on the far right of the pop-up tool bar"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "2: Select the *Copy Link* option"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "3: Paste the link anywhere – Slack, for example :slack:– and it will take you directly to the original item"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "These links can be very helpful when you are trying to share one aspect of an extensive board! "
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
        }
    ]
}
                
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
