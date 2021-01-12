# from code.classes.load import Load

class Random():

    def __init__(self, data):
        # data from load.py
        self.connection = data.connection

    def get_random(self):
        return self.connection