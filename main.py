# Подключение модуля для Телеграма
import telebot
# Указание токена
bot = telebot.TeleBot('5306367079:AAFoHb4twE5rlH5HoSl6pEaIZN9oDRQSSE0')
# Импорт типов из модуля, чтобы создавать кнопки
from telebot import types
# Импорт цитат из модуля
import quote
# Подключение модуля случайных чисел
import random


# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «ты пидор»
    if message.text == "ты пидор" or message.text == "Ты пидор":
        # Установка приветствия
        bot.send_message(message.from_user.id,
                         "Привет, сейчас ты почитаешь цитаты от людей, решивших найти средство против "
                         "несправедливости и лицемерия общества.")
        # Подготовка кнопок
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого автора
        key_carlin = types.InlineKeyboardButton(text='Карлин', callback_data='Сarlin')
        # Добавление кнопки на экран
        keyboard.add(key_carlin)
        key_ranevskaya = types.InlineKeyboardButton(text='Раневская', callback_data='Ranevskaya')
        keyboard.add(key_ranevskaya)
        # Установка всех кнопок сразу и написание сообщения о выборе
        bot.send_message(message.from_user.id, text='Выбери автора', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши \"ты пидор\"")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажата одна из кнопок — выводим цитату
    if call.data == "Сarlin":
        # Формирование цитат
        msg = random.choice(quote.carlin_list)
        # Отправка текста в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "Ranevskaya":
        # Формирование цитат
        msg = random.choice(quote.ranevskaya_list)
        # Отправка текста в Телеграм
        bot.send_message(call.message.chat.id, msg)


# Запуск постоянного опроса бота в Телеграме
bot.polling(none_stop=True, interval=0)
#