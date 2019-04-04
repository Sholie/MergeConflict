class Counter(object):

    def __init__(self, name):
        self._name = name
        self._count = 0

    def Increment(self):
        self._count = self._count + 1

    def Reset(self):
        self._count = 0

    def Value(self):
        return self._count



class Clock(object):
    def __init__(self):
        self._hours = Counter("Hours")
        self._minutes = Counter("Minutes")
        self._seconds = Counter("Seconds")

    def Reset(self):
        self._hours.Reset()
        self._minutes.Reset()
        self._seconds.Reset()

    def Tick(self):
        if(self._seconds.Value() < 59):
            self._seconds.Increment()
        else:
            self._seconds.Reset()
            if(self._minutes.Value() < 59):
                self._minutes.Increment()
            else:
                self._minutes.Reset()
                if(self._hours.Value() < 23):
                    self._hours.Increment()
                else:
                    self._hours.Reset()

    def Read(self):
        return str(self._hours.Value()).zfill(2) + ":" + str(self._minutes.Value()).zfill(2) + ":" + str(self._seconds.Value()).zfill(2)




i = 0
j = 0
c = Clock()
while i < 60:
    i += 1
    while j < 60:
        j += 1
        c.Tick()
        print(c.Read())