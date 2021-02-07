import socket
import traceback
from cmus_controller import CmusController

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
                user, message = self._get_user_and_message(line)
                print(f'{user}: {message}')
                if user == self.channel:
                    if message == "!pause":
                        self.cmus_controller.pause()
                    if message == "!play":
                        self.cmus_controller.play()
                    if message == "!stop":
                        self.cmus_controller.stop()
                    if message == "!next":
                        self.cmus_controller.next_()
                    if message.startswith("!add"):
                        try:
                            arg = message.split("\"")[1]
                            self.cmus_controller.add(arg)
                        except Exception as exc:
                            print(traceback.format_exc())
                            print(exc)

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

    def _get_user_and_message(self, line):
        user = line.split('!')[0].replace(':', '')
        message = line.split(':')[-1]
        return user, message

if __name__=="__main__":
    pass