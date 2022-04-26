#!/usr/bin/env python3

from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt import App
import os
from dotenv import load_dotenv
import joke_file_f as j

load_dotenv()

SLACK_BOT_TOKEN = os.getenv('BOT_TOKEN')
SLACK_APP_TOKEN = os.getenv('APP_TOKEN')

app = App(token=SLACK_BOT_TOKEN)

@app.command('/joke')
def joke(ack, say):
    ack()
    say(j.getJoke())

@app.command('/source')
def source(ack, respond):
    ack()
    respond(f'Here is the source code for the bot! github.com/ImDeviate/Public-Repos/tree/master/Python-Slack-Bot')

if __name__ == '__main__':
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()