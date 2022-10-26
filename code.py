''' Определение бота. Библиотеки '''
import requests
from pyquery import PyQuery as pq
from tqdm import tqdm_notebook
from time import *
import wikipedia

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

from telebot import *
from telebot import types
bot = TeleBot('5439686409:AAE48mBLZ_vimVPpT6nj-uWvArWmcdZD_tE')

owm = OWM('10e402c478e9f587f10e92d183285590')
mgr = owm.weather_manager()





''' Вспомогательные Функции '''
def get_name(message):
    # Получаем UserName Пользователя
    return str(message.from_user.first_name)


def message_normilizer(string):
    # Упрощаем определение строки, все буквы становятся строчными
    return string.lower()
    # string = normal_message(message.text) - обработка строки


''' Вспомогательные переменные '''
greeting_text = '''Я - бот, у меня есть парочку интересных функций, которые тебе могут понравится.
\nИдем покажу?'''

menu_text = '''Ниже представлен список того, что я умею: \n\n• Википедия - Могу вывести значение Слова.
\n• Население Планеты - В реальном времени можно увидеть сколько людей живет на земле.
\n• Новости HSE - Последние актульные новости вышки.
\n• Погода - Узнать погоду в городе.
\n• О боте - Пару слов обо мне.
\nВыбирете Один из Вариантов:'''

help_text = "Не очень хорошо, что тебе понадобилась эта функция. Попробуй ввести /start ."

deleted_num = 0

hse_news_page_num = 2





''' Start и Help '''
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, ' + get_name(message) + '!')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(telebot.types.KeyboardButton('Идем!'))
    
    bot.send_message(message.chat.id, greeting_text,reply_markup = markup)
    bot.register_next_step_handler(message, menu_buttons)
    #print(get_name(message))





''' Главное Меню ''' 
def menu_buttons(message):
    string = message_normilizer(message.text)
    if string == 'идем!' or string == 'в главное меню':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
        button1 = (telebot.types.KeyboardButton('Википедия'))
        button2 = (telebot.types.KeyboardButton('Население Планеты'))
        button3 = (telebot.types.KeyboardButton('Новости HSE'))
        button4 = (telebot.types.KeyboardButton('Погода'))
        button5 = (telebot.types.KeyboardButton('О Боте'))
        markup.add(button1, button2, button3, button4, button5)
    
        bot.send_message(message.chat.id, menu_text, reply_markup = markup)
        bot.register_next_step_handler(message, func_choser)

    else:
        bot.send_message(message.chat.id, 'не очень понятно что вы сказали, но давайте продолжим')
        start(message)




        
''' Обработчик Кнопок ''' 
def func_choser(message):
    string = message_normilizer(message.text)

    if string == 'википедия':
        wikipedia_by_word(message)

    elif string == 'население планеты':
        planet_popuation(message)

    elif string == 'новости hse':
        hse_news(message)

    elif string == 'погода':
        bot_weather(message)
        
    elif string == 'о боте':
        about_bot(message)

    else:
        bot.send_message(message.chat.id, 'Не очень понятно, что вы имели ввиду. Попробуйте снова.') 
        bot.register_next_step_handler(message, func_choser)




        
''' Работа функции Википедия ''' 
def wikipedia_by_word(message):
    bot.send_message(message.chat.id, 'Введите слово или выражение, значение которого вы хотите получить.')
    bot.register_next_step_handler(message, wiki_word_understanding)

def wiki_word_understanding(message):
    string = message_normilizer(message.text)
    wikipedia.set_lang("Ru") 
    wiki_list = (wikipedia.search(string, results = 4))
    if len(wiki_list) == 0:
        bot.send_message(message.chat.id, 'К сожалению, таких запросов на Википедии не найдено. Попробуйте заново.')
        bot.register_next_step_handler(message, wiki_word_understanding)
    else: 
        anslist = 'Ниже список похожих запросов. Выбирете Один из них. \n'
        for i in range(len(wiki_list)):
            anslist += str('• "' + wiki_list[i] + '" \n')
        bot.send_message(message.chat.id, anslist)

        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=1)
        button1 = (telebot.types.KeyboardButton(wiki_list[0]))
        button2 = (telebot.types.KeyboardButton(wiki_list[1]))
        button3 = (telebot.types.KeyboardButton(wiki_list[2]))
        button4 = (telebot.types.KeyboardButton(wiki_list[3]))
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, 'Сделайте выбор!', reply_markup = markup)
        bot.register_next_step_handler(message, wiki_word_difinition)


def wiki_word_difinition(message):
    string = message_normilizer(message.text)
    #bot.send_message(message.chat.id, wikipedia.summary(string))
    try:
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text=string, url=wikipedia.page(string).url)
        keyboard.add(url_button)
        bot.send_message(message.chat.id, '• ' + str(wikipedia.summary(string, sentences = 8)), reply_markup=keyboard)

        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=1)
        button1 = (telebot.types.KeyboardButton('Еще Слово'))
        button2 = (telebot.types.KeyboardButton('В Главное Меню'))
        markup.add(button1, button2)
        bot.send_message(message.chat.id, 'Выберите Действие:', reply_markup = markup)
        bot.register_next_step_handler(message, wiki_next)
    except:
        bot.send_message(message.chat.id, 'С этим запросом, к сожалению, некототорые проблемы. Попробуйте что-нибудь другое.')
        wikipedia_by_word(message)

        
def wiki_next(message):
    string = message_normilizer(message.text)
    if string == 'еще слово':
        wikipedia_by_word(message)
        #print('1')
    elif string == 'в главное меню':
        wiki_quiting(message)
        #print('-1')
    else:
        bot.send_message(message.chat.id, 'Не очень понятно, что вы имели ввиду. Попробуйте снова.')
        #print('0')
        bot.register_next_step_handler(message, wiki_word_difinition)

def wiki_quiting(message):
    menu_buttons(message)




    
''' Работа функции Население Планеты '''
def planet_popuation(message):
    #string = message_normilizer(message.text)
    urlreq = requests.get("https://countrymeters.info/ru/World")
    population = pq(urlreq.text).find("div#cp1").text()
    men_pop = pq(urlreq.text).find("div#cp2").text()
    women_pop = pq(urlreq.text).find("div#cp3").text()
    bot.send_photo(message.chat.id, 'https://rusvesna.su/sites/default/files/styles/orign_wm/public/human-population.jpg')
    bot.send_message(message.chat.id, ' Население земли сейчас составляет:' + '\n ' + population + 2 * '\n' + 'Из Которых: ' + '\nМужчин: \n' + men_pop + '\nЖенщин: \n' + women_pop)

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    button1 = (telebot.types.KeyboardButton('Обновить Данные'))
    button2 = (telebot.types.KeyboardButton('В Главное Меню'))
        
    markup.add(button1, button2)
        
    bot.send_message(message.chat.id, 'Выберите Действие:', reply_markup = markup)
    bot.register_next_step_handler(message, pp_next)


def pp_next(message):
    string = message_normilizer(message.text)
    if string == 'обновить данные':
        pp_refreshing(message)
        bot.delete_message(message.chat.id, message.message_id)
    elif string == 'в главное меню':
        pp_quiting(message)
    else:
        bot.send_message(message.chat.id, 'Не очень понятно, что вы имели ввиду. Попробуйте снова.') 
        bot.register_next_step_handler(message, planet_popuation)


def pp_refreshing(message):
    global deleted_num
    urlreq = requests.get("https://countrymeters.info/ru/World")
    population = pq(urlreq.text).find("div#cp1").text()
    men_pop = pq(urlreq.text).find("div#cp2").text()
    women_pop = pq(urlreq.text).find("div#cp3").text()
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id - 2 - deleted_num, text=  'Население земли сейчас составляет:' + '\n ' + population + 2 * '\n' + 'Из Которых: ' + '\nМужчин: \n' + men_pop + '\nЖенщин: \n' + women_pop)
    bot.register_next_step_handler(message, pp_next)
    deleted_num += 1

           
def pp_quiting(message):
    menu_buttons(message)





''' Работа функции Новости HSE '''

hse_news_page_num = 2
def hse_news(message):
    global hse_news_page_num
    urlreq = requests.get('https://www.hse.ru/news/edu/page' + str(hse_news_page_num // 2) + '.html')

    if hse_news_page_num % 2 == 0:
        nstart = 0
        nfinish = 5
    else:
        nstart = 5
        nfinish = 10
    #print(hse_news_page_num, nstart, nfinish)
    
    for n in range(nstart,nfinish):
        #urlreq = requests.get('https://www.hse.ru/news/page1.html')
        #string = message_normilizer(message.text)
        content = pq(urlreq.text).find('div.post').text().split('\xa0')
        content = (content[n][0:content[n].rfind('.')] + '.').split('\n')

        try:
            if len(content[0].split()) == 1:
                data = (content[0]) + ' ' + (content[1]) + ' ' + content[2]
            else:
                data = (content[0]).split()[1] + ' ' + (content[1]) + ' ' + content[2]

            title = content[3]
            text = content[4]
            
            link = str(pq(urlreq.url).find('a.link.link_dark2.no-visited')).split('</a>')
            link = ('https://www.hse.ru/news/edu' + link[n+1].split('"')[1])

            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text='Ссылка на Ресурс', url=link)
            keyboard.add(url_button)
            bot.send_message(message.chat.id, '• ' + title  + ' (' + data + ').', reply_markup=keyboard)
        except:
            pass
        
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    button1 = (telebot.types.KeyboardButton('Еще Новости'))
    button2 = (telebot.types.KeyboardButton('В Главное Меню'))
        
    markup.add(button1, button2)
        
    bot.send_message(message.chat.id, 'Выберите Действие:', reply_markup = markup)
    bot.register_next_step_handler(message, hse_news_next)  


def hse_news_next(message):
    global hse_news_page_num
    string = message_normilizer(message.text)
    if string == 'еще новости':
        hse_news_page_num += 1
        hse_news(message)
        
    elif string == 'в главное меню':
        hse_news_quiting(message)
        hse_news_page_num = 0
    else:
        bot.send_message(message.chat.id, 'Не очень понятно, что вы имели ввиду. Попробуйте снова.') 
        bot.register_next_step_handler(message, hse_news)


def hse_news_quiting(message):
    menu_buttons(message)





''' Работа функции Погода '''
def bot_weather(message):
    bot.send_message(message.from_user.id, "Введите, пожалуйста, название вашего города.")
    bot.register_next_step_handler(message, weather_city_unserstanding)

@bot.message_handler(content_types=['text'])
def weather_city_unserstanding(message):
    string = message_normilizer(message.text)
    try:
        obs = owm.weather_at_place(string)
        weather = obs.get_weather()
        temp = round(weather.get_temperature("celsius")["temp"] )

        weather_info = "В городе " + string.title() + " сейчас " + weather.get_detailed_status() + "." + "\n"
        weather_info += "Температура около: " + str(temp) + " градусов по цельсию" + "\n"

        if temp <= -20:
            weather_info += "Одевайтесь как можно теплее! На улице очень холодно!"
        elif temp <= 0:
            weather_info += "На улице холодно, не забудьте шапку и шарф."
        elif temp <= 15:
            weather_info += "Погода не такая теплая, не забывайся взять термос с теплым чаем!"
        elif temp >= 25:
            weather_info += "Погода просто шикарная, надевайте что-нибдь легкое!"

    except Exception:
        weather_info = "Не найден город, попробуйте ввести иначе."

    bot.send_message(message.chat.id, weather_info)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    button1 = (telebot.types.KeyboardButton('Другой Город'))
    button2 = (telebot.types.KeyboardButton('В Главное Меню'))
    
    markup.add(button1,button2)
        
    bot.send_message(message.chat.id, 'Выбирете действие:', reply_markup = markup)
    bot.register_next_step_handler(message, bot_weather_next)

    
def bot_weather_next(message):
    string = message_normilizer(message.text)
    if string == 'другой город':
        bot_weather(message)
        
    elif string == 'в главное меню':
        bot_weather_quiting(message)
    else:
        bot.send_message(message.chat.id, 'Не очень понятно, что вы имели ввиду. Попробуйте снова.') 
        bot_weather(message)

def bot_weather_quiting(message):
    menu_buttons(message)
    
    
    
    
    
''' Работа функции О Боте '''
def about_bot(message):
    bot.send_message(message.chat.id, 'Не особо можно много чего тут написать...\n\n' + 'Автор Бота - @WhiteShape \n(Зуев Гордей Зовут)!')
    
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='ГитХаб!', url='https://github.com/GordeyZuev/PythonBot_HSE')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'О процессе создания подробно тут (нажмите на кнопочку ниже).', reply_markup=keyboard)
    
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
    button1 = (telebot.types.KeyboardButton('В Главное Меню'))
    
    markup.add(button1)
        
    bot.send_message(message.chat.id, 'Вернуться в главное меню?', reply_markup = markup)
    bot.register_next_step_handler(message, about_bot_quiting)

def about_bot_quiting(message):
    menu_buttons(message)
    
    
    
    
    
### - Постоянное ожидание сообщения
bot.polling(none_stop = True)
### 
