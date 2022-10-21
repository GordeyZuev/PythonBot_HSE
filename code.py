''' Определение бота '''
from telebot import *
#from telebot import types
bot = TeleBot('5439686409:AAE48mBLZ_vimVPpT6nj-uWvArWmcdZD_tE')



''' Вспомогательные Функции '''
def get_name(message):
    # Получаем UserName Пользователя
    return str(message.from_user.first_name + ' ' +  message.from_user.last_name)

def message_normilizer(string):
    # Упрощаем определение строки, все буквы становятся строчными
    return string.lower()
    # string = normal_message(message.text) - обработка строки
'''
pas = 0
def command_detector(message):
    global help_text
    global pas
    string = message_normilizer(message.text)
    if string == '/help':
        return help_text
    elif string == '/start':
        return
    else:
        return 0
''' 


''' Вспомогательные переменные '''
greeting_error = """, Я не очень понимаю, что ты написал.
Попробуй написать '/help', там все должны  рассказать рассказать! """
        
help_text = '12312312123123123help'



''' Приветствие '''
@bot.message_handler(content_types=['text'])
def greeting(message):
    greetings = ['/start','привет','добрый день','добрый день','добрый вечер','доброе утро','здравствуй','здравствуйте']
    string = message_normilizer(message.text)
    if string in greetings:
        bot.send_message(message.chat.id, 'Привет, ' + get_name(message) + '!')
        bot.register_next_step_handler(message, Main_menu)
        #bot.send_message(message.chat.id, '~Зачёркнутый~', parse_mode='MarkdownV2')
        
    elif string == '/help':
        bot.register_next_step_handler(message, greeting)
        bot.send_message(message.chat.id, help_text)
        
    else:
        bot.send_message(message.chat.id, get_name(message) + greeting_error)
        bot.register_next_step_handler(message, greeting)
        




''' Главное Меню ''' 
@bot.message_handler(content_types=['text'])
def Main_menu(message):
    #bot.send_message(message.chat.id, get_name(message) + ', ниже представлен список того, что я могу сделать!')
    #string = message_normilizer(message.text)
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True, one_time_keyboard = True)
    keyboard.row('func1', 'func2','func3','func4','func5')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard) 

    
    if string == 'func1':
        bot.register_next_step_handler(message, func1)
    elif string == 'func2':
        bot.register_next_step_handler(message, func2)
    elif string == 'func3':
        bot.register_next_step_handler(message, func3)
    elif string == 'func4':
        bot.register_next_step_handler(message, func4)
    elif string == 'func5':
        bot.register_next_step_handler(message, func5)
    else:
        bot.send_message(message.chat.id, "Не очень понятно, что вы имели ввиду. Попробуйте снова либо введите '/help'") 
        bot.register_next_step_handler(message, Main_menu)
    

''' Основные Функции '''
#@bot.message_handler(content_types=['text'])
def func1(message):
    # Функция - Название
    string = message_normilizer(message.text)
    bot.send_message(message.chat.id, '1')

    
#@bot.message_handler(content_types=['text'])
def func2(message):
    # Функция - Название
    string = message_normilizer(message.text)
    bot.send_message(message.chat.id, '2')


#@bot.message_handler(content_types=['text'])
def func3(message):
    # Функция - Название
    string = message_normilizer(message.text)
    bot.send_message(message.chat.id, '3')


#@bot.message_handler(content_types=['text'])
def func4(message):
    # Функция - Название
    string = message_normilizer(message.text)
    bot.send_message(message.chat.id, '4')


#@bot.message_handler(content_types=['text'])
def func5(message):
    # Функция - Название
    string = message_normilizer(message.text)
    bot.send_message(message.chat.id, '5')


### - Постоянное ожидание сообщения
bot.polling(none_stop=True)
###
