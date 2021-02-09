# Standard library imports
import os

# Third-party imports
from dotenv import load_dotenv

# Local imports
from src.bot import Bot

load_dotenv()

SERVER=os.getenv("SERVER")
PORT=int(os.getenv("PORT"))
OAUTH=os.getenv("OAUTH")
BOT_NAME=os.getenv("BOT_NAME")
CHANNEL=os.getenv("CHANNEL")

if __name__=="__main__":
    bot = Bot(BOT_NAME, OAUTH, CHANNEL)
    bot.connect(SERVER, PORT)
    bot.listen()
