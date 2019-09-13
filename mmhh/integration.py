from .message import Message


class Integration:
    def __init__(self,hook_url):
        self.hook_url = str(hook_url)

    def send_message(self, message: Message):
        message.send(hook=self.hook_url)

    def __str__(self):
        return self.hook_url
