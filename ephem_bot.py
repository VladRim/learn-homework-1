"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(bot, update):
    text = "вызван /start"
    print(text)
    print(ephem.earth_radius)
    update.message.reply_text(text)


def ephem_explorer(bot, update):
    msg= update.message.text.split(" ")
    planet = msg[1]
    constell = ephem.constellation(planet)
    print(planet)
    print(constell)

def talk_to_me(bot, update):
    user_text = "Привет! {} Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                 update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Бот запущен')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", ephem_explorer))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

