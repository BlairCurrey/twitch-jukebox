# Standard library imports
import subprocess
from pathlib import Path

class CmusController:
    
    song_path = Path('songs')

    def __init__(self):
        pass

    def status(self):
        # need to make this it's own module if I start
        # digging in here for more lines other than status
        result = subprocess.run(['cmus-remote', '-Q'], stdout=subprocess.PIPE)
        result_lines = result.stdout.decode('utf-8').splitlines()
        status = result_lines[0].split("status ")[1]
        return status

    def pause(self):
        subprocess.call(['cmus-remote', '-U'])

    def play(self):
        subprocess.call(['cmus-remote', '-p'])

    def stop(self):
        subprocess.call(['cmus-remote', '-s'])

    def next_(self):
        subprocess.call(['cmus-remote', '-n'])

    def add(self, song):
        path = self.song_path / song
        subprocess.call(['cmus-remote', '-q', path])

    def raw_command(self, text):
        """
        Equivalent to entering command into focused cmus.
        For testing/example purposes only - Do not let users pass 
        text to this function.
        """
        subprocess.call(['cmus-remote', '-C', f'{text}'])