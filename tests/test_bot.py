# Standard library imports
import sys
import unittest

# Local imports
from src.bot import Bot

class BotTestSet(unittest.TestCase):
    def test_1_initiliaze_bot(self):
        bot = Bot('name', 'oauth', 'channel')
        bot.socket.close() # silences unclosed socket warning
        self.assertTrue(bot)

if __name__=="__main__":
    unittest.main(verbosity=2)