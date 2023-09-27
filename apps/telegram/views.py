from django.shortcuts import render
from django.conf import settings
from aiogram import Bot, Dispatcher, types, executor
from asgiref.sync import sync_to_async
from logging import basicConfig, INFO

from apps.telegram.models import TelegramUser, BillingDelivery, BillingDeliveryHistory

# Create your views here.
print(settings.TELEGRAM_BOT_TOKEN)
bot = Bot(settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
basicConfig(level=INFO)

profile_buttons = [
    types.KeyboardButton('Профиль'),
    types.KeyboardButton('Заказы'),
    types.KeyboardButton('Поддержка'),
]
profile_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*profile_buttons)

"""Функция для обработки комманды /start. Если пользователя нету в базе, 
бот создаст его и даст ему поль пользователя.
По желаю можно сделать его курьером"""
@dp.message_handler(commands='start')
async def start(message:types.Message):
    user = await sync_to_async(TelegramUser.objects.get_or_create)(
        username=message.from_user.username,
        user_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        user_role="User"
    )
    await message.answer(f"Привет {message.from_user.full_name}!", reply_markup=profile_keyboard)

""""Фукнция для показа профиля пользователя"""
@dp.message_handler(text="Профиль")
async def get_user_profile(message:types.Message):
    user = await sync_to_async(TelegramUser.objects.get)(user_id=message.from_user.id)
    await message.answer(f"""ВОТ ВАШ ПРОФИЛЬ
Имя: {user.first_name}
Фамилия: {user.last_name}
Имя пользователя: @{user.username}
ID: {message.from_user.id}
Статус пользователя: {user.user_role}""")

billing_buttons = [
    types.InlineKeyboardButton('Удалить', callback_data='delete_order'),
    types.InlineKeyboardButton("Такси", callback_data='taxi_order'),
    types.InlineKeyboardButton("Взять заказ", callback_data='take_order')
]
billing_keyboard = types.InlineKeyboardMarkup().add(*billing_buttons)

order_buttons = [
    types.InlineKeyboardButton('В пути', callback_data="on_road"),
    types.InlineKeyboardButton('Завершить', callback_data="finish_order")
]
order_keyboard = types.InlineKeyboardMarkup().add(*order_buttons)

on_road_buttons = [
    types.InlineKeyboardButton('Завершить', callback_data="finish_order")
]
on_road_keyboard = types.InlineKeyboardMarkup().add(*on_road_buttons)

"""Функция для удаления заказа менеджерами"""
@dp.callback_query_handler(lambda call: call.data == 'delete_order')
async def delete_order_button(callback_query: types.CallbackQuery):
    try:
        user = await sync_to_async(TelegramUser.objects.get)(user_id=int(callback_query["from"]["id"]))
        if user.user_role == "Manager":
            await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
            await bot.answer_callback_query(callback_query.id, text="Успешно удалено")
        else:
            await bot.answer_callback_query(callback_query.id, text="У вас нет прав на удаления")
    except:
        await bot.answer_callback_query(callback_query.id, text="Зарегистрируйтесь в боте /start")

"""Функция для такси (в разработке)"""
@dp.callback_query_handler(lambda call: call.data == 'taxi_order')
async def taxi_order_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Такси")

"""Функция для получения заказа курьером, после нажатия кнопки (Взять заказ)
в базе создается запись и также в личные сообщения приходит сам заказ
где курьер может завершить заказ после получения"""
@dp.callback_query_handler(lambda call: call.data == 'take_order')
async def take_order_button(callback_query: types.CallbackQuery):
    try:
        user = await sync_to_async(TelegramUser.objects.get)(user_id=int(callback_query["from"]["id"]))
        id_billing = callback_query.message.text.split()[1].replace('#', '')
        print(id_billing)
        print(user.id)
        if user.user_role == "Delivery":
            delivery_create = await sync_to_async(BillingDelivery.objects.create)(
                billing_id = int(id_billing),
                telegram_user_id = user.id,
                delivery = "Accepted"
            )
            await bot.edit_message_text(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id,
                text=f"{callback_query.message.text }\nСтатус: Принят курьером @{user.username}",
                # reply_markup=billing_keyboard  # Если вы хотите также обновить клавиатуру
            )
            await bot.answer_callback_query(callback_query.id, text=f"Вы успешно взяли заказ {id_billing}")
            await bot.send_message(user.user_id, f"{callback_query.message.text}", reply_markup=order_keyboard)
        else:
            await bot.answer_callback_query(callback_query.id, text="Вы не можете взять заказ")
    except:
        await bot.answer_callback_query(callback_query.id, text="Зарегистрируйтесь в боте /start")

"""Функиция (В пути) для курьером после того как они успешно получили заказ"""
@dp.message_handler(lambda call: call.data == "on_road")
async def delivery_on_road(callback_query: types.CallbackQuery):
    print("ON ROAD")
    user = await sync_to_async(TelegramUser.objects.get)(user_id=int(callback_query["from"]["id"]))
    id_billing = callback_query.message.text.split()[1].replace('#', '')
    if user.user_role == "Delivery":
        order = await sync_to_async(BillingDelivery.objects.get())(
            id = int(id_billing)
        )
        order.delivery = "On way"
        order.save()
        await bot.edit_message_text(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            text=f"{callback_query.message.text }\nСтатус: В пути курьер @{user.username}",
            reply_markup=on_road_keyboard  # Если вы хотите также обновить клавиатуру
        )
        await bot.answer_callback_query(callback_query.id, text=f"Вы в пути {id_billing}")
    else:
        await bot.answer_callback_query(callback_query.id, text=f"У вас нет прав, свяжитесь с менеджерами")

"""Функция (Завершить) для курьера после того как он успешно выполнил заказ"""
@dp.message_handler(lambda call: call.data == "finish_order")
async def delivery_finish_order(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text=f"Завершить заказ")
    # finish_order

"""Функция для отправки биллинга в телеграм группу"""
async def send_post_billing(id, products, payment_method, payment_code, address, phone, total_price):
    await bot.send_message(-4013644681, f"""Биллинг #{id}
Товары: {products}
Способ оплаты: {payment_method}
Код оплаты: {payment_code}
Адрес: {address}
Номер: {phone}
Итого: {total_price} KGS
Статус: Ожидание курьера""",
reply_markup=billing_keyboard)