# Standard library imports
import sys
import unittest

# Local imports
from src.cmus_controller import CmusController

"""
Assumes cmus is playing before starting tests
"""

class CmusControllerTestSet(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CmusControllerTestSet, self).__init__(*args, **kwargs)
        self.cmus_controller = CmusController()
    """
    Status
    """
    def test_1_status(self):
        status = self.cmus_controller.commands.status()
        self.assertTrue(status == "paused" or "playing")

    """
    Play
    """
    def test_2_play(self):
        self.cmus_controller.process("!play")
        status = self.cmus_controller.commands.status()
        self.assertEqual(status, "playing")

    """
    Pause
    """
    def test_3_pause(self):
        self.cmus_controller.process("!pause")
        status = self.cmus_controller.commands.status()
        self.assertEqual(status, "paused")

    """
    Raw command
    """
    def test_4_raw_command(self):
        self.cmus_controller.commands.raw_input('player-play')
        status = self.cmus_controller.commands.status()
        self.assertEqual(status, "playing")

if __name__=="__main__":
    unittest.main(verbosity=2)