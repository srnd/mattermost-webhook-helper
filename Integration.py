import Message


class Integration():
    def __init__(self,hook_url):
        self.hook_url = hook_url

    def send_message(self,message: Message):
        message.send(hook_url=self.hook_url)