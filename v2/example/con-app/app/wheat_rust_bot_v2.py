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

ENTRY, WARNING, ACTION, ACTION_2, END_C, OPTIONS = range(6)

G_NAME, SEVERITY, DISEASE, G_KEBELE, G_WOREDA, SALUTATION, VARIETY, GROWTH_STAGE = range(8)

print("---wheat_rust_bot---")

def fetch_details(update):
    global G_NAME
    global SEVERITY
    global DISEASE
    global G_KEBELE
    global G_WOREDA
    global SALUTATION
    global VARIETY
    global GROWTH_STAGE
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
                    SEVERITY = value["add_info"]["severity"]
                    G_KEBELE = value["Kebele"]
                    DISEASE = value["add_info"]["disease"]
                    VARIETY = value["add_info"]["variety"]
                    GROWTH_STAGE = value["add_info"]["growth stage"]
                    SALUTATION = value["Salutation"]
                    G_WOREDA = value["Woreda"]
                    break

def start(update, context):
    """Introduction to the bot"""
    reply_keyboard = [['Yes', 'No']]

    # get data from merge
    fetch_details(update)

    update.message.reply_text(
        'Hi %s %s I am a representative from MoA/BoA to send you an early warning ' \
        'message on wheat rust incidence specific to your area. If you want to receive the message please press yes or else no.' % (SALUTATION, G_NAME),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return ENTRY


def entry_point(update, context):
    """Give warning info"""
    reply_keyboard = [['Next']]
    update.message.reply_text('There is a %s likely of %s happening in %s woreda for %s crop' % (SEVERITY, DISEASE, G_WOREDA, GROWTH_STAGE),
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return WARNING


def warning_message(update, context):
    """give action info"""
    reply_keyboard = [['Next']]
    update.message.reply_text('Please inform farmers in your area to be vigilant for early appearance of %s and take appropriate action' % (DISEASE),
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return ACTION


def control_action(update, context):
    """give control info"""
    reply_keyboard = [['Next']]
    update.message.reply_text('Control should be considered for farmers growing the following varieties %s' % (VARIETY),
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return OPTIONS

def control_action_2(update, context):
    """Check farmer presence"""
    reply_keyboard = [['Next']]
    update.message.reply_text('And if farmer sees Presence of infection ',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return END_C

def option_action(update, context):
    """Check farmer presence"""
    reply_keyboard = [['Yes'], ['Detecting wheat rust'], ['Variety'], ['Applying Chemials'], ['Control'], ['Any other question']]
    update.message.reply_text('If you find this information helpful and want to subscribe so as to receive messages every ten days, please press yes \n\n If you have any further questions please select from the menu below.',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return OPTIONS

def detect_wheat_rust(update, context):
    """Check farmer presence"""
    reply_keyboard = [['Back']]
    update.message.reply_text('Link - https://www.youtube.com/watch?v=7C_fhB3M17o&t=141s',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return OPTIONS

def detect_variety(update, context):
    """Check farmer presence"""
    reply_keyboard = [['Back']]
    update.message.reply_text('Link - https://www.youtube.com/watch?v=7C_fhB3M17o&t=141s',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return OPTIONS

def apply_chemicals(update, context):
    """Check farmer presence"""
    reply_keyboard = [['Back']]
    update.message.reply_text('የተመዘገቡ ፀረ ሻጋታ ኬሚካሎች መካከል ዋና ዋናዎቹ፡-\n\nሬክሲዱኦ 0.5 ሊ/ር በ200 ሊ/ር ዉሃ፣\nባይላተን 25 ደብሊዩ ፒ 0.5 ሊ/ር በ200 ሊ/ር ዉሃ፣\nባምፐር 25 ኢሲ፣ ናትቮ  0.75 ሊ/ር በ200 ሊ/ር ዉሃ እና\nቲልት 0.5 ሊ/ር በ200 ሊ/ር ዉሃ ናቸዉ::\nእነዚህን ፀረ ሻጋታ ተህዋስያን ኬሚካሎችን በአግባቡ ለመጠቀም በአቅራቢያዎ የሚገኙ የእርሻ ባለሙያዎች የምክር አገልግሎት በየጊዜው መጠቀም ያስፈልጋል።',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return OPTIONS

def any_other_ques(update, context):
    """Check farmer presence"""
    reply_keyboard = [['Back']]
    update.message.reply_text('Link - https://www.youtube.com/watch?v=7C_fhB3M17o&t=141s',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return OPTIONS

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

            OPTIONS: [MessageHandler(Filters.regex('^(Yes)$'), end_conv), MessageHandler(Filters.regex('^(Next)$'), option_action), MessageHandler(Filters.regex('^(Back)$'), option_action), MessageHandler(Filters.regex('^(Detecting wheat rust)$'), detect_wheat_rust), MessageHandler(Filters.regex('^(Variety)$'), detect_variety), MessageHandler(Filters.regex('^(Applying Chemials)$'), apply_chemicals), MessageHandler(Filters.regex('^(Any other question)$'), any_other_ques)],

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