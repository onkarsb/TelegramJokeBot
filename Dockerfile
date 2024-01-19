FROM python:3.9-alpine

WORKDIR /TelegramJokeBot
COPY ./joke_bot.py .
COPY ./requirements.txt .

RUN pip install --upgrade --no-cache-dir pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python3", "joke_bot.py"]
