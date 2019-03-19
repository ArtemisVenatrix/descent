class Date:
    def __init__(self, year, month, day, hour, minute):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.units = {"year": self.incYear, "month": self.incMonth, "day": self.incDay, "hour": self.incHour, "minute": self.incMinute}

    def increment(self, unit, amount):
        self.units[unit](amount)

    def incYear(self, amount):
        self.year += amount

    def incMonth(self, amount):
        self.month += amount
        years = (self.month - self.month % 12)/12
        self.month = self.month % 12
        self.incYear(years)

    def incDay(self, amount):
        self.day += amount
        months = (self.day - self.day % 31)/31
        self.day = self.day % 12
        self.incMonth(months)

    def incHour(self, amount):
        self.hour += amount
        days = (self.hour - self.hour % 24)/24
        self.hour = self.hour % 24
        self.incDay(days)

    def incMinute(self, amount):
        self.minute += amount
        hours = (self.minute - self.minute % 60)/60
        self.minute = self.minute % 60
        self.incHour(hours)