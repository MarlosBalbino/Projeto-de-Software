from dataBase import data
from os import system


class PrintData:

    @staticmethod
    def printDataBase():
        """imprime os dados dos empregados"""
        print(f"{11 * '='} Empregados cadastrados {12 * '='}\n")

        # VERIFICA SE HÁ EMPREGADOS CADASTRADOS
        if not data.dynamicDataBase:
            print('\nNão há empregados cadastrados no sistema\n')
            system('pause')
            return None

        # IMPRIME OS DADOS PESSOAIS DOS EMPREGADOS
        for Id in data.dynamicDataBase:
            print(f'{data.dynamicDataBase[Id].getData()}\n')
        system('pause')

    @staticmethod
    def printTimeCards():
        """imprime os cartões de ponto de todos os empregados"""
        print(f"{14 * '='} Cartões de ponto {15 * '='}\n")

        # VERIFICA SE HÁ CARTÕES DE PONTO
        if not data.dynamicTimeCards:
            print('\nNão há cartões de ponto no sistema\n')
            system('pause')
            return None

        # IMPRIME OS CARTÕES DE PONTO
        for Id in data.dynamicTimeCards:
            emp = data.dynamicDataBase[Id]
            print(f'\n{Id} : {emp.getName()}')
            for timecard in data.dynamicTimeCards[Id]:
                print(f'{timecard}')
        print()
        system('pause')

    @staticmethod
    def printSellResults():
        """imprime os resultados de vendas de todos os empregados"""
        print(f"{12 * '='} Resultados de vendas {13 * '='}\n")

        # VERIFICA SE HÁ RESULTADOS DE VENDAS
        if not data.dynamicSellResults:
            print('\nNão há resultados de vendas no sistema\n')
            system('pause')
            return None

        # IMPRIME OS RESULTADOS DE VENDAS
        for Id in data.dynamicSellResults:
            emp = data.dynamicDataBase[Id]
            print(f'\n{Id} : {emp.getName()}')
            for result in data.dynamicSellResults[Id]:
                print(f'{result}')
        print()
        system('pause')

    @staticmethod
    def printSyndicate():
        """imprime os dados relacionados ao sindicato"""
        print(f"{5 * '='} Empregados vinculados ao sindicato {6 * '='}\n")

        if not data.dynamicSyndicateDB:
            print('\nNão há empregados associados ao sindicato\n')
            system('pause')
            return None

        for syndicateId in data.dynamicSyndicateDB:
            empAux = data.dynamicSyndicateDB[syndicateId]
            Id = empAux.getId()
            emp = data.dynamicDataBase[Id]
            print(emp.getName())
            print(f'{empAux.getData()}\n')

        system('pause')

    @staticmethod
    def printSchedules():
        print(f"{12 * '='} Agendas de pagamento {13 * '='}\n")

        # VERIFICA SE HÁ AGENDAMENTOS
        if not data.scheduleDB:
            print('\nNão há pagamentos agendados no sistema\n')
            system('pause')
            return None

        # IMPRIME OS EMPREGADOS E SUAS RESPECTIVAS AGENDAS
        for Id in data.dynamicDataBase:
            emp = data.dynamicDataBase[Id]
            print(f'\n{Id} : {emp.getName()}')
            print(f'{data.scheduleDB[Id][0]}')
        print()
        system('pause')

    @staticmethod
    def printScheduleList():
        types = {1: 'semanalmente', 2: 'mensalmente', 3: 'bi-mensalmente'}
        print(f"{18*'='} Agendas {18*'='}\n")
        for value in data.scheduleList.values():
            print(f'{value[0]} - {types[value[1]]}')
        print()
        system('pause')

    @staticmethod
    def printPaychecks():
        """imprime os dados relacionados ao sindicato"""
        print(f"{15 * '='} Contracheques {16 * '='}\n")

        if not data.paycheckDB:
            print('\nNão há contracheques registrados\n')
            system('pause')
            return None

        for Id in data.paycheckDB:
            paycheck = data.paycheckDB[Id]
            print(paycheck.payCheck())
            print(paycheck.printDiscounts())
            print()
        system('pause')
