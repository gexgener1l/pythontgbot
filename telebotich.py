import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	# sti = open('static/welcome.webp', 'rb')
	# bot.send_sticker(message.chat.id, sti)

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("анекдот")
	# item2 = types.KeyboardButton("😊 Как дела?")

	markup.add(item1) #item2

	bot.send_message(message.chat.id, "Рофлан здарова, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот c лучшими анекдлотами kekw".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

anekdots = ['''Великий философ Фридрих Ницше был добрый и веселый человек.
Один раз он пошел в магазин за хлебом.
Толстая продавщица на хлебном отделе очень любила издеваться над добрым и веселым философом. Ницше терпеть ее не мог и часто называл тупой пиздой.
— Ну что, Ницше, — сказала толстая продавщица, завидев Фридриха. — За хлебом небось прискакал? Любишь хлебушек-то?
— Обожаю, — сдержанно ответил Ницше.
— А ты его пёк, чтобы вот так его жрать? — вкрадчиво спросила вдруг продавщица. — Ты вообще когда-нибудь пёк хлеб? А, Ницше?
— Я? Пёк хлеб? — переспросил Ницше.
— Ты в уши долбишься, Ницше?
— Нет, — сказал Ницше. — На оба вопроса — нет.
Великий философ умел быть лаконичным.
— Вот испеки сначала, а там поговорим, — триумфально закончила продавщица.
— Секундочку, — сказал Ницше. — Если я буду печь хлеб, то нахуя мне тогда, тупая ты пизда, покупать его у тебя?
— Меня, Ницше, твои запарки совершенно не ебут — спокойно парировала продавщица. — Делать мне больше нехуй, как вместе с тобой философствовать. Муку тебе продам. А хлеба — во, — продавщица показала мозолистый кукиш, для убедительности схватив себя за локоть.
Ницше задумался.
— А ты-то, — наконец произнес он, — ты-то сама хлеб пекла?
— Пекла, голубчик, пекла, — сказала продавщица. — Да я столько его выпекла, что ты бы всю жизнь ел, да еще и детям бы твоим осталось.
— У меня нет детей, — сообщил Ницше.
— Это пиздец какой-то, — сказала продавщица. — Детей у него нет, хлеб он печь не умеет и не хочет, а только и знает, что честных продавщиц заебывать.
— Это ты честная продавщица, что ли? — заинтересовался Ницше. — Да у тебя ебало как у Муссолини. У честных людей лица другие.
— А что Муссолини? Чем тебе теперь Муссолини не угодил? Да он, если хочешь знать, тоже хлеб пёк. Эх ты, Ницше.
Ницше неуверенно потоптался на месте.
— Ладно, хуй с ним — махнул он рукой. — Давай сюда свою муку.
— Запомни, Ницше: культура — это лишь тоненькая хлебная корочка над раскаленным хаосом, — довольно сказала продавщица. — Крепко запомни.
— Запомню, — сказал Ницше с ненавистью. — Крепко запомню.

На следующий день Ницше пришёл в тот же магазин.
— Чего тебе? — спросила продавщица.
— Муки давай, сквозь зубы ответил Ницше.
— Что, научился печь?
— Тебя, суку, забыл спросить. Давай муки.
— За такую грубость могу и скалкой по ебальнику… — промямлила продавщица.
— Давай муку, говорю.

Продавщица подала муку.

— А теперь жри.
— Что жрать?
— Муку жри.
— С какого перепугу? Сам жри.
— Я сказал жри, сказал Ницще и опустил продавщицу мордой в муку. — Что, нравится?

Продавщица покорно съела муку и посмотрела на философа испуганными глазами.

— Приятно, да? А я вчера целый вечер это говно жрал.

Ницше так и не научился печь хлеб''','''Приходит мужик к генекологу: Помогите мне, у меня член чешется
-Мой чаще
-Нет мой''',
'''пришёл как то негр с попугаем в бар, и Бармен спрашивает "по чём брал?" попугай отвечает "да вот, бесплатно достался"''',
'''Ползёт как то улитка вокруг бочки, и думает: когда же забор закончится..''',
'''Едут батя с сыном на шестёрке, перевернулись едут на девятке''',
'''встретились наркоман и повар в кафе
повар: видишь стол? это я накрыл
наркоман: ты видишь гномика?
повар: нет
наркоман: это меня накрыло)))''',
'''один раз сын червяк спрашивает маму червяка:мама,а куда папа ушёл?
А мама ему отвечает:с пацанами на рыбалку''',
'''Лысого мужика не могли выгнать из церкви, потому что гонять лысого грех.''',
'''пришёл как то негр с попугаем в бар, и Бармен спрашивает "по чём брал?" попугай отвечает "да вот, бесплатно достался"''',
'''идёт однорукий чел, видит секондхенд и плачет.''',
'''Жил—был царь. И было у него косоглазие. Пошёл он однажды куда глаза глядят и порвался.''',
'''Играли как то евреи в прятки,их быстро спалили''',
'''Почему слепой мальчик выронил мороженное?
Его сбила фура''',
'''Кошка родила двух котят и бабушка чтобы их не перепутать одного назвала барсик,а второго утопила''',
'''в машине еврей боялся нажать газ''',
'''Знаешь сколько евреев поместиться в машине? 2 спереди, 2 сзади , остальные в пепельнице''',
'''мужик в бассейне сделал каменное лицо и утонул.........''',
'''Ко мне подошла девушка - еврейка.
Она сказала, что я ей понравился и попросила мой номер.
Я сказал, что в Казахстане мы пользуемся именами''',
'''Играл я как то с дедом в шахматы, настал его ход, ну он коня и двинул
АХАХАХАХАХ''',
'''Знаете, что видит оптимист на кладбище? одни плюсы ''',
'''Китайцы делают утром зарядку ,а обедом ее продают ''',
'''шел безрукий парень,и никого не трогал ''',
'''Жила в деревне собачка по имени "Новость"
Наступила однажды на мину
Новость разлетелась по всей деревне ''',
'''суицидники странные люди - чем их больше, тем их меньше ''',
'''как избавиться от глистов за 15 дней?
нужно 14 дней подряд есть булку, а на 15 не есть, тогда глист вылезет, чтобы узнать почему булки нет ''',
'''Купил мужик шляпу, а она ему как раз. Купил вторую, а она ему как двa, купил третью но на этот раз музыкальную и она ему как раз два три раз два три ''',
'''Парень бросил свою девушку-колясницу, и отобрал коляску. Угадайте, кто ко мне приполз на коленях? ''',
'''Собрались все гендеры в ресторане и заказали столик на двоих ''',
'''слепой приходит в бар.
знаете что он сказал?
всем привет кого не видел ''',
'''Заходят ветераны в магазин обуви. В-ветераны, П-продавец.В-у вас есть обувь? П-да, какой размер интересует? В-41-45. П-не расслышал. В-Можем повторить ''',
]
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'анекдот':
			bot.send_message(message.chat.id,random.choice(anekdots))
		# elif message.text == '😊 Как дела?':
# str(random.randint(0,100))
		# 	markup = types.InlineKeyboardMarkup(row_width=2)
		# 	item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
		# 	item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

		# 	markup.add(item1, item2)

		# 	bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'чел ты..')

# @bot.callback_query_handler(func=lambda call: True)
#  def callback_inline(call):
# 	try:
# 		if call.message:
# 			if call.data == 'good':
# 				bot.send_message(call.message.chat.id, 'Легенда')
# 			elif call.data == 'bad':
# 				bot.send_message(call.message.chat.id, 'Похуй')

# 			# remove inline buttons
# 			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
# 				reply_markup=None)

# 			# show alert
# 			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
# 				text="go zxc")

# 	except Exception as e:
# 		print(repr(e))

# RUN
bot.polling(none_stop=True)