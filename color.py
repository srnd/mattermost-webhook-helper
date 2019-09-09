class Color:
    def __init__(self,color):
        if type(color) is int and len(color) == 6:
            self.color = '#' + str(color)
        elif type(color) == str:
            if not color.startswith('#') and len(color) == 6:
                self.color = '#' + color
            elif color.startswith('#') and len(color) == 7:
                self.color = color

    def __repr__(self):
        return self.color

    def __str__(self):
        return self.color