from aiogram.utils import executor
from config import  dp
from handlers import  start, chat_actions, callback, fsm_form,list_polss
from database import sql_commands
from scraper import asyn_limon


start.register_handlers_start(dp=dp)
asyn_limon.register_scraper(dp=dp)
fsm_form.register_handler_fsm_form(dp=dp)
list_polss.register_handler_list_poll(dp=dp)
callback.register_handlers_callback(dp=dp)
chat_actions.register_handlers_chat_actions(dp=dp)
async def on_startup(_):
    db = sql_commands.Database()
    db.sql_create_db()
    print("bot is ready")

if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates= True,
                           on_startup=on_startup
                           )