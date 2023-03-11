import keyboard as keyboard
from aiogram import types, Dispatcher
from create_bot import dp
from keyboards import key_board_main,\
    key_board_search,\
    key_board_spam,\
    key_board_choise,\
    inline_key_board_dragstore,\
    key_board_dragstore
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from parsers import collector


async def send_welcome(message: types.Message):
    await message.answer("Привет!\nЯ бот Фармацевт!\nЯ помогу тебе найти лекарства.", reply_markup=key_board_main)


class FSMDrag(StatesGroup):
    nameDrag_all = State()
    nameDrag_min = State()


class FSMMenu(StatesGroup):
    choise_menu = State()


@dp.message_handler(state=FSMDrag.nameDrag_all)
async def load_name_drag_all(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    str = collector.print_price(data['name'])
    if len(str) > 4096:
        for x in range(0, len(str), 4096):
            await message.answer(str[x:x + 4096], reply_markup=key_board_search)
    else:
        await message.answer(str, reply_markup=key_board_search)
    await state.finish()
    await FSMMenu.choise_menu.set()
    async with state.proxy() as data:
        data['name'] = message.text
        data['type'] = 'all'


@dp.message_handler(state=FSMDrag.nameDrag_min)
async def load_name_drag_min(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer(collector.print_min_price(data['name']), reply_markup=key_board_search)
    await state.finish()
    await FSMMenu.choise_menu.set()
    async with state.proxy() as data:
        data['name'] = message.text
        data['type'] = 'min'


async def echo(message: types.Message, state: FSMContext):
    if message.text == '❓ Инфо':
        await message.answer("1. Предупреждения:\n"
"   • Поиск аналогов лекарств производит сторонний ресурс, бот не является врачом, перед покупкой аналога, проконсультируйтесь с врачом;\n"
"   • В разных аптеках сети «Миницен» на одно и тоже лекарство цена может отличатся;\n"
"   • Поиск лекарств в сети «Миницен» производится по адресу Зейская, 182, поскольку данный филиал является самым крупным в городе;\n"
"   • Цены актуальны только при заказе онлайн;\n"
"3. Правила поиска:\n"
"   Шаг 1: в главном меню выбрать пункт «Найти лекарство»\n"
"   Шаг 2: выбрать «Все цены лекарства» в случае, если вам необходимо посмотреть все совпадения по вашему поиску или «Минимальная цена во всех аптеках», если хотите найти минимальную цену искомого лекарства (подходит для более точного поиска с указанием дополнительных атрибутов, например: тбл, в/в, 25мг)\n"
"   Шаг 3: после выбора условий поиска, необходимо с помощью отобразившийся клавиатуры написать название и при необходимости нужные атрибуты искомого лекарства.\n"
"Поиск займёт некоторое время, после чего бот выведет результаты поиска и отобразит меню действий.\n"
"   Шаг 4: действия после поиска:\n"
"      • если необходимо посмотреть наличие лекарства в определённой аптеке, нужно выбрать пункт меню «Наличие в аптеках», после чего выбрать нужную аптеку (работает только при поиске минимальных цен в аптеках).\n"
"      • В разных филиалах сети аптек «миниецен», разные цены на одни и те же лекарства, для того чтобы отобразить цены во всех филиалах, используйте кнопку «Все цены в миницен»\n"
"      • Чтобы бот подобрал вам аналоги лекарства, воспользуйтесь пунктом меню «Аналоги»\n"
"      •  Для того чтобы перейти в одну из аптек, выберите «перейти в аптеку», бот отправит сообщение с кнопками для перехода в аптеки.\n"
"      • Для поиска нового лекарства нажмите на кнопку «Поиск нового лекарства», далее см. Шаг 2.\n"
"      • После завершения поиска выберите пункт меню «На главную».")

    elif message.text == '⚙ Управление рассылкой':
        await message.answer("Настройки рассылки", reply_markup=key_board_spam)
    elif message.text == '💾 Получить обновления':
        await message.answer("Все обновления получены!", reply_markup=key_board_main)
    elif message.text == '🔎 Найти лекарство' or message.text == '🔎 Поиск нового лекарства':
        await message.answer('Что вас интересует?', reply_markup=key_board_choise)
        await state.finish()
    elif message.text == '📈 Все цены лекарства':
        await FSMDrag.nameDrag_all.set()
        await message.answer('Напиши название лекарства, которое необходимо найти')
    elif message.text == '📉 Минимальная цена во всех аптеках':
        await FSMDrag.nameDrag_min.set()
        await message.answer('Напиши название лекарства, которое необходимо найти')
    elif message.text == '📃 На главную':
        current_state = await state.get_state()
        if current_state is None:
            await message.answer('Главная', reply_markup=key_board_main)
            return
        await state.finish()
        await message.answer('Главная', reply_markup=key_board_main)
    elif message.text == '✅ Включить':
        await message.answer("Настройки рассылки", reply_markup=key_board_spam)
    elif message.text == '❌ Выключить':
        await message.answer("Настройки рассылки", reply_markup=key_board_spam)
    elif message.text == 'Вернуться назад':
        await message.answer('Меню', reply_markup=key_board_search)
    else:
        await message.answer("Я не понимаю")


async def echo_menu(message: types.Message, state: FSMContext):
    if message.text == '🔎 Найти лекарство' or message.text == '🔎 Поиск нового лекарства':
        await message.answer('Что вас интересует?', reply_markup=key_board_choise)
        await state.finish()

    elif message.text == '🚶‍♂ Перейти в аптеку':
        await message.answer("Ссылки на аптеки", reply_markup=inline_key_board_dragstore)

    elif message.text == '❔ Наличие в аптеках':
        async with state.proxy() as data:
            if data['type'] == 'min':
                await message.answer('Какая аптека вас интересует', reply_markup=key_board_dragstore)
            else:
                await message.answer('Наличие можно посмотреть только при поиске минимальных цен.',
                                     reply_markup=key_board_search)

    elif message.text == '🔃 Аналоги':
        async with state.proxy() as data:
            await message.answer(collector.print_analog(data['name']), reply_markup=key_board_search)

    elif message.text == '💵 Все цены в миницен':
        async with state.proxy() as data:
            await message.answer(collector.print_minicen(data['name'], data['type']), reply_markup=key_board_search)

    elif message.text == '📃 На главную':
        current_state = await state.get_state()
        if current_state is None:
            await message.answer('Главная', reply_markup=key_board_main)
            return
        await state.finish()
        await message.answer('Главная', reply_markup=key_board_main)

    elif message.text == '🔙 Вернуться назад':
        await message.answer('Меню', reply_markup=key_board_search)

    elif message.text == 'Твоя аптека':
        async with state.proxy() as data:
            await message.answer(collector.print_availability(data['name'], 'Твоя аптека'),
                                 reply_markup=key_board_search)

    elif message.text == 'Миницен':
        async with state.proxy() as data:
            await message.answer(collector.print_availability(data['name'], 'Миницен'),
                                 reply_markup=key_board_search)

    elif message.text == 'АптекаРу':
        await message.answer("🏥Аптека.РУ🏥"
                             "\nВ данной аптеки можно оформить только под заказ."
                             "\nПримерное время доставки 6 - 10 дней.", reply_markup=key_board_search)

    elif message.text == 'Монастырёв':
        async with state.proxy() as data:
            await message.answer(collector.print_availability(data['name'], 'Монастырёв'),
                                 reply_markup=key_board_search)

    elif message.text == 'Амур Фармация':
        async with state.proxy() as data:
            await message.answer(collector.print_availability(data['name'], 'Амур Фармация'),
                                 reply_markup=key_board_search)
    else:
        await message.answer("Я не понимаю")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['старт', 'start'])
    dp.register_message_handler(echo, state=None)
    dp.register_message_handler(echo_menu, state=FSMMenu.choise_menu)


# medicines = ['кагоцел', 'ношпа', 'снуп', 'ромашка', 'детралекс', 'аспирин',
#              'парацетамол', 'тизин', 'отривин', 'ацц', 'анвимакс', 'диазалин',
#              'кагоцел', 'кагоцел', 'кагоцел', 'БГПУ', '.', ' ']
# number_test = 0
#
#
# def test():
#     global number_test #знаю что так нехорошо делать
#     for elem in medicines:
#         number_test += 1
#         dp.send_message(elem)
#
#
# @dp.message_handler(content_types=["text"])
# def repeat_all_messages(message):
#     if medicines[number_test] in message:
#         dp.send_message('Бот нашёл совпадения')
#     else:
#         dp.send_message('Совпадений нет')