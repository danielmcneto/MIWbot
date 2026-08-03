import slack
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from pathlib import Path
from dotenv import load_dotenv

import random
import requests
import platform

env_path = Path('.') / '.env'
load_dotenv()

#client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

app = App(token=os.environ.get("SLACK_TOKEN"))

@app.command("/miw_wiki")
def search(ack, respond, command):
    ack()
    query = command.get("text", "").strip()
    if not query:
        respond("Please say what you want to search.")
        return

    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"

    #uses to bypass the 403 error from wikipedia api
    headers = {
        'User-Agent': 'MIWHardwareDex/1.0 (dontcontact@me.com)'
        }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            #respond(data["extract"])
            respond(f"{data.get('title')}\n {data.get('extract', 'No summary found.')}\n\nRead more: {data.get('content_urls', {}).get('desktop', {}).get('page')}")
        else:
            respond(f"Sorry, I couldn't access Wikipedia right now. Please try again later. {response.status_code}")
    except Exception as e:
        respond("Error trying to find the database.")

@app.command("/miw_status")
def status(ack, respond):
    ack()
    system_info = platform.system()
    python_version = platform.python_version()
    respond(f"System: {system_info}\nPython Version: {python_version}\nI'm doing great! How can I help you today?")

@app.command("/miw_random")
def random_fact(ack, respond):
    ack()

    url = "https://dummyjson.com/quotes/random"

    headers = {
        'User-Agent': 'MIWHardwareDex/1.0 (dontcontact@me.com)'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            respond(f"\"{data.get('quote')}\" - {data.get('author')}")
        else:
            respond(f"Sorry, I couldn't access the quote API right now. Please try again later. {response.status_code}")
    except Exception as e:
        respond("Error trying to find a random fact.")

if __name__ == "__main__":
    socket_mode_handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()