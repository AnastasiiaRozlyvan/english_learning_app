import typing

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.executor import start_webhook

from fastapiclient import FastAPIClient
from config import SECRET, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT

bot = Bot(token=SECRET, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

topics_cb = CallbackData('topic', 'id', 'action')
fast_api_client = FastAPIClient()


async def get_keyboard() -> types.InlineKeyboardMarkup:
    """
    Generate keyboard with list of topics
    """
    markup = types.InlineKeyboardMarkup()

    for topic in await fast_api_client.get('topics'):
        markup.add(
            types.InlineKeyboardButton(
                topic,
                callback_data=topics_cb.new(id=topic, action='learn')
            ),
        )
    return markup


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await fast_api_client.post("users", {"name": message.from_user.username})
    await message.reply(
        'What topic would you like to learn?',
        reply_markup=await get_keyboard()
    )


@dp.callback_query_handler(topics_cb.filter(action='learn'))
async def query_learn(
        query: types.CallbackQuery, callback_data: typing.Dict[str, str]
):
    topic = callback_data['id'].lower()

    text = f"Nice choice, {query.from_user.first_name}! " \
           f"\nLet's learn everything about {topic}."

    await query.message.edit_text(text)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )
