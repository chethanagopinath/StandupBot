import slack
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timedelta

#loading the env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

#get the environment variable - the token specifically and passing it to the client
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

message = """Hi! Please send in your updates in the format below. 
\n1. What did you do yesterday? 
\n2. What will you do today?
\n3. Are there any impediments in your way?
"""

date = (datetime.now() + timedelta(seconds=20)).timestamp()

client.chat_scheduleMessage(channel='#standup', text=message, post_at=date) 