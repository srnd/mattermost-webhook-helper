import requests


class Message:
    def __init__(self,text: str):
        self.text = text

    def send(self,hook_url):
        json = {
            'text':self.text
        }
        requests.post(url=hook_url,json=json)
