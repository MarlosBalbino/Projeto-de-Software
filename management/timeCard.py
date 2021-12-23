import time
from dataBase import data
from employee.hourly import Hourly
from management.extraModules.mytime import Time
from management.fill_employee_data.fillData import FillHourly
from management.extraModules.verifyEmployee import verifyEmployee
from management.undoRedo import UndoRedo


class TimeCard:
    @staticmethod
    def calcWorkingHours(timecards, new_timecard, employee):
        Id = employee.getId()

        def calcExtraWorkingHours(delta_h):
            extra_h = 0
            if delta_h > 8:
                extra_h = delta_h - 8
            return extra_h

        # CALCULA AS HORAS TRABALHADAS NO DIA
        if len(timecards) % 2 != 0:
            last_timecard = timecards[-1]  # pega o último cartão de ponto registrado
            h_final = new_timecard.split()[-1]  # obtém a hora final
            h_initial = last_timecard.split()[-1]  # obtém a hora inicial
            # Δh = hora_final - hora_inicial
            h_final = Time(h_final)
            h_initial = Time(h_initial)
            delta_h = h_final - h_initial
            extra_h = calcExtraWorkingHours(delta_h.getHours())
            employee.setWorkingHours(delta_h.getHours())
            employee.setExtraWorkingHours(extra_h)
            data.dynamicDataBase[Id] = employee
            data.DataBaseManager.writeDataBase()

    @staticmethod
    def setTimeCard():
        """lança um cartão de ponto"""
        Id = verifyEmployee()
        if Id != -1:
            employee = data.dynamicDataBase[Id]
            if type(employee) != Hourly:
                print('Esse empregado não é horista.')
                return None

            try:
                new_timecard = time.strftime('%d/%m/%y %H:%M:%S')
                timecards = []

                # RECUPERA CARTÕES DE PONTO, CASO EXISTAM
                if Id in data.dynamicTimeCards:
                    timecards = data.dynamicTimeCards[Id]
                    TimeCard.calcWorkingHours(timecards, new_timecard, employee)

                # ADICIONA NOVO CARTÃO DE PONTO
                timecards.append(new_timecard)
                data.dynamicTimeCards[Id] = timecards
                data.DataBaseManager.writeTimeCard()
                print('Cartão de ponto adicionado com sucesso!!')
                return 1

            except:
                print('Não foi possível lançar cartão de ponto.')

    @staticmethod
    def setHours():
        Id = verifyEmployee()
        if Id != -1:
            employee = data.dynamicDataBase[Id]
            if type(employee) != Hourly:
                print('Esse empregado não é horista.')
                return None

            fill = FillHourly(init=0)
            fill.setWorkingHours()
            hours = fill.getWorkingHours()

            employee.setWorkingHours(hours)
            data.dynamicDataBase[Id] = employee
            data.DataBaseManager.writeDataBase()

    @staticmethod
    def setExtra():
        Id = verifyEmployee()
        if Id != -1:
            employee = data.dynamicDataBase[Id]
            if type(employee) != Hourly:
                print('Esse empregado não é horista.')
                return None

            fill = FillHourly(init=0)
            fill.setExtraWorkingHours()
            extra_h = fill.getExtraWorkingHours()

            employee.setExtraWorkingHours(extra_h)
            data.dynamicDataBase[Id] = employee
            data.DataBaseManager.writeDataBase()
