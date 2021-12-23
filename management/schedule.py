from management.fill_schedule_data.fillData import FillSchedule
from dataBase import data
from management.extraModules.verifyEmployee import verifyEmployee
from management.printData import PrintData
from os import system


class Schedule:

    @staticmethod
    def schedules():
        """lista as agendas de pagamento e escolhe uma"""
        print(f"{16 * '='} Escolher agenda {16 * '='}")

        Id = verifyEmployee()
        if Id != -1:
            fill = FillSchedule()
            fill.setScheduleKey()
            key = fill.getKey()
            if key is None:
                return None

            data.scheduleDB[Id] = data.scheduleList[key]
            data.DataBaseManager.writeScheduleDB()
            print('\nPagamento agendado com sucesso.\n')
            system('pause')
            return 1
        system('pause')

    @staticmethod
    def newSchedules():
        """cria novas agendas de pagamento"""
        print(f"{15 * '='} Criar nova agenda {15 * '='}")

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

        print('Agenda criada com sucesso\n')
        system('pause')
        return 1


