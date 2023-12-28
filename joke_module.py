# Define the Telegram bot token
# export your token that you get from BotFather
# Run the below commands in the terminal
# export TOKEN= "6255139505:AAGQXZwzi4xH1KPI3UAIPwQ6OcmSvojSayE"
# export JOKE_API_URL="https://v2.jokeapi.dev/joke/Any?format=txt"

import os

# TOKEN and JOKE_API_URL should be exported before running the script
TOKEN = os.environ['TOKEN']
# Define the URL for retrieving jokes
JOKE_API_URL = os.environ['JOKE_API_URL']
