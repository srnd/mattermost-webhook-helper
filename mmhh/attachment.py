from typing import Union
from .field import Field

import requests
class Attachment:
    def __init__(self, text: str, fallback: str = None, color: Union[str, int] = None, pretext: str = None,
                 author_name: str = None, author_link: str = None, author_icon: str = None,
                 fields: Union[Field, list] = None, image_url: str = None, thumb_url: str = None, title: str = None,
                 title_link: str = None):
        self.json = {}
        if fallback is None:
            fallback = text
        args = locals()
        for arg in args:
            if args[arg] is not None:
                self.json[arg] = args[arg]
        self.json.pop('self')

    def send(self, hook):
        if 'fields' in self.json:
            for idx,field in enumerate(self.json['fields']):
                self.json['fields'][idx] = self.json['fields'][idx].json

        json = {
            'attachments':[self.json]
        }
        requests.post(url=str(hook), json=json)