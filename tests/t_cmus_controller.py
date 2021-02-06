import unittest
from src import cmus_controller

class TestSet(unittest.TestCase):
    
    """
    Assumes cmus is playing before starting tests
    """

    def __init__(self, *args, **kwargs):
        super(TestSet, self).__init__(*args, **kwargs)
        self.playing = 'playing'
        self.paused = 'paused'
    """
    Status
    """
    def test_1_status(self):
        status = cmus_controller.status()
        self.assertTrue(status == self.paused or self.playing)
    
    """
    Pause
    """
    def test_2_pause(self):
        cmus_controller.pause()
        status = cmus_controller.status()
        self.assertEqual(status, self.paused)

    """
    Play
    """
    def test_4_play(self):
        cmus_controller.play()
        status = cmus_controller.status()
        self.assertEqual(status, self.playing)

    """
    Raw command
    """
    def test_5_raw_command(self):
        cmus_controller.raw_command('player-play')
        status = cmus_controller.status()
        self.assertEqual(status, self.playing)

if __name__=="__main__":
    unittest.main(verbosity=2)