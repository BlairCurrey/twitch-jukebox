# Standard library imports
import subprocess
from pathlib import Path

class Commands:
    
    _song_path = Path('songs')

    @staticmethod
    def status():
        # need to make this it's own module if I start
        # digging in here for more lines other than status
        result = subprocess.run(['cmus-remote', '-Q'], stdout=subprocess.PIPE)
        result_lines = result.stdout.decode('utf-8').splitlines()
        status = result_lines[0].split("status ")[1]
        return status

    @staticmethod
    def pause():
        subprocess.call(['cmus-remote', '-U'])

    @staticmethod
    def play():
        subprocess.call(['cmus-remote', '-p'])

    @staticmethod
    def stop():
        subprocess.call(['cmus-remote', '-s'])

    @staticmethod
    def next_():
        subprocess.call(['cmus-remote', '-n'])

    @staticmethod
    def add(song):
        path = Commands._song_path / song
        subprocess.call(['cmus-remote', '-q', path])

    @staticmethod
    def raw_input(text):
        """
        Equivalent to entering command into focused cmus.
        For testing/example purposes only - Do not let users pass 
        text to this function.
        """
        subprocess.call(['cmus-remote', '-C', f'{text}'])