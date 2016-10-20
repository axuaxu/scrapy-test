from slackclient import SlackClient
from  private import *
from  settings import *

#SLACK_TOKEN = "xoxp-78949513686-78949513750-78948238596-db8be5b5bd"
#SLACK_CHANNEL = "#housing"
sc = SlackClient(SLACK_TOKEN)

desc = "this is a test message"

sc.api_call("chat.postMessage", channel=SLACK_CHANNEL, text=desc , username='alappin', icon_emoji=':robot_face:')
