class Counter(object):

    def __init__(self, name):
        self._name = name
        self._count = 0

    def Increment(self):
        self._count = self._count + 1

    def Reset(self):
        self._count = 10 #inital value

    def Value(self):
        return self._count