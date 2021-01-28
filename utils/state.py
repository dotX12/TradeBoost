class State:
    def __init__(self):
        self.array = []
        self.sent = 0

    def add(self, item):
        if item:
            self.array.append(item)

    def remove(self, item):
        self.array.remove(item)

    def not_in(self, item):

        if item not in self.array:
            return True
        else:
            return False

    def add_sent(self):
        self.sent += 1


