from aiogram.types import ReplyKeyboardMarkup,\
    KeyboardButton,\
    ReplyKeyboardRemove, \
    InlineKeyboardMarkup, \
    InlineKeyboardButton

b_info = KeyboardButton('❓ Инфо')
b_filter = KeyboardButton('🔎 Найти лекарство')
b_spam = KeyboardButton('⚙ Управление рассылкой')
b_update = KeyboardButton('💾 Получить обновления')


b_go_drugstore = KeyboardButton('🚶‍♂ Перейти в аптеку')
b_availability = KeyboardButton('❔ Наличие в аптеках')
b_analog = KeyboardButton('🔃 Аналоги')
b_price = KeyboardButton('💵 Все цены в миницен')
b_search = KeyboardButton('🔎 Поиск нового лекарства')
b_go_main = KeyboardButton('📃 На главную')


b_on_spam = KeyboardButton('✅ Включить')
b_off_spam = KeyboardButton('❌ Выключить')


b_all_price = KeyboardButton('📈 Все цены лекарства')
b_min_price = KeyboardButton('📉 Минимальная цена во всех аптеках')


b_tvoya_apteka = KeyboardButton('Твоя аптека')
b_minicen = KeyboardButton('Миницен')
b_amur_farma = KeyboardButton('Амур Фармация')
b_monastirev = KeyboardButton('Монастырёв')
b_apteka_ru = KeyboardButton('АптекаРу')
b_planeta = KeyboardButton('Планета Здоровья')
b_back = KeyboardButton('🔙 Вернуться назад')


key_board_search = ReplyKeyboardMarkup(resize_keyboard=True)
key_board_main = ReplyKeyboardMarkup(resize_keyboard=True)
key_board_spam = ReplyKeyboardMarkup(resize_keyboard=True)
key_board_choise = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
key_board_dragstore = ReplyKeyboardMarkup(resize_keyboard=True)


key_board_main.add(b_info).add(b_filter).add(b_spam).add(b_update)
key_board_search.add(b_go_drugstore).add(b_availability).add(b_price, b_analog)
key_board_search.row(b_search, b_go_main)
key_board_spam.add(b_on_spam).add(b_off_spam).add(b_go_main)
key_board_choise.add(b_all_price).add(b_min_price).add(b_go_main)
key_board_dragstore.row(b_tvoya_apteka, b_minicen)\
    .row(b_amur_farma, b_monastirev)\
    .row(b_apteka_ru, b_planeta).row(b_back)


inline_tvoya_apteka = InlineKeyboardButton('Твоя Аптека', url='https://www.tvoyaapteka.ru')
inline_minicen = InlineKeyboardButton('Миницен', url='https://minicen.ru/')
inline_amur_farma = InlineKeyboardButton('АмурФармация', url='https://amurfarma.ru')
inline_monastirev = InlineKeyboardButton('Монастырёв', url='https://monastirev.ru/')
inline_apteka_ru = InlineKeyboardButton('Аптека.Ру', url='https://apteka.ru/')
inline_planeta = InlineKeyboardButton('Планета Здоровья', url='https://planetazdorovo.ru')
inline_key_board_dragstore = InlineKeyboardMarkup()
inline_key_board_dragstore.row(inline_tvoya_apteka, inline_minicen)\
    .row(inline_amur_farma, inline_monastirev)\
    .row(inline_apteka_ru, inline_planeta)