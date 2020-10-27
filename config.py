"""
БОТА СОЗДАЛ "CVC" - t.me/cvc_code
"""
from aiogram import types
from sqlite_helper import *
import uuid


bot_token = "" # токен от бота (@BotFather) вставлять в кавычки
admin_id = 123123123 # айди админа
my_qiwi = "79312720081" # номер киви без +





start_m = """
Привет, {} 👋 

Ты попал в лучший бесплатный скам шоп.
"""

main_m = """
Главное меню
"""


profile_m = """
❤️ Пользователь: {}
💸 Количество покупок: 0 
🔑 ID: {}
"""

rules_m = """
Правило #1 - После оплаты ты попадаешь в чс
"""

help_m = """
При проблемах в процессе мамонтизации обращаться к 👉 @cvc_code

"""

categories_m = "Активные категории товаров:"





#  Кнопки для главного меню
def u_main_kb():
    u_main = types.InlineKeyboardMarkup()
    categories_b = types.InlineKeyboardButton(text="📖 Категории", callback_data="categories")
    availability_b = types.InlineKeyboardButton(text="📑 Наличие товаров", callback_data="availability")
    profile_b = types.InlineKeyboardButton(text="👤 Профиль", callback_data="profile")
    rulse_b = types.InlineKeyboardButton(text="🔥 Правила", callback_data="rules")
    help_b = types.InlineKeyboardButton(text="🚨 Помощь", callback_data="help")

    u_main.add(categories_b)
    u_main.add(profile_b)
    u_main.add(rulse_b, help_b)

    return u_main



# КНОПКА ОТМЕНЫ
def u_back_kb():
    u_back = types.InlineKeyboardMarkup()
    back_b = types.InlineKeyboardButton(text="🔙 В главное меню", callback_data="back")
    u_back.add(back_b)

    return u_back


#  Кнопки категорий
def u_categories_kb():
    u_categories = types.InlineKeyboardMarkup()
    for i in get_all_categories():
        u_categories.add(types.InlineKeyboardButton(text=i[2], callback_data="category_" + i[1]))
    u_categories.add(types.InlineKeyboardButton(text="🔙 В главное меню", callback_data="back"))

    return u_categories


#  Вывод кнопок товаров по определенной категории
def u_items_kb(category_id):
    u_items = types.InlineKeyboardMarkup()

    items = get_items(category_id)
    if items != None:
        for i in items:
            u_items.add(types.InlineKeyboardButton(text=i[1], callback_data="item_" + i[1]))
        u_items.add(types.InlineKeyboardButton(text="🔙 В главное меню", callback_data="back"))
        return u_items
    else:
        return None


def u_buy_kb(price):
    pay_url = f"https://qiwi.com/payment/form/99?extra%5B%27account%27%5D={my_qiwi}&amountInteger={price}&amountFraction=0&extra%5B%27comment%27%5D={uuid.uuid4()}&currency=643&blocked%5B0%5D=sum&blocked%5B1%5D=comment&blocked%5B2%5D=account"
    u_items = types.InlineKeyboardMarkup()
    u_items.add(types.InlineKeyboardButton(text="🕸 Перейти к оплате", url=pay_url))
    u_items.add(types.InlineKeyboardButton(text="🔁 Проверить оплату", callback_data="check_payment"))
    u_items.add(types.InlineKeyboardButton(text="Отмена", callback_data="back"))

    return u_items