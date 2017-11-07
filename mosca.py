# A bot dedicated to the one and only Maurizio Mosca, sends pics of his beautiful shiny grin on command

import requests
import json
import random
from telegram.ext import Updater, CommandHandler, MessageHandler

botUrl = 'BOT_URL'

def start(bot, update):
        update.message.reply_text('Eccoci allora fiamo pronti.', quote=False)

def sendpic(bot, update):
        numbersArray = [0, 10, 20, 30, 40, 50, 60, 70, 80]

        randRange = random.choice(numbersArray)

        body = {'key': 'KEY',
                'cx': 'CX',
                'imgType': 'face',
                'lowRange': randRange,
                'num': 10,
                'q': 'maurizio mosca',
                'searchType': 'image'}

        r = requests.get('https://www.googleapis.com/customsearch/v1', params=body)

        jsonResponse = r.json()

        imgList = []

        for elem in jsonResponse['items']:
                imgList.append(elem['link'])

        pic = random.choice(imgList)

        update.message.reply_photo(pic, quote=False)

def main():
        updater = Updater("UPDATER")
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("pic", sendpic))

#start
        updater.start_polling()

        updater.idle()

if __name__ == '__main__':
        main()
