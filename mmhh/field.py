class Field:
    def __init__(self, title: str, value: str, short: bool = None):
        self.title = title
        self.value = value
        self.short = short
        json = {
            'title': self.title,
            'value': self.value
        }
        if self.short is not None:
            json['short'] = self.short
        self.json = json
