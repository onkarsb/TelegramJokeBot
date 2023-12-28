import requests
from telegram.ext import CommandHandler, Updater
from joke_module import TOKEN, JOKE_API_URL


# Define a function to handle the /start command
def start(update, context):
    # Send a welcome message
    update.message.reply_text('Welcome to Joke Bot. Send /joke to get a joke')
    # chat_id=update.effective_chat.id
    # chat_username = update.effective_chat.username
    # print(f"Start cmd\nUsername : {chat_username}\nChat Id : {chat_id}")


# Define the function to handle the /joke command
def get_joke(update, context):
    # Send a request to the joke API
    response = requests.get(JOKE_API_URL)
    if response.status_code == 200:
        joke = response.text.strip()
        # Send the joke as a message to the user
        chat_id = update.effective_chat.id
        # chat_username = update.effective_chat.username
        context.bot.send_message(chat_id=chat_id, text=joke)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Sorry, I couldn't fetch a joke at the moment. Please try again later.")


def main():
    # Create an instance of the Updater class and pass in your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start function as a command handler
    dispatcher.add_handler(CommandHandler('start', start))

    # Register the /joke command handler
    dispatcher.add_handler(CommandHandler('joke', get_joke))

    # Start the bot
    print("Bot starting...")
    updater.start_polling()
    print("Bot started")
    updater.idle()


if __name__ == '__main__':
    main()
