#REFERENCE: "https://blog.ashija.net/2017/03/29/post-888/"

class Cyclist:
    def __init__(self, list):
        self.i = 0
        self.list = list
 
    def next(self):
        self.i = (self.i + 1) % len(self.list)
        return self.list[self.i]
 
    def previous(self):
        self.i = (self.i - 1 + len(self.list)) % len(self.list)
        return self.list[self.i]
 
    def present(self):
        return self.list[self.i]
 
    def reset(self):
        self.i = 0
        return