# PythonBot_HSE
# Вспомогательное
## Библиотеки
**Библиотек для проекта я использовал ровно 4.**
1. Конечно же, самая нужная здесь **telebot** - это API Телеграма, с помощью которого и имелась возможность создать бота.
2 Следующая библиотека - **requests**, которая позваляла заниматься Парсингом.
3. **Библиотека pyown** - Библиотека с API OpenWeatherMap, которая дала возможность работать с погодой.
4. Ну и еще одна библиотека - **wikipedia**. Это в свою очередь API Википедии, которое позволяло работать с поиском нужных значений слов или выражений.


## Переменные
**Вспомогательных переменных у меня не так много.**
Большая часть из них - не самые короткие тексты, что я делал для экономии места в коде.
Из этих переменных - это **greeting text**, **menu_text**, **help_text**.

Другой же тип переменных - для корректной работы функций, которые мы обсудим немного позже.
Из этих переменных - это **deleted_num** и **hse_news_page_num**


## Функции
**Вспомогательные функции тоже имеются.**

Самая часто используемая - **message_normilizer()**, которая обрабатывала каждую введенную строчку и делала все буквы строчными, что позволяло не рассматривать после каждого запроса миллион вариантов написания ввода.

Вторая функция - **get_name()**, которая получала имя и фамилию пользователя через API телеграма. После тестов с разных аккаунтов я понял, что не у всех пользователей есть фамилия у акканта (то есть user_last_name), поэтому пришлось доставать только имя пользователя, что можно было делать и без создания этой функции одной строкой. Но опять же, изначально было два запроса, что экономило бы строчки и время.

Не совсем уверен относятся ли к вспомогательным функция функции **start() и help()**, но я решил их поставить сюда.
Фукнция **start()** регестрирует начала использования бота и его перезапуск и призывала пользователя к действиям!
Функция **help()** помогает пользователю и дает короткую инструкцию что и как делать.


## Функционал
**Функций в коде у меня огого...**
Не то чтобы это прям большой плюс, думаю, все таки, что этому поспособствовало не самое быстрое освоение библиотеки telebot, поэтому я зачастую выбирал не самые оптимизированные пути, но старался их исправлять, от чего-то избавляясь или заменяя, но решил, что сокращать количество этих самых функций будет весьма долго. Оставил как есть. 


### Главное Меню
Функция **menu_buttons()** Принимала запрос на использование доступных функций с помощью кнопок. После этого информация передавалась в функцию **func_choser()**, которая в свою очередь обрабатывала ввод и при условии, что все выполнено верно, переходила уже к интересным функциям бота. Если же изначальный запрос был неверным, отправлялся еще один запрос.


### Википедия
#### Короткое вступление
**Передем к первой большой функции, которая принесла не мало трудностей - Wikipedia**
Этот блок состоит из нескольких функций, которые занимаются одним делом - выдают определение слова или выражения, которое ввел пользователь.
#### Обработчик
Первая мини функция - **wikipedia_by_word()**, которая принимала нужное слово / выражение и передавала его дальше, можем назвать ее обработчиком.

#### Понимание ввода
Вторая мини функция **wiki_word_understanding()**. Зная английский можно понять, что функция занималась определением введенонго запроса. Тут все не так просто. Сначала создавался массив из 4 похожих нужных значений, которые библиотека вытаскивала из википедии, после чего все значения переделывались в кнопки и пользователь выбирал нужный ему вариант. Если же запрос был слииишком странным, то понятное дело, что похожие запросы просто не находились и размер массива в таком случае - 0, после чего запрос на ввод делался еще раз.

#### Вывод значения
После того как код и мы определили существующее значение, бот приступал к выводу (с помощью функции **wiki_word_difinition()**), который таил в себе небольшие проблемы. Значение выводилось, но, к сожалению, не всегда. Причина этого - несколько значений одного и того же слова и, к примеру - слово капитан (а капитанов у нас огого сколько может быть...). У этого слова изначальное значений, существующее в википедии - Капитан (воинское звание), а библиотека об этом как будто не знает, что и вызывало ошибку, о короторой предупреждался пользователь с помощью try - except. Если же все было нормально, то бот выводил значение.

