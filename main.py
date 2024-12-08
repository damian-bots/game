import os
import logging
from src import commands, callbacks
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, filters

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


if __name__ == '__main__':
    TELEGRAM_API_TOKEN = os.getenv('7717376439:AAHUUpfF-wY_L__bEX2QEnecIX0z0K77c04')
    application = ApplicationBuilder().token('7717376439:AAHUUpfF-wY_L__bEX2QEnecIX0z0K77c04').build()

    application.add_handler(CommandHandler('help', commands.help))
    application.add_handler(CommandHandler('start', commands.register, filters.Regex('-\d+')))
    application.add_handler(CommandHandler('alive', commands.start))
    application.add_handler(CommandHandler('begin', commands.begin))
    application.add_handler(CommandHandler('stop', commands.stop))
    application.add_handler(CallbackQueryHandler(callbacks.voting_callback, pattern='^-\d+_\d+_maf_\d+_\d+$'))
    application.add_handler(CallbackQueryHandler(callbacks.voting_callback, pattern='^-\d+_\d+_dayvote_\d+_\d+$'))
    application.add_handler(CallbackQueryHandler(callbacks.doctor_callback, pattern='^-\d+_\d+_doc_\d+_\d+$'))
    application.add_handler(CallbackQueryHandler(callbacks.detective_action_choice_callback, pattern='^-\d+_\d+_det(?:kill|check)_\d+_$'))
    application.add_handler(CallbackQueryHandler(callbacks.detective_player_choice_callback, pattern='^-\d+_\d+_det(?:kill|check)_\d+_\d+$'))

    application.run_polling()
