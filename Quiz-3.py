from time import *


class Time:
    def __init__(self, hour=0, mine=0, sec=0, msec=0):
        self.hour = hour
        self.mine = mine
        self.sec = sec
        self.msec = msec

    def to_seconds(self):
        self.total_sec = self.hour * 3600 + self.mine * 60 + self.sec + (self.msec / 100)
        return self.total_sec

    def __str__(self):
        return f"{self.hour}:{self.mine}:{self.sec}:{self.msec}"

    @classmethod
    def from_seconds(cls, sec_input):
        hour, mine = divmod(sec_input, 3600)
        mine, sec = divmod(mine, 60)
        sec, msec = divmod(sec, 100)
        return f"{round(hour)}:{round(mine)}:{round(sec)}:{round(msec)}"
        # return f"{strftime('%H:%M:%S', gmtime(sec_input))}"

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __add__(self, other):
        return self.to_seconds() + other.to_seconds()


class DateTime(Time):
    def __init__(self, year, mounth, day, hour, mine, sec=0, msec=0):
        super().__init__(hour, mine, sec=0, msec=0)
        self.year = year
        self.mounth = mounth
        self.day = day

    def to_seconds(self):
        total_sec_new = self.year * 31556926 + self.mounth * 2628000 + self.day * 86400 + self.total_sec
        return total_sec_new

    def __str__(self):
        return f"{self.year}-{self.mounth}-{self.day} {self.hour}:{self.mine}:{self.sec}:{self.msec}"

    @classmethod
    def from_seconds(cls, sec_input):
        year, mounth = divmod(sec_input, 31556926)
        mounth, day = divmod(mounth, 2628000)
        day, hour = divmod(day, 86400)
        hour, mine = divmod(hour, 3600)
        mine, sec = divmod(mine, 60)
        sec, msec = divmod(sec, 100)
        return f"{year}-{mounth}-{day} {hour}:{mine}:{sec}:{msec}"

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __add__(self, other):
        return self.to_seconds() + other.to_seconds()


T = Time(5, 27, 10)
T2 = DateTime(1, 0, 0, 0, 0)
print(T.to_seconds())
print(T)
print(DateTime.from_seconds(31556926))
