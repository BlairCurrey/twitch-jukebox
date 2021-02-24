# Standar library imports
import traceback

# Local imports
from .commands import Commands

class CmusController:
    def __init__(self):
        self.commands = Commands()
    
    def process(self, command):
        command = command.strip()

        if command == "!pause":
            self.commands.pause()
        if command == "!play":
            self.commands.play()
        if command == "!stop":
            self.commands.stop()
        if command == "!next":
            self.commands.next_()
        if command.startswith("!add"):
            try:
                arg = command.split("\"")[1]
                self.commands.add(arg)
            except Exception as exc:
                print(traceback.format_exc())
                print(exc)