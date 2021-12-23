import time
import calendar


class Calendar:

    year = eval(time.strftime('%Y'))
    month = eval(time.strftime('%m'))
    day = eval(time.strftime('%d'))

    switch = {0: 'segunda-feira', 1: 'terca-feira', 2: 'quarta-feira', 3: 'quinta-feira', 4: 'sexta-feira',
                 5: 'sabado', 6: 'domingo'}

    @classmethod
    def currentMonthDay(cls):
        return cls.day

    @classmethod
    def currentWeekDay(cls):
        case = calendar.weekday(cls.year, cls.month, cls.day)
        return cls.switch[case]

    @classmethod
    def currentDay(cls):
        currentDay = calendar.weekday(cls.year, cls.month, cls.day)
        return currentDay

    @classmethod
    def lastMonthDay(cls):
        lastMonth = calendar.monthrange(cls.year, cls.month)
        return lastMonth[-1]
