from Counter import *

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
            #self._seconds.Reset()
            if(self._minutes.Value() < 59):
                self._minutes.Increment()
            else:
                self._minutes.Reset()
                if(self._hours.Value() < 23):
                    self._hours.Increment()
                elif(self._hours.Value()>40):
                   self._hours.Reset()

    def Read(self):
        return str(self._hours.Value()).zfill(2) + ":" + str(self._minutes.Value()).zfill(2) + ":" + str(self._seconds.Value()).zfill(2)