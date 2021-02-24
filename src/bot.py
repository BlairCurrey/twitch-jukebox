# Standard library imports
import socket

# Local imports
from .cmus_controller import CmusController
from .message import Message

class Bot:
    def __init__(self, name, oauth, channel):
        self.name = name
        self.oauth = oauth
        self.channel = channel
        self.socket = socket.socket()
        self.cmus_controller = CmusController()

    def listen(self):
        while True:
            read_buffer = self._get_response()
            line = read_buffer.strip('\n').strip('\r')

            if line.startswith('PING'):
                print(f'<< {line}')
                res = "PONG :tmi.twitch.tv\r\n"
                self.socket.send(res.encode())
                print(f'>> {res}')
            else:
                msg = Message(line)
                print(f'{msg.user}: {msg.body}')
                if msg.isCommand:
                    self.cmus_controller.process(msg.body)

    def connect(self, server, port):
        self.socket.connect((server, port))
        self.socket.send(( "PASS " + self.oauth + "\n" +
                            "NICK " + self.name + "\n" +
                            "JOIN #" + self.channel + "\n").encode())
        self._wait_until_joined()
        self._send_message(f'{self.name} joined the channel')

    def _wait_until_joined(self):
        joined = False
        while not joined:
            read_buffer = self._get_response()
            for line in read_buffer.split('\n')[:-1]:
                print(line)
                joined = 'End of /NAMES list' in line
        print(f'{self.name} joined {self.channel}\'s channel')

    def _get_response(self):
        buffer_size = 1024
        return self.socket.recv(buffer_size).decode()

    def _send_message(self, message):
        message = (f'PRIVMSG #{self.channel} :{message}\n').encode()
        self.socket.send(message)