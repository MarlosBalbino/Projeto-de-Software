import time
from dataBase import data
from management.mytime import Time
from employee.hourly import Hourly
from management.verifyEmployee import verifyEmployee


class TimeCard:
    @staticmethod
    def calcWorkingHours(timecards, new_timecard, employee):
        Id = employee.getId()

        # CALCULA AS HORAS TRABALHADAS NO DIA
        if len(timecards) % 2 != 0:
            last_timecard = timecards[-1]  # pega o último cartão de ponto registrado
            h_final = new_timecard.split()[-1]  # obtém a hora final
            h_initial = last_timecard.split()[-1]  # obtém a hora inicial
            # Δh = hora_final - hora_inicial
            h_final = Time(h_final)
            h_initial = Time(h_initial)
            delta_h = h_final - h_initial
            employee.setWorkingHours(delta_h.getHours())
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

            except:
                print('Não foi possível lançar cartão de ponto.')