
from html.parser import HTMLParser

class CovidParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.follows_cz = 0
        self.first = True

    def handle_data(self, data):
        if not self.first:
            return
        if self.follows_cz > 0:
            self.follows_cz -= 1
            if self.follows_cz == 0:
                self.data = data
                self.first = False
        elif ("Czechia" in data):
            self.follows_cz = 2

class BazenParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.follows = 0

    def handle_data(self, data):
        if self.follows > 0:
            self.follows -= 1
            if self.follows == 0:
                self.data = data
        elif ("PlaveckÃ½ bazÃ©n: " in data):
            self.follows = 1
