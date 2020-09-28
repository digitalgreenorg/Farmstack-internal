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

ENTRY, FIRST_NAME, FATHERS_NAME, KEBELE, END_C = range(5)

G_NAME, G_FNAME, G_KEBELE = range(3)

def fetch_details(update):
    global G_NAME
    global G_FNAME
    global G_KEBELE
    G_NAME = ""
    G_FNAME = ""
    G_KEBELE = ""
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
                    G_FNAME = value["Father_s_Name"]
                    G_KEBELE = value["Kebele"]
                    break
    

def start(update, context):
    """Introduction to the bot"""
    reply_keyboard = [['Yes', 'No']]

    # call fetch_details to get user details
    fetch_details(update)

    update.message.reply_text(
        'Hello "%s", your number is mentioned in the Woreda office, "DG REG" register.' \
        'It is mentioned that you are working as a Development Agent working for the Regional Burao of' \
        'agriculture, Ethiopia. We would like to verify the details we have through this chat. It will'\
        ' take only a few minutes. If you are a Development Agent and wish to proceed, please press yes or else no.' \
        'To abort, simply type /stop.' % (G_NAME),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return ENTRY


def entry_point(update, context):
    """Check Users name"""
    reply_keyboard = [['Yes', 'No']]
    update.message.reply_text('Is your name %s?' % (G_NAME),
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return FIRST_NAME

def update_entry_point(update, context):
    """Update firstname"""
    update.message.reply_text('Enter Your name')

    return FIRST_NAME

def check_first_name(update, context):
    """Check Users name"""
    reply_keyboard = [['Yes', 'No']]
    # user = update.message.from_user
    logger.info("Firstname %s", update.message.text)
    update.message.reply_text('Is your fathers name %s?' % (G_FNAME),
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return FATHERS_NAME

def update_first_name(update, context):
    """Update firstname"""
    logger.info("Firstname %s", update.message.text)
    update.message.reply_text('Enter Your Fathers name')

    return FATHERS_NAME

def check_fathers_name(update, context):
    """Check Users name"""
    reply_keyboard = [['Yes', 'No']]
    logger.info("Fathers name %s", update.message.text)
    update.message.reply_text('Is your keble name %s?' % (G_KEBELE),
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return KEBELE

def update_fathers_name(update, context):
    """Update firstname"""
    logger.info("Fathers name %s", update.message.text)
    update.message.reply_text('Enter Your kebele name')

    return END_C


def cancel(update, context):
    """cancel coversation"""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Thank you for your time. If you have pressed no by mistake and want to restart, please type and send start.', reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def end_conv(update, context):
    """end coversation"""
    user = update.message.from_user
    logger.info("Kebele %s", update.message.text)
    logger.info("User %s completed the conversation.", user.first_name)
    update.message.reply_text('Thank you for your time. Completed your verification.', reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1334865601:AAGM8u07ZzDqa__jV42DXiRFcUR3aMSm4g0", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            ENTRY: [MessageHandler(Filters.regex('^(Yes)$'), entry_point), MessageHandler(Filters.regex('^(No)$'), end_conv)],

            FIRST_NAME: [MessageHandler(Filters.regex('^(Yes)$'), check_first_name), MessageHandler(Filters.regex('^(No)$'), update_entry_point), MessageHandler(Filters.text & ~Filters.command, check_first_name)],

            FATHERS_NAME: [MessageHandler(Filters.regex('^(Yes)$'), check_fathers_name), MessageHandler(Filters.regex('^(No)$'), update_first_name), MessageHandler(Filters.text & ~Filters.command, check_fathers_name)],

            KEBELE: [MessageHandler(Filters.regex('^(Yes)$'), end_conv), MessageHandler(Filters.regex('^(No)$'), update_fathers_name), MessageHandler(Filters.text & ~Filters.command, check_fathers_name)],

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