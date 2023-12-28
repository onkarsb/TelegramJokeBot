# TelegramJokeBot
Telegram Joke Bot that sends a new joke, almost everytime!

# Run

## 1. Manually
We need to export two environment variables TOKEN and JOKE_API_URL before running the joke_bot.py script.

```bash 
export TOKEN="6255139505:AAGQXZwzi4xH1KPI3UAIPwQ6OcmSvojSayE"
export JOKE_API_URL="https://v2.jokeapi.dev/joke/Any?format=txt"
python3 ./joke_bot.py
```

## 2. Docker

### build container
```bash
docker build -t joke_bot:0.1 .
```

### run docker container
```bash
docker run --rm -d \
    -e TOKEN="6255139505:AAGQXZwzi4xH1KPI3UAIPwQ6OcmSvojSayE" \
    -e JOKE_API_URL="https://v2.jokeapi.dev/joke/Any?format=txt" \
    joke_bot:0.1
```
