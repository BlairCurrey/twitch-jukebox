from dotenv import load_dotenv
import os
import socket
from cmus_controller import *

load_dotenv()

SERVER=os.getenv("SERVER")
PORT=int(os.getenv("PORT"))
OAUTH=os.getenv("OAUTH")
BOT_NAME=os.getenv("BOT_NAME")
CHANNEL=os.getenv("CHANNEL")
OWNER=os.getenv("OWNER")

irc=socket.socket()
irc.connect((SERVER, PORT))
irc.send((  "PASS " + OAUTH + "\n" +
            "NICK " + BOT_NAME + "\n" +
            "JOIN #" + CHANNEL + "\n").encode())

def join_chat():
    loaded = False
    while not loaded:
        # saves 1024 bytes at a time
        readbuffer_join = irc.recv(1024).decode()
        # split into lines and discard last line (empty)
        for line in readbuffer_join.split('\n')[:-1]:
            print(line)
            loaded = check_load_complete(line)

def check_load_complete(line):
    if 'End of /NAMES list' not in line: return False
    print(f'{BOT_NAME} joined {CHANNEL}\'s channel')
    send_message(irc, f'{BOT_NAME} joined the channel')
    return True

def send_message(irc, message):
    message = (f'PRIVMSG #{CHANNEL} :{message}\n').encode()
    irc.send(message)

def get_user(line):
    user = line.split('!')[0].replace(':', '')
    return user

def get_message(line):
    try:
        messsage = line.split(':')[-1]
    except:
        messsage = ""
    return messsage

if __name__=="__main__":
    join_chat()
    while True:
        try:
            readbuffer = irc.recv(1024).decode()
        except:
            readbuffer = ""
        for line in readbuffer.split('\r\n'):
            if line == "":
                continue
            else:
                if line.startswith('PING'):
                    print(line)
                    res = "PONG :tmi.twitch.tv\r\n"
                    irc.send(res.encode())
                    print(res)
                else:
                    message = get_message(line)
                    print(f'{get_user(line)}: {message}')
                    if message == "pause":
                        pause()
                    if message == "play":
                        play()