"""
БОТА СОЗДАЛ "CVC" - t.me/cvc_code
"""
from aiogram import Bot, Dispatcher, executor
from config import *
from subprocess import Popen
import sys
from sqlite_helper import *



Popen([sys.executable, 'manage.py', 'runserver'])
bot = Bot(bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message):
	add_user(message.chat.id)
	await bot.send_message(message.chat.id, start_m.format(message.from_user.first_name), reply_markup=u_main_kb())


@dp.callback_query_handler(lambda c:True)
async def profile(message):
	data = message.data
	uid = message.from_user.id
	mid = message.message.message_id


	if data == "back":
		await bot.edit_message_text(main_m, uid, mid, reply_markup=u_main_kb())

	elif data == "rules":
		await bot.edit_message_text(rules_m, uid, mid, reply_markup=u_back_kb())

	elif data == "help":
		await bot.edit_message_text(help_m, uid, mid, reply_markup=u_back_kb())

	elif data == "profile":
		await bot.edit_message_text(profile_m.format(message.from_user.username, uid), uid, mid, reply_markup=u_back_kb())

	elif data == "categories":
		await bot.edit_message_text(categories_m, uid, mid, reply_markup=u_categories_kb())

	elif data.startswith("category_"):
		category_id = data.split("_")[1]
		category_result = is_category_exists(category_id)

		if category_result != False:

			items_result = u_items_kb(category_id)
			if items_result != None:
				await bot.edit_message_text(category_result, uid, mid, reply_markup=items_result)
			else:
				await bot.send_message(uid, "В этой категории у нас пока нет товаров.")

		else:
			await bot.send_message(uid, "Такой категории нет.")

	elif data.startswith("item_"):
		item_title = data.split("_")[1]
		item_result = is_item_exists(item_title)

		if item_result != None:
			await bot.edit_message_text(f"Название товара: <b>{item_result[1]}</b>\nЦена - <b>{item_result[3]}₽</b>", uid, mid, reply_markup=u_buy_kb(item_result[3]), parse_mode="HTML")

		else:
			await bot.send_message(uid, "Такого товара больше него")

	elif data == "check_payment":
		await bot.send_message(uid, "Платеж не найден. Попробуй еще раз через 30 секунд.")




executor.start_polling(dp, skip_updates=False)