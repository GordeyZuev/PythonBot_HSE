''' Определение бота '''
from telebot import *
from telebot import types
bot = TeleBot('5439686409:AAE48mBLZ_vimVPpT6nj-uWvArWmcdZD_tE')



''' Вспомогательные Функции '''
def get_name(message):
    # Получаем UserName Пользователя
    return str(message.from_user.first_name + ' ' +  message.from_user.last_name)

def message_normilizer(string):
    # Упрощаем определение строки, все буквы становятся строчными
    return string.lower()
    # string = normal_message(message.text) - обработка строки


''' Вспомогательные переменные '''
greeting_text = ''', Я не очень понимаю, что ты написал.
Попробуй написать '/help', там все должны  рассказать рассказать! '''
menu_text = '''Вот что я умею!
Нажми на одну из кнопок.'''        
help_text = "/start 12312312123123123help"









#Вот здесь нужно делать ответ на кнопки
#@bot.callback_query_handler(func = lambda call: True)
#def answer(call):
#    if call.data == 'ok':
#        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Пыщь')
#        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Пыщь!')

'''
@bot.callback_query_handler(func = lambda call: True)
def menu(call):
    if call.data == 'ok':
        markup_inline = types.InlineKeyboardMarkup(row_width=1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Продолжим!')
        button1 = types.InlineKeyboardButton(text = 'Давай!', callback_data = 'ok')
        button2 = types.InlineKeyboardButton(text = 'Давай!', callback_data = 'ok')
        button3 = types.InlineKeyboardButton(text = 'Давай!', callback_data = 'ok')
        button4 = types.InlineKeyboardButton(text = 'Давай!', callback_data = 'ok')
        button5 = types.InlineKeyboardButton(text = 'Давай!', callback_data = 'ok')
        markup_inline.add(button1,button2,button3,button4,button5)
        bot.send_message(call.message.chat.id, menu_text, reply_markup=markup_inline)
'''




        
''' Приветствие '''
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать ' + get_name(message) + '!')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton('Идем!'))
    
    bot.send_message(message.chat.id, 'Идем Дальше?',reply_markup = markup)
    bot.register_next_step_handler(message, menu_buttons)


@bot.message_handler(content_types=['text'])
def menu_buttons(message):
    string = message_normilizer(message.text)
    if string == 'идем!':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(telebot.types.KeyboardButton('funcq'))
        markup.add(telebot.types.KeyboardButton('funcw'))
        markup.add(telebot.types.KeyboardButton('funce'))
        markup.add(telebot.types.KeyboardButton('funcr'))
        markup.add(telebot.types.KeyboardButton('funct'))
        bot.send_message(message.chat.id,'Сделайте выбор!',reply_markup = markup)
        bot.register_next_step_handler(message, func_choser)
        
@bot.message_handler(content_types=['text'])
def func_choser(message):
    string = message_normilizer(message.text)
    print(string)
    if string == 'funcq':
        bot.register_next_step_handler(message, func1)
    elif string == 'funcw':
        bot.register_next_step_handler(message, func2)
    elif string == 'funce':
        bot.register_next_step_handler(message, func3)
    elif string == 'funcr':
        bot.register_next_step_handler(message, func4)
    elif string == 'funct':
        bot.register_next_step_handler(message, func5)
    else:
        bot.send_message(message.chat.id, 'Не очень понятно, что вы имели ввиду. Попробуйте снова либо введите "/help"') 
        bot.register_next_step_handler(message, func_choser)

        
#bot.send_message(message.chat.id, '~Зачёркнутый~', parse_mode='MarkdownV2')

'''
@bot.message_handler(content_types=['text'])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='Перейти на Яндекс', url='https://ya.ru')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Привет! Нажми на кнопку и перейди в поисковик.', reply_markup=keyboard)
'''

''' Главное Меню ''' 
    

''' Основные Функции '''
@bot.message_handler(content_types=['text'])
def func1(message):
    # Функция - Название
    string = message_normilizer(message.text)
    bot.send_message(message.chat.id, '1')

    
@bot.message_handler(content_types=['text'])
def func2(message):
    # Функция - Название
    string = message_normilizer(message.text)
    bot.send_message(message.chat.id, '2')


@bot.message_handler(content_types=['text'])
def func3(message):
    # Функция - Название
    string = message_normilizer(message.text)
    bot.send_message(message.chat.id, '3')


@bot.message_handler(content_types=['text'])
def func4(message):
    # Функция - Название
    string = message_normilizer(message.text)
    bot.send_message(message.chat.id, '4')


@bot.message_handler(content_types=['text'])
def func5(message):
    # Функция - Название
    string = message_normilizer(message.text)
    bot.send_message(message.chat.id, '5')


### - Постоянное ожидание сообщения
bot.polling(none_stop=True)
###
