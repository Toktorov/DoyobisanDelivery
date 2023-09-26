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
    types.InlineKeyboardButton("Такси", callback_data='taxi'),
    types.InlineKeyboardButton("Взять заказ", callback_data='order')
]

billing_keyboard = types.InlineKeyboardMarkup().add(*billing_buttons)

async def send_post_billing(id, products, payment_code, address, phone, total_price):
    await bot.send_message(-4013644681, f"""Биллинг #{id}
Товары: {products}
Код оплаты: {payment_code}
Адрес: {address}
Номер: {phone}
Цена: {total_price} KGS""",
reply_markup=billing_keyboard)