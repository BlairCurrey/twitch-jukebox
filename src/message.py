class Message:
    def __init__(self, line):
        # should use a validation before continuing with init
        self.line = line
        self.user = self._get_user()
        self.body = self._get_message()
        self.isCommand = self._isCommand()

    def _get_user(self):
        return self.line.split('!')[0].replace(':', '')

    def _get_message(self):
        return self.line.split(':')[-1]

    def _isCommand(self):
        return self.body.startswith("!")

    # def validate(self, line):
    #     pass

if __name__ == "__main__":
    l = ":nonethewiserer!nonethewiserer@nonethewiserer.tmi.twitch.tv PRIVMSG #nonethewiserer :play"
    m = Message(l)
    print(m)