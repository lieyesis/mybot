from aiogram import Bot, Dispatcher, types
from database import Database
from dotenv import load_dotenv
import os


load_dotenv()


token = os.getenv('TOKEN')
bot = Bot(token = token)
dp = Dispatcher()
database = Database("db.sqlite3")