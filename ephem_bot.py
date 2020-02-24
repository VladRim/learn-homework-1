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
import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(bot, update):
    text = "вызван /start"
    print(text)
    print(ephem.earth_radius)
    update.message.reply_text(text)


def ephem_explorer(bot, update):
    #planets = ['Солнце', 'Луна', 'Меркурий', 'Земля', 'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун', 'Плутон']
    planets = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    msg = update.message.text.split(" ")
    planet = msg[1]
    date = '2000/09/09'
    #for pl in planets:
    if msg == 'Sun':
        planet_coordinates = ephem.Sun(date)
    elif msg == 'Moon':
        planet_coordinates = ephem.Moon(date)
    elif msg == 'Mercury':
        planet_coordinates = ephem.Mercury(date)
    elif msg == 'Venus':
        planet_coordinates = ephem.Venus(date)
    elif msg == 'Mars':
        planet_coordinates = ephem.Mars(date)
    elif msg == 'Jupite':
        planet_coordinates = ephem.Jupiter(date)
    elif msg == 'Saturn':
        planet_coordinates = ephem.Saturn(date)
    elif msg == 'Uranus':
        planet_coordinates = ephem.Uranus(date)
    elif msg == 'Neptune':
        planet_coordinates = ephem.Neptune(date)
    else:
        planet_coordinates = ephem.Pluto(date)



    constellation = ephem.constellation(planet_coordinates)

    #calc_data = getattr(ephem, planet)(date)
    #final = ephem.constellation(calc_data)
    print(constellation)


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

