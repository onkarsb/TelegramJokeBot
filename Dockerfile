FROM python:3.9-alpine

RUN apk add git
RUN git clone https://github.com/onkarsb/TelegramJokeBot.git /TelegramJokeBot

WORKDIR /TelegramJokeBot
RUN pip install --upgrade --no-cache-dir pip && \
    pip install --no-cache-dir -r requirements.txt

CMD python3 joke_bot.py 
