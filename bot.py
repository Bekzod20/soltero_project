

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    languages = "1. O'zbek ðºð¿ \n2. Rus ð·ðº \n3. English ðºð¸"
    update.message.reply_text('Tilni Tanlang: ')
    update.message.reply_text(languages)

    print(update.message.text)



def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Man sizga yordam bera olaman!')
    update.message.reply_text("Shu havola oraqali o'ting")


def echo(update, context):
    """Echo the user message."""
    # update.message.reply_text(update.message.text)
    print(update.message.text)
    if update.message.text == '1':
        update.message.reply_text('Shahar/Viloyatni Tanlang: ')
        cities = "1. Andijon \n2. Toshkent viloyati \n3. Samarqand \n4. Jizzax \n5. Toshkent Shahri" \
                 "\n6. Farg'ona \n7. Namangan \n8. Surxandaryo \n9. Qashqadaryo \n10. Xorazm \n11 Buxoro \n12. Navoiy"

        update.message.reply_text(cities)



    if update.message.text == '5':
        update.message.reply_text('Tumani Tanlang: ')
        districts = "1. Yunusobod \n2. Yakkasaroy  \n3. Chilonzor \n4. Uchtepa \n5. Shayxontohur" \
                    "\n6. Mirobod \n7. Olmazor \n8. Mirzo Ulugâbek \n9. Sergeli tumani \n10. Bektemir tumani"

        update.message.reply_text(districts)

    if update.message.text == '7':
        update.message.reply_text('Klinikani tanlang ð¥: ')
        clinics = "1. NEW LIFE MEDICAL  \n2. Akfa Medline"

        update.message.reply_text(clinics)
    

    if update.message.text == '2':
        update.message.reply_text('Doktorni tanlang ð¨ââð©ââ: ')
        doctors = "1. Ð¥Ð¸ÑÑÑÐ³  \n2. ÐÑÐ¸ÑÐ¸Ð°ÑÑ \n3. ÐÐ°ÑÐ´Ð¸Ð¾Ð»Ð¾Ð³ \n4. ÐÐµÐ´Ð¸Ð°ÑÑ \n5. Ð­Ð½Ð´Ð¾ÐºÑÐ¸Ð½Ð¾Ð»Ð¾Ð³ \n6. ÐÐ»Ð»ÐµÑÐ³Ð¾Ð»Ð¾Ð³ \n7. ÐÐ½ÐµÑÑÐµÐ·Ð¸Ð¾Ð»Ð¾Ð³ \n8. ÐÑÐ¸ÑÐ¼Ð¾Ð»Ð¾Ð³ \n9. ÐÐ°ÑÑÑÐ¾ÑÐ½ÑÐµÑÐ¾Ð»Ð¾Ð³ \n10. Ð³ÐµÐ¼Ð°ÑÐ¾Ð»Ð¾Ð³ \n11. ÐÐµÐ¿Ð°ÑÐ¾Ð»Ð¾Ð³ \n12. Ð¢ÐµÑÐ°Ð¿ÐµÐ²Ñ"
        update.message.reply_text(doctors)

    if update.message.text == '3':
        update.message.reply_text('Doktor: ÐÐ¼Ð¸Ð½Ð¾Ð² Ð¡Ð°Ð½Ð¶Ð°Ñ ÐÐ±Ð´ÑÐ°Ð·Ð¸Ð¼Ð¾Ð²Ð¸Ñ (ÐÑÐ°Ñ-ÐºÐ°ÑÐ´Ð¸Ð¾Ð»Ð¾Ð³)')

        update.message.reply_text('Doktor ish vaqtlari â°ï¸: ')
        doctors = "1. Dushanbi 13:00-18:00  " \
                  "\n2. Seshanbi 13:00-18:00" \
                  "\n3. Chorshanbi 13:00-18:00 " \
                  "\n4. Payshanbi 13:00-18:00 " \
                  "\n5. Juma - " \
                  "\n6. Shanbi - " \
                  "\n7. Yakshanbi - "
        update.message.reply_text(doctors)
        update.message.reply_text('Qabulga yozilish uchun hafta kuni raqamda yuvoring ðï¸: ')

    if update.message.text == '4':
        update.message.reply_text('Mavjud vaqtlar â°')

        available_times = "10. 13:00-13:20" \
                  "\n11. 14:00-14:20" \

        update.message.reply_text(available_times)
        update.message.reply_text('Qabulga yozilish uchun mavjud vaqtni raqamda yuvoring ðï¸: ')

    if update.message.text == '10':
        update.message.reply_text('6. Yozilish â \n4. Ortga')

    if update.message.text == '6':
        update.message.reply_text('Siz doktor qabuliga yozildingiz! â')
        msg = 'ð  Hafta kuni: Payshanbi \nâ°  Vaqt: 13:00-13:20 \nð¨ââ Doktor: ÐÐ¼Ð¸Ð½Ð¾Ð² Ð¡Ð°Ð½Ð¶Ð°Ñ ÐÐ±Ð´ÑÐ°Ð·Ð¸Ð¼Ð¾Ð²Ð¸Ñ (ÐÑÐ°Ñ-ÐºÐ°ÑÐ´Ð¸Ð¾Ð»Ð¾Ð³) '
        update.message.reply_text(msg)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("your_token", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
