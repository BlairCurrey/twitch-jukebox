# Standard library imports
import sys
import unittest

# Local imports
from src.cmus_controller import CmusController


class CmusControllerTestSet(unittest.TestCase):
    
    """
    Assumes cmus is playing before starting tests
    """

    def __init__(self, *args, **kwargs):
        super(CmusControllerTestSet, self).__init__(*args, **kwargs)
        self.playing = 'playing'
        self.paused = 'paused'
        self.cmus_controller = CmusController()
    """
    Status
    """
    def test_1_status(self):
        status = self.cmus_controller.status()
        self.assertTrue(status == self.paused or self.playing)
    
    """
    Pause
    """
    def test_2_pause(self):
        self.cmus_controller.pause()
        status = self.cmus_controller.status()
        self.assertEqual(status, self.paused)

    """
    Play
    """
    def test_3_play(self):
        self.cmus_controller.play()
        status = self.cmus_controller.status()
        self.assertEqual(status, self.playing)

    """
    Raw command
    """
    def test_4_raw_command(self):
        self.cmus_controller.raw_command('player-play')
        status = self.cmus_controller.status()
        self.assertEqual(status, self.playing)

if __name__=="__main__":
    unittest.main(verbosity=2)