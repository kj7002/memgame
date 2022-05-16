# -*- coding: utf-8 -*-
"""FrameMem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o21ua8swREMQj77oiN_ISLieszGIgHOs
"""

pip install python_telegram_bot

!pip install Telegram
import Telegram
!pip install InlineKeyboardButton

import os
PORT = int(os.environ.get('PORT', 5000)) 
import logging, time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND = range(2)
# Callback data
ZERO1, ZERO2, ZERO3, LAST, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN= range(14)
i=0
def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to play the qiuz. Made by KJ")

def start(update: Update, context: CallbackContext):
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    update.message.reply_sticker("CAACAgIAAxkBAALxfmIFRGkEeU28NhN8zYlO5SvBk83gAAIUEgAC2jhpSHqUAlCeS8m1IwQ")
    time.sleep(3)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("Proceed", callback_data=str(ONE)),
            InlineKeyboardButton("Quit", callback_data=str(ZERO1)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("Welcome to THE MEMORY GAME! \n Rules:- \n Words will be shown and you will be asked to pick the correct one from the options \n ~KJ", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return SECOND

def one(update: Update, context: CallbackContext) -> int:
    global i
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Quit", callback_data=str(ZERO1)),
            InlineKeyboardButton("Telegram", callback_data=str(ZERO2)),
        ], 
    
    
        [
            InlineKeyboardButton("Soap", callback_data=str(TWO)),
            InlineKeyboardButton("Rugby" , callback_data=str(ZERO3)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Stage 1: Warm Up!"
    ) 
    time.sleep(3)
    query.edit_message_text(
        text="Remember this word: Soap",
    )
    time.sleep(2)
    query.edit_message_text(
        text="What was the word!?", reply_markup=reply_markup
    )
    i=0
    return SECOND

def two(update: Update, context: CallbackContext) -> int:
    global i
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("After", callback_data=str(ZERO1)),
            InlineKeyboardButton("Life", callback_data=str(THREE)),
        ], 
        [ 
            InlineKeyboardButton("Hello", callback_data=str(ZERO2)),
            InlineKeyboardButton("Officer", callback_data=str(ZERO3)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Life",
    )
    time.sleep(1)
    query.edit_message_text(
        text="What was the word!?", reply_markup=reply_markup
    )
    i+=1
    return SECOND


def three(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    global i
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Ruff", callback_data=str(ZERO1)),
            InlineKeyboardButton("Run", callback_data=str(ZERO2)),
        ],  
    
        [     
            InlineKeyboardButton("Roll", callback_data=str(ZERO3)),
            InlineKeyboardButton("Rub", callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Rub",
    )
    time.sleep(0.75) 
    query.edit_message_text(
        text="What was the word!?", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    i+=1
    return SECOND

def four(update: Update, context: CallbackContext) -> str:
    global i
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Race King Break", callback_data=str(FIVE)),
            InlineKeyboardButton("Case Ring Break", callback_data=str(ZERO2)),
        ],  
    
        [     
            InlineKeyboardButton("Race Break Ring", callback_data=str(ZERO3)),
            InlineKeyboardButton("Ring Case Break", callback_data=str(ZERO1)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='Stage 2: Series of words') 
    time.sleep(3)
    query.edit_message_text(
        text="Race King Break",
    )
    time.sleep(1)
    query.edit_message_text(
        text="What was the series of words!?", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    i+=1
    return SECOND

def five(update: Update, context: CallbackContext) -> str:
    global i
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("fire", callback_data=str(ZERO2)),
            InlineKeyboardButton("far", callback_data=str(SIX)),
        ],  
    
        [     
            InlineKeyboardButton("frock", callback_data=str(ZERO3)),
            InlineKeyboardButton("fit", callback_data=str(ZERO1)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(
        text="fit",
    )
    time.sleep(0.75)
    query.edit_message_text(
        text="fire",
    )
    time.sleep(0.75)
    query.edit_message_text(
        text="far",
    )
    time.sleep(0.75) 
    query.edit_message_text(
        text="frock",
    )
    query.edit_message_text(
        text="What was the third word of the series?", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    i+=1
    return SECOND

def six(update: Update, context: CallbackContext) -> str:
    global i
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Bitter", callback_data=str(ZERO1)),
            InlineKeyboardButton("Better", callback_data=str(ZERO2)),
        ],  
    
        [     
            InlineKeyboardButton("Butter", callback_data=str(ZERO3)),
            InlineKeyboardButton("Batter", callback_data=str(SEVEN)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(
        text="Better Batter Butter Bitter",
    )
    time.sleep(1)
    query.edit_message_text(
        text="What was the second word of the series?", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    i+=1
    return SECOND

def seven(update: Update, context: CallbackContext) -> str:
    global i
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Play", callback_data=str(EIGHT)),
            InlineKeyboardButton("Hug", callback_data=str(ZERO3)),
        ],  
    
        [     
            InlineKeyboardButton("Joy", callback_data=str(ZERO2)),
            InlineKeyboardButton("Fast", callback_data=str(ZERO1)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Ok... Now don't blink your eyes!" ) 
    time.sleep(2)
    query.edit_message_text(
        text=" \\\\\\$¥₹# Fast Joy Play Hug $¥₹#\\\\\ ",
    )
    time.sleep(1)
    query.edit_message_text(
        text="What was the word before word after the third word of the series?", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    i+=1
    return SECOND

def eight(update: Update, context: CallbackContext) -> str:
    global i
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("172 306", callback_data=str(ZERO2)),
            InlineKeyboardButton("127 495", callback_data=str(ZERO3)),
        ],  
    
        [     
            InlineKeyboardButton("172 385", callback_data=str(NINE)),
            InlineKeyboardButton("127 365", callback_data=str(ZERO1)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='Stage 3: Numbers...')
    time.sleep(2)
    query.edit_message_text(
        text="172385",
    )
    time.sleep(1)
    query.edit_message_text(
        text="What was the number?", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    i+=1
    return SECOND

def nine(update: Update, context: CallbackContext) -> str:
    global i
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("2>35>57>72>5", callback_data=str(ZERO2)),
            InlineKeyboardButton("57>72>2>5>35", callback_data=str(ZERO1)),
        ],  
    
        [     
            InlineKeyboardButton("35>2>72>57>5", callback_data=str(ZERO3)),
            InlineKeyboardButton("57>2>72>5>35", callback_data=str(TEN)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(
        text="57",
    )
    time.sleep(0.75)
    query.edit_message_text(
        text="2",
    )
    time.sleep(0.75)
    query.edit_message_text(
        text="72",
    )
    time.sleep(0.75) 
    query.edit_message_text(
        text="5",
    )
    time.sleep(0.75)
    query.edit_message_text(
        text="35",
    )
    time.sleep(0.75)
    query.edit_message_text(
        text="In which order did the numbers appear? ", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    i+=1
    return SECOND

def ten(update: Update, context: CallbackContext) -> str:
    global i
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🔴🟠🟢🔵🟣", callback_data=str(ZERO2)),
            InlineKeyboardButton("🟠🟣🔵🟢🔴", callback_data=str(ZERO1)),
        ],  
    
        [     
            InlineKeyboardButton("🟢🔵🟣🟠🔴", callback_data=str(ZERO3)),
            InlineKeyboardButton("🟠🟢🟣🔵🔴", callback_data=str(LAST)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='Stage 2: Colours')
    time.sleep(2)
    query.edit_message_text(
        text="🟠",
    )
    time.sleep(0.75)
    query.edit_message_text(
        text="🟢",
    )
    time.sleep(0.75)
    query.edit_message_text(
        text="🟣 ",
    )
    time.sleep(0.75) 
    query.edit_message_text(
        text="🔵",
    )
    time.sleep(0.75)
    query.edit_message_text(
        text="🔴",
    )
    time.sleep(0.75)
    query.edit_message_text(
        text="In which order did the colours appear appear? ", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    i+=1
    return SECOND

def last(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("AGAIN", callback_data=str(ONE)),
            InlineKeyboardButton("QUIT", callback_data=str(ZERO1)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Congratulations, You Won! 🥳🥳... \n But you get nothing 😅 \n Want to play again? ", reply_markup=reply_markup
    )
    return SECOND 

def end1(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    global i
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Uh oh! See you next time!")
    time.sleep(2)
    query.edit_message_text(text='Youre score is...') 
    time.sleep(1.5)
    query.edit_message_text(text=i)
    return ConversationHandler.END
    
def end2(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    global i
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Uh oh! See you next time!")
    time.sleep(2)
    query.edit_message_text(text='Youre score is...') 
    time.sleep(1.5)
    query.edit_message_text(text=i) 
    return ConversationHandler.END

def end3(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    global i
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Uh oh! See you next time!")
    time.sleep(2)
    query.edit_message_text(text='Youre score is...') 
    time.sleep(1.5)
    query.edit_message_text(text=i)
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5274169669:AAE0z_DxdU5A3UzDC2quAO0XzEJUDiPptjA", use_context=True )

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'),
                
            ],
            SECOND: [
                CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(end1, pattern='^' + str(ZERO1) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),  
                CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'), 
                CallbackQueryHandler(last, pattern='^' + str(LAST) + '$'), 
                CallbackQueryHandler(end2, pattern='^' + str(ZERO2) + '$'),
                CallbackQueryHandler(end3, pattern='^' + str(ZERO3) + '$'),
                CallbackQueryHandler(four, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(five, pattern='^' + str(FIVE) + '$'),
                CallbackQueryHandler(six, pattern='^' + str(SIX) + '$'),
                CallbackQueryHandler(seven, pattern='^' + str(SEVEN) + '$'),
                CallbackQueryHandler(eight, pattern='^' + str(EIGHT) + '$'),
                CallbackQueryHandler(nine, pattern='^' + str(NINE) + '$'),
                CallbackQueryHandler(ten, pattern='^' + str(TEN) + '$'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(CommandHandler('help', help_command)) 
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    

if __name__ == '__main__':
    main()