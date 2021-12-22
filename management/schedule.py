from management.fill_schedule_data.fillData import FillSchedule
from dataBase import data
from management.extraModules.verifyEmployee import verifyEmployee
from management.printData import PrintData
import calendar
import time


class Schedule:
    year = eval(time.strftime('%Y'))
    month = eval(time.strftime('%m'))
    day = eval(time.strftime('%d'))

    @staticmethod
    def schedules():
        """lista as agendas de pagamento e escolhe uma"""
        Id = verifyEmployee()
        if Id != -1:
            fill = FillSchedule()
            fill.setScheduleKey()
            key = fill.getKey()
            if key is None:
                return None

            data.scheduleDB[Id] = data.scheduleList[key]
            data.DataBaseManager.writeScheduleDB()
            print('Pagamento agendado com sucesso.')

    @staticmethod
    def newSchedules():
        """cria novas agendas de pagamento"""

        newSchedule = FillSchedule()
        if newSchedule.list() == 1:
            PrintData.printScheduleList()

        newSchedule.setSchedule()
        type_ = newSchedule.getScheduleType()
        day = newSchedule.getDay()
        description = newSchedule.getDescription()

        key = 0
        for key in data.scheduleList:
            pass
        data.scheduleList[key + 1] = [description, type_, day]
        data.DataBaseManager.writeScheduleList()
        print('Agenda criada com sucesso')

    @classmethod
    def currentDay(cls):
        case = calendar.weekday(cls.year, cls.month, cls.day)
        switch = {0: 'segunda-feira', 1: 'terca-feira', 2: 'quarta-feira', 3: 'quinta-feira', 4: 'sexta-feira',
                  5: 'sabado', 6: 'domingo'}
        return switch[case]

    @classmethod
    def monthLastDay(cls):
        lastMonth = calendar.monthrange(cls.year, cls.month)
        return lastMonth[-1]
