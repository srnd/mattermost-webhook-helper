import requests


class Message:
    def __init__(self,text: str):
        self.text = text

    def send(self, hook):
        json = {
            'text': self.text
        }
        requests.post(url=str(hook), json=json)