from management.fill_schedule_data.fillData import FillSchedule
from dataBase import data
from management.extraModules.verifyEmployee import verifyEmployee
from management.undoRedo import UndoRedo
from management.printData import PrintData


class Schedule:

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
            return 1

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
        return 1


