from aiogram.utils import executor
from config import dp
from database import sql_commands
from handlers import start, chat_actions, callback, ban_actions_in_gang


start.register_handlers_start(dp=dp)
callback.register_handlers_callback(dp=dp)
# ban_actions_in_gang.filter_messages()
chat_actions.register_handlers_chat_actions(dp=dp)
async def on_startup(_):
    db = sql_commands.Database()
    db.sql_create_db()
    print("Bot is ready to work!!!")

if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup
                           )
