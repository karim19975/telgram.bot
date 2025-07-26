from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "7897254628:AAGF5-RzfqbQci5RFHI30u38a6fpMdweMQM"  #


def start(update: Update, context: CallbackContext):
    update.message.reply_text("مرحبًا! أنا بوتك على GitHub Codespaces! 🚀")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"📩: {update.message.text}")

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    print("✅ البوت يعمل...")

if __name__ == "__main__":
    main()