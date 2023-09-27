from django.shortcuts import render
from django.conf import settings
from aiogram import Bot, Dispatcher, types, executor
from asgiref.sync import sync_to_async
from logging import basicConfig, INFO

from apps.telegram.models import TelegramUser

# Create your views here.
print(settings.TELEGRAM_BOT_TOKEN)
bot = Bot(settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
basicConfig(level=INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    user = await sync_to_async(TelegramUser.objects.get_or_create)(
        username=message.from_user.username,
        user_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    await message.answer(f"Привет {message.from_user.full_name}!")

billing_buttons = [
    types.InlineKeyboardButton('Удалить', callback_data='delete_order'),
    types.InlineKeyboardButton("Такси", callback_data='taxi_order'),
    types.InlineKeyboardButton("Взять заказ", callback_data='take_order')
]

billing_keyboard = types.InlineKeyboardMarkup().add(*billing_buttons)


@dp.callback_query_handler(lambda call: call.data == 'delete_order')
async def delete_order_button(callback_query: types.CallbackQuery):
    print(callback_query["from"]["id"])
    user = await sync_to_async(TelegramUser.objects.get)(user_id=int(callback_query["from"]["id"]))
    print(user.user_role)
    if user.user_role == "Manager":
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
        await bot.answer_callback_query(callback_query.id, text="Успешно удалено")
    else:
        await bot.answer_callback_query(callback_query.id, text="У вас нет прав на удаления")

@dp.callback_query_handler(lambda call: call.data == 'taxi_order')
async def taxi_order_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Такси")

@dp.callback_query_handler(lambda call: call.data == 'take_order')
async def take_order_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Вы успешно взяли заказ")


async def send_post_billing(id, products, payment_method, payment_code, address, phone, total_price):
    await bot.send_message(-4013644681, f"""Биллинг #{id}
Товары: {products}
Способ оплаты: {payment_method}
Код оплаты: {payment_code}
Адрес: {address}
Номер: {phone}
Цена: {total_price} KGS""",
reply_markup=billing_keyboard)