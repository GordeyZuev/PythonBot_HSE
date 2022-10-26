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

# Функционал
**Функций в коде у меня огого...**
Не то чтобы это прям большой плюс, думаю, все таки, что этому поспособствовало не самое быстрое освоение библиотеки telebot, поэтому я зачастую выбирал не самые оптимизированные пути, но старался их исправлять, от чего-то избавляясь или заменяя, но решил, что сокращать количество этих самых функций будет весьма долго. Оставил как есть. 

## Главное Меню
Функция **menu_buttons()** Принимала запрос на использование доступных функций с помощью кнопок. После этого информация передавалась в функцию **func_choser()**, которая в свою очередь обрабатывала ввод и при условии, что все выполнено верно, переходила уже к интересным функциям бота. Если же изначальный запрос был неверным, отправлялся еще один запрос.

## Википедия
**Передем к первой большой функции, которая принесла не мало трудностей - Wikipedia**
Этот блок состоит из нескольких функций, которые занимаются одним делом - выдают определение слова или выражения, которое ввел пользователь.

Первая мини функция - **wikipedia_by_word()**, которая принимала нужное слово / выражение и передавала его дальше, можем назвать ее обработчиком.

Вторая мини функция **wiki_word_understanding()**. Зная английский можно понять, что функция занималась определением введенонго запроса. Тут все не так просто. Сначала создавался массив из 4 похожих нужных значений, которые библиотека вытаскивала из википедии, после чего все значения переделывались в кнопки и пользователь выбирал нужный ему вариант. Если же запрос был слииишком странным, то понятное дело, что похожие запросы просто не находились и размер массива в таком случае - 0, после чего запрос на ввод делался еще раз.

После того как код и мы определили существующее значение, бот приступал к выводу (с помощью функции **wiki_word_difinition()**), который таил в себе небольшие проблемы. Значение выводилось, но, к сожалению, не всегда. Причина этого - несколько значений одного и того же слова и, к примеру - слово капитан (а капитанов у нас огого сколько может быть...). У этого слова изначальное значений, существующее в википедии - Капитан (воинское звание), а библиотека об этом как будто не знает, что и вызывало ошибку, о короторой предупреждался пользователь с помощью try - except. Если же все было нормально, то бот выводил значение.

После этого (с помощью функции **wiki_word_difinition()**) пользователю давалась возможность с помошью все тех же кнопок принять решение что делать дальше - вернуться обратно в меню или узнать значение другого слова. Если пользователь выбирал "еще слово", то его направляло обратно в функцию wiki_word_difinition(), где случалось все описанное до этого. В случае желания вернуться в меню - вызывалась функция **wiki_quiting()**, которая в свою очередь перенаправляла пользователя в главное меню (то есть в menu_buttons()). Возможно вы зададитесь вопросом для чего нужен вызов функции чтобы вызвать функцию, что вроде не очень нужно, ведь есть путь покороче, но иногда при выводе планировалось изменять какие-то значения во вспомогательных функциях, что тоооооже можно было сделать и при вызове заранее, но как-то изначально я думал иначе... В любом случае этот формат Блоков функций вместе с функцией вывода сохранился, что я решил не менять. А ну конечно забыл еще сказать .что если пользо

### 1 
### 2

## Население Планеты
### 1 
### 2

## Новости HSE
### 1 
### 2

## Погода
### 1 
### 2

## О Боте
### 1 
### 2

