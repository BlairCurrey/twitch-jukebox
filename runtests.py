# Standard library imports
import unittest

# Local imports
from tests import test_cmus_controller
from tests import test_bot

if __name__=="__main__":
    test_sets = [
        test_cmus_controller.CmusControllerTestSet(),
        test_bot.BotTestSet()
    ]
    for t in test_sets:
        unittest.main(t,verbosity=2,exit=False)