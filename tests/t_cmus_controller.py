import unittest
from src.cmus_controller import CmusController

class TestSet(unittest.TestCase):
    
    """
    Assumes cmus is playing before starting tests
    """

    def __init__(self, *args, **kwargs):
        super(TestSet, self).__init__(*args, **kwargs)
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
    def test_4_play(self):
        self.cmus_controller.play()
        status = self.cmus_controller.status()
        self.assertEqual(status, self.playing)

    """
    Raw command
    """
    def test_5_raw_command(self):
        self.cmus_controller.raw_command('player-play')
        status = self.cmus_controller.status()
        self.assertEqual(status, self.playing)

if __name__=="__main__":
    unittest.main(verbosity=2)