#### - "Что дальше?" - Спросил бот.
После этого (с помощью функции **wiki_quiting()**) пользователю давалась возможность с помошью все тех же кнопок принять решение что делать дальше - вернуться обратно в меню или узнать значение другого слова. Если пользователь выбирал "еще слово", то его направляло обратно в функцию wiki_word_difinition(), где случалось все описанное до этого. В случае желания вернуться в меню - вызывалась функция **wiki_quiting()**, которая в свою очередь перенаправляла пользователя в главное меню (то есть в menu_buttons()). Возможно вы зададитесь вопросом для чего нужен вызов функции чтобы вызвать функцию, что вроде не очень нужно, ведь есть путь покороче, но иногда при выводе планировалось изменять какие-то значения во вспомогательных функциях, что тоооооже можно было сделать и при вызове заранее, но как-то изначально я думал иначе... В любом случае этот формат Блоков функций вместе с функцией вывода сохранился, что я решил не менять. А ну конечно забыл еще сказать, что если пользователь ввел бы неверное слово, то все было бы проверено и неверные вводы бы не допустиись. 

На этом с этим разделом заканчиваем.


### Население Планеты
#### Короткое вступление
Блок функций населения планеты работает немножечко иначе. Он не принимает никаких значений, зачем они ему? Функция работает на парсинге.


#### Первоначальный вывод + *обработка и выход*
У нас есть сайт с населением земли, который обновляется чуть ли не каждые полсекунды. Нам же такое частое обновление не нужно, тем более это много запросов (А мне пару раз блокировался доступ!!! и я не мог понять почему все перестало работать, пока не запустил сайт из браузера сайт, который просто не запускался. К счастью, через час все разблокировалось, но все равно забавно вышло). Я решил что самая первая функция **planet_popuation()** будет выводить нам:

---
1. Красивую картинку земли (почему бы и нет?).
2. Население всей земли.
3. Количество женщин на земле.
4. Количество мужчин на земле.
---

После вывода предлагалось две вещи: выйти в главное меню (с помощью **pp_next()** и **pp_quiting()**), что достаточно скучновато для всего функционала блока функций, поэтому я решил: *"а почему бы мне не сделать обновление информации?"*

#### Обновление информации
Функция **pp_refreshing()** занимается обновлением функции, а как она это делает? Она берет прошлое свое сообщение и редактирует его, вышло классно, как мне показалось. Вдобавок, я решил, чтобы не копились сообщение "Обновить данные" от пользователя, то буду их удалять все тем же ботом, где столкнулся с небольшой проблемой. Удаляя сообщение, бот не удаляет у себя его из запросов пользователя, поэтому редактирование сообщения с населением (редактирование делается по номеру сообщения) не редактировалось (выходила ошибка). Тогда нужно было изменять номер редактирования сообщения. Так выглядит код, где deleted_num - число удаленных сообщений.

```python
bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id - 2 - deleted_num, text=  ...
```

После такого редатирование проходило успешно.

#### Выход в меню
После многократных попыток обновить сообщение с населением земли можно и выйти в главное меню, что я описал кааапельку выше.


### Новости HSE
#### Вступление
Идем Дальше. На очереди Парсинг новостей. Парсинг здесь отличается от парсинга в предыдущем блоке, потому что мы тут достаем огромные текст и ооочень сложными путями (много сплитов, а нужно было еще и понять как тексты сплитать) достаем нужную информацию.

#### Вывод новости
Функция **hse_news()** достаточно огромная.
Начну не с самого начала, а с самого вывода. У нас есть цикл, который выводит по новости. Сначала мы вытаскиваем такой элемент как 'div.post', который представляет собой огромный текст со всей информацией, после чего пытаемся адекватно его разделить и использовать все по отдельности, что выходит у меня с трудом, так как оочень много символом, но вроде как, все получается, а именно, получается достать название новости, дату публикации и текст публикации, который был слишком большим, и я решил его не выставлять сообщением, а лучше добавить кнопку с ссылкой на новость. Это оказалось тоже не так легко, пришлось отдельно парсить через:

```python
 pq(urlreq.url).find('div.post')
```

А не через:
```python
 pq(urlreq.text).find('div.post').text()
```

Как все тексты до этого. Почему? Да потому что на сайте все ссылки скрыты за текстом (то есть гиперссылки), и я не очень знал как этим заниматься, но вроде как вышло. 

Единственная проблема, которая могла возникнуть - так это проблема "распарсивания". Когда я доставал огромный текст вначале, все было нормально в нем структурированно, но на второй и третьей странице уже появлялись проблемы, поэтому я воспользовался здесь try-except, которые выводили только "Исправные новости".

Ну и конечно, что я хотел добавить в начале, но подумал, что не очень вышло бы понятно. Так как на сайте вышки ноовостей много, то там есть разные страницы новостей и приходилось менять изначальную ссылку для парсинга. А так как всего было по 10 новостей на странице, а я выдавал по 5, то надо было прибавлять к заранее созданной переменной (**hse_news_page_num**,которую мы объявляли глобально) по 1 (при еще одном запросе новостей) и смотреть на четность: *Если четное, то выводить первые 5, если нечетное, то - следующие пять*:

```python
if hse_news_page_num % 2 == 0:
    nstart = 0
    nfinish = 5
else:
    nstart = 5
    nfinish = 10
```

Ну и просто делением все той же переменной "перелистывать" страницу новостей:

```python
    urlreq = requests.get('https://www.hse.ru/news/edu/page' + str(hse_news_page_num // 2) + '.html')
```

---
Изначально переменная **hse_news_page_num** = 2, то есть при запросе на еще пять новостей, переменная становилась 3. Страница оставалась той же, тк 3 // 2 = 1, а на странице показывался второй блок из 5 новостей, тк 3 % 2 = 1!
---

Также вместе с *запросом на вывод еще 5 новостей*, можно было еще и запросить *выход в меню*, что делалось кнопкамии обрабатывалось функцией **hse_news_page_num()**, которая в первом случае заново вызывала **hse_news()**, предварительно прибавляя к переменной hse_news_page_num 1 (рассказал выше что за переменная).
#### Обработка дальнейшего действия и выхода
Про **hse_news_page_num()** Рассказал до этого, ну функция **hse_news_quiting()** просто вызывалась при запросе на выход в главное меню и сама вызывала функцию **menu_buttons()**, переходя в меню.

Фух, про новости вроде все.


### Погода
#### Вступление
С этой функции небольшие проблемы, потому что она перестала работать, спустя некоторое время. Стало выдаваться сообщение о том, что запрос выполняется слишком много, поэтому по сути из-за try-except выдается просто сообщение о том, что не получилось найти погоду для этого города((( Очень странно, так как до этого все работало, хотя вроде сам сайт в браузере открывается, хоть и ооооочень долго иногда.

#### Обработчик
Функция **bot_weather()** запрашивает у пользователя название города, который ему нужен. После этого строка передается дальше.

#### Понимание ввода
После принятия строки функция **weather_city_unserstanding()** добывает информацию с помощью библиотеки pyowm, которая является API сайта, на котором можно найти миллион вещей от погоды до направление ветра в селе. Потом узнаем информацию и, работая с ней, выдаем результат температуры и даем совет о том, как лучше одеться. Если же город не нашелся, либо же вышла ошибка, описанная во вступлении, бот просто предупреждает об этом, после чего предлает на выбор два действия с помощью кнопок: *запросить погоду еще в одном городе* и *выйти в главное меню*.

### Думаем что дальше
Функция **bot_weather_next()** обрабатывает то, что мы должны были ввести до этого, то есть выбрать что мы хотим и, при условии, что пользователь желает узнать температуру в другом городе, отправляем его в начало это блока с помощью вызова функции **bot_weather()**, а если пользователь хочет выйти, то вызываем **bot_weather_quiting()**, после чего оказываемся в меню. Также уточню, что в функции **bot_weather_next()**, как и всегда, имеется проверка на правильность ввода.


### О Боте
#### Немного слов о боте
Не думаю, что то много есть чего рассказать, просто есть функция **about_bot()** которая выводит информацию о том, кто сделал бота, выводит сообщение ссылкой, которая ведет на информацию о создании бота (то есть сюда, на гитхаб). Также присутствует кнопка для возвращения в главное меню, нажимая на которую вызывается функция **about_bot_quiting()**, которая, как и во всех 4 предыдущих блоках функций возвращает нас в главное меню.

## Итог

Вроде все рассказал, если есть вопросы - пишите в телеграме @WhiteShape
Ссылка на бота - https://t.me/zuevgordeybot
