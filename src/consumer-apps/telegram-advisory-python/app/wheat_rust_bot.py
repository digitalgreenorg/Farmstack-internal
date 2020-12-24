#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import json

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

ENTRY, WARNING, ACTION, ACTION_2, END_C = range(5)

G_NAME, SEVERITY, DISEASE, G_KEBELE = range(4)

print("---wheat_rust_bot---")

def fetch_details(update):
    global G_NAME
    global SEVERITY
    global DISEASE
    global G_KEBELE
    G_NAME = ""
    SEVERITY = ""
    G_KEBELE = ""
    DISEASE = ""
    user = update.message.from_user
    u_name = user.first_name
    data = {}
    with open("merged_data.json", "r") as ofs:
        data = json.loads(ofs.readlines()[0])
    for value in data:
        for key, val in value.items():
            if key == "Name":
                if u_name.lower() in val.lower():
                    G_NAME = value["Name"]
                    SEVERITY = value["add_info"][0]["severity"]
                    G_KEBELE = value["Kebele"]
                    DISEASE = value["add_info"][0]["disease"]
                    break

def start(update, context):
    """Introduction to the bot"""
    reply_keyboard = [['Yes', 'No']]

    # get data from merge
    fetch_details(update)

    update.message.reply_text(
        'Hi Mr. / Ms %s I am a representative from MoA/BoA to send you an early warning ' \
        'message on wheat rust incidence specific to your area. If you want to receive the message please press yes or else no.' % (G_NAME),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return ENTRY


def entry_point(update, context):
    """Give warning info"""
    reply_keyboard = [['Next']]
    update.message.reply_text('There is a %s likely of %s happening in %s kebele' % (SEVERITY, DISEASE, G_KEBELE),
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return WARNING



def warning_message(update, context):
    """give action info"""
    reply_keyboard = [['Next']]
    update.message.reply_text('Please inform farmers in your area to be vigilant for early appearance of stipe rusts and take appropriate action',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return ACTION


def control_action(update, context):
    """give control info"""
    reply_keyboard = [['Next']]
    update.message.reply_text('Control should be considered for farmers growing the following varieties \n 1. Kubasa \n 2. Lemu',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return ACTION_2

def control_action_2(update, context):
    """Check farmer presence"""
    reply_keyboard = [['Next']]
    update.message.reply_text('And if farmer sees Presence of infection (>10% of leaf area infected)',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return END_C


def cancel(update, context):
    """cancel coversation"""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Thanks for your time. If you wish to start the conversation again, please type start and send.', reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def end_conv(update, context):
    """end coversation"""
    reply_keyboard = [['Yes', 'No']]
    user = update.message.from_user
    logger.info("User %s completed the conversation.", user.first_name)
    update.message.reply_text('If you find this information helpful and want to subscribe so as to receive messages every ten days, please press yes', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return ConversationHandler.END


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1333903854:AAGhtAkHVlPNaM3y0Hu-D3l5rvHiaUqqLYE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            ENTRY: [MessageHandler(Filters.regex('^(Yes)$'), entry_point), MessageHandler(Filters.regex('^(No)$'), end_conv)],

            WARNING: [MessageHandler(Filters.regex('^(Next)$'), warning_message)],

            ACTION: [MessageHandler(Filters.regex('^(Next)$'), control_action)],

            ACTION_2: [MessageHandler(Filters.regex('^(Next)$'), end_conv)],

            END_C: [MessageHandler(Filters.text & ~Filters.command, end_conv)]

        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
