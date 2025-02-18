from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from requests import t_shirts_req,trousers_req,jackets_req,shoes_req
main=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог',callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина',callback_data='basket'),
     InlineKeyboardButton(text='Поддержка',callback_data='contacts')],
])


catalog=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Футболки',callback_data='t_shirts'),
    InlineKeyboardButton(text='Брюки',callback_data='trousers')],
    [InlineKeyboardButton(text='Куртки',callback_data='jackets'),
    InlineKeyboardButton(text='Обувь',callback_data='shoes')],
])

async def t_shirts_fun():
    all_shirts=await t_shirts_req()
    keyboard_ts=InlineKeyboardBuilder()
    for ts in all_shirts:
        keyboard_ts.add(InlineKeyboardButton(text=ts.name,callback_data=f'ts_{ts.id}'))
    keyboard_ts.add(InlineKeyboardButton(text='На главную',callback_data='to_main'))
    return keyboard_ts.adjust(2).as_markup()

async def trousers_fun():
    all_trousers=await trousers_req()
    keyboard_trousers=InlineKeyboardBuilder()
    for tr in all_trousers:
        keyboard_trousers.add(InlineKeyboardButton(text=tr.name,callback_data=f'tr_{tr.id}'))
    keyboard_trousers.add(InlineKeyboardButton(text='На главную',callback_data='to_main'))
    return keyboard_trousers.adjust(2).as_markup()

async def jackets_fun():
    all_jackets=await jackets_req()
    keyboard_jack=InlineKeyboardBuilder()
    for jk in all_jackets:
        keyboard_jack.add(InlineKeyboardButton(text=jk.name,callback_data=f'jk_{jk.id}'))
    keyboard_jack.add(InlineKeyboardButton(text='На главную',callback_data='to_main'))
    return keyboard_jack.adjust(2).as_markup()

async def shoes_fun():
    all_shoes=await shoes_req()
    keyboard_sh=InlineKeyboardBuilder()
    for sh in all_shoes:
        keyboard_sh.add(InlineKeyboardButton(text=sh.name,callback_data=f'sh_{sh.id}'))
    keyboard_sh.add(InlineKeyboardButton(text='На главную',callback_data='to_main'))
    return keyboard_sh.adjust(2).as_markup()

