from aiogram.types import Message,CallbackQuery
from aiogram import Router,F
from aiogram.filters import Command,CommandStart
import keyboards as kb
import requests as rq
rt=Router()

@rt.message(CommandStart())
async def start(message:Message):
    await message.answer('Добро пожаловать в магазин одежды и обуви!',reply_markup=kb.main)

@rt.callback_query(F.data=='contacts')
async def contacts(callback:CallbackQuery):
    await callback.answer('Вы обратились в поддержку!')
    await callback.message.edit_text('Вот наши контакты\n8988-277-90-20\ntg:asbarovv')

@rt.callback_query(F.data=='catalog')
async def catalog(callback:CallbackQuery):
    await callback.answer('Вы выбрали каталог!')
    await callback.message.edit_text('Выберите категорию товара',reply_markup=kb.catalog)

@rt.callback_query(F.data=='t_shirts')
async def t_shirts_query(callback:CallbackQuery):
    await callback.message.edit_text('Выберите фирму',reply_markup=await kb.t_shirts_fun())

@rt.callback_query(F.data=='trousers')
async def trousers_query(callback:CallbackQuery):
    await callback.message.edit_text('Выберите фирму',reply_markup=await kb.trousers_fun())

@rt.callback_query(F.data=='jackets')
async def jackets_query(callback:CallbackQuery):
    await callback.message.edit_text('Выберите фирму',reply_markup=await kb.jackets_fun())

@rt.callback_query(F.data=='shoes')
async def shoes_query(callback:CallbackQuery):
    await callback.message.edit_text('Выберите фирму',reply_markup=await kb.shoes_fun())

@rt.callback_query(F.data=='to_main')
async def main_query(callback:CallbackQuery):
    await callback.message.edit_text('Выберите категорию товара',reply_markup=kb.catalog)
