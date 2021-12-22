from employee.Imports import *
import os

dynamicDataBase = {}
dynamicTimeCards = {}
dynamicSellResults = {}
dynamicSyndicateDB = {}

scheduleDB = {}
scheduleList = {1: ['toda sexta-feira', 'semanalmente', 'sexta'],
                2: ['ultimo dia do mês', 'mensalmente', 31],
                3: ['a cada duas sextas-feiras', 'bi-mensalmente', 'sexta']}


class DataBaseManager:

    @staticmethod
    def readDataBase():
        try:
            # LÊ OS DADOS DOS PESSOAIS DOS EMPREGADOS
            file = open(f'dataBase\\employees.db', 'r', encoding='utf8')
            global dynamicDataBase
            dynamicDataBase = eval(file.read())
            file.close()

            # LÊ OS CARTÕES DE PONTO DOS HORISTAS
            try:
                global dynamicTimeCards
                file = open(f'dataBase\\timecards.db', 'r', encoding='utf8')
                dynamicTimeCards = eval(file.read())
                file.close()
            except FileNotFoundError:
                pass

            # LÊ OS RESULTADOS DE VENDAS DOS COMISSIONADOS
            try:
                global dynamicSellResults
                file = open(f'dataBase\\sellresults.db', 'r', encoding='utf8')
                dynamicSellResults = eval(file.read())
                file.close()
            except FileNotFoundError:
                pass

            # Lê OS DADOS SINDICAIS
            try:
                global dynamicSyndicateDB
                file = open(f'dataBase\\syndicate.db', 'r', encoding='utf8')
                dynamicSyndicateDB = eval(file.read())
                file.close()
            except FileNotFoundError:
                pass

            # Lê A LISTA DE AGENDAS
            try:
                global scheduleList
                file = open(f'dataBase\\schedule_list.db', 'r', encoding='utf8')
                dbSchedule = eval(file.read())
                file.close()
                for key in dbSchedule:
                    scheduleList[key] = dbSchedule[key]
            except FileNotFoundError:
                pass

            # LÊ AS AGENDAS DOS EMPREGADOS
            try:
                global scheduleDB
                file = open(f'dataBase\\schedule.db', 'r', encoding='utf8')
                scheduleDB = eval(file.read())
                file.close()
            except FileNotFoundError:
                pass

        except FileNotFoundError:
            pass

    @staticmethod
    def writeDataBaseExe(db_name):
        file = open(f"dataBase\\{db_name}.db", 'w', encoding='utf8')
        file.write(f"{eval(db_name)}")
        file.flush()
        file.close()

    @staticmethod
    def writeDataBase():
        file = open(f'dataBase\\employees.db', 'w', encoding='utf8')
        file.write(f"{dynamicDataBase}")
        file.flush()
        file.close()

    @staticmethod
    def writeTimeCard():
        file = open(f'dataBase\\timecards.db', 'w', encoding='utf8')
        file.write(f"{dynamicTimeCards}")
        file.flush()
        file.close()

    @staticmethod
    def writeSellResults():
        file = open(f'dataBase\\sellresults.db', 'w', encoding='utf8')
        file.write(f"{dynamicSellResults}")
        file.flush()
        file.close()

    @staticmethod
    def writeSyndicateDB():
        file = open(f'dataBase\\syndicate.db', 'w', encoding='utf8')
        file.write(f"{dynamicSyndicateDB}")
        file.flush()
        file.close()

    @staticmethod
    def writeScheduleDB():
        file = open(f'dataBase\\schedule.db', 'w', encoding='utf8')
        file.write(f"{scheduleDB}")
        file.flush()
        file.close()

    @staticmethod
    def writeScheduleList():
        file = open(f'dataBase\\schedule_list.db', 'w', encoding='utf8')
        file.write(f"{scheduleList}")
        file.flush()
        file.close()

    @staticmethod
    def eraseDataBase():
        try:
            global dynamicDataBase
            dynamicDataBase = {}
            os.remove('dataBase\\employees.db')
        except OSError:
            pass
        try:
            global dynamicTimeCards
            dynamicTimeCards = {}
            os.remove('dataBase\\timecards.db')
        except OSError:
            pass
        try:
            global dynamicSellResults
            dynamicSellResults = {}
            os.remove('dataBase\\sellresults.db')
        except OSError:
            pass
        try:
            global dynamicSyndicateDB
            dynamicSyndicateDB = {}
            os.remove('dataBase\\syndicate.db')
        except OSError:
            pass
        try:
            global scheduleDB
            scheduleDB = {}
            os.remove('dataBase\\schedule.db')
        except OSError:
            pass
        try:
            global scheduleList
            scheduleList = {}
            os.remove('dataBase\\schedule_list.db')
        except OSError:
            pass


