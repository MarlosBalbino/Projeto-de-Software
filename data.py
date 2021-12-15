from employee import *

dynamicDataBase = {}
dynamicTimeCards = {}
dynamicSellResults = {}


class DataBaseManager:

    @staticmethod
    def readDataBase():
        try:
            # LÊ OS DADOS DOS PESSOAIS DOS EMPREGADOS
            dataBaseFile = open(f'dataBase\\employees.db', 'r', encoding='utf8')
            global dynamicDataBase
            dynamicDataBase = eval(dataBaseFile.read())
            dataBaseFile.close()

            try:
                # LÊ OS CARTÕES DE PONTO DOS HORISTAS
                global dynamicTimeCards
                timeCardFile = open(f'dataBase\\timecards.db', 'r', encoding='utf8')
                dynamicTimeCards = eval(timeCardFile.read())
                timeCardFile.close()
            except FileNotFoundError:
                pass

            try:
                # LÊ OS RESULTADOS DE VENDAS DOS COMISSIONADOS
                global dynamicSellResults
                sellResultsFile = open(f'dataBase\\sellresults.db', 'r', encoding='utf8')
                dynamicSellResults = eval(sellResultsFile.read())
                sellResultsFile.close()
            except FileNotFoundError:
                pass

        except FileNotFoundError:
            pass

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


