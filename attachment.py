from typing import Union
from field import Field
from color import Color


class Attachment:
    def __init__(self, text: str, fallback: str = None, color: Union[str, int] = None, pretext: str = None,
                 author_name: str = None, author_link: str = None, author_icon: str = None,
                 fields: Union[Field, list] = None, image_url: str = None, thumb_url: str = None):

        if fallback is None:
            self.fallback = text
