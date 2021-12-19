from dataBase import data


class PrintData:

    @staticmethod
    def printDataBase():
        """imprime os dados dos empregados"""

        # VERIFICA SE HÁ EMPREGADOS CADASTRADOS
        if not data.dynamicDataBase:
            print('Não há empregados cadastrados no sistema')
            return None

        # IMPRIME OS DADOS PESSOAIS DOS EMPREGADOS
        for Id in data.dynamicDataBase:
            print(f'{data.dynamicDataBase[Id].getData()}\n')

    @staticmethod
    def printTimeCards():
        """imprime os cartões de ponto de todos os empregados"""

        # VERIFICA SE HÁ CARTÕES DE PONTO
        if not data.dynamicTimeCards:
            print('Não há cartões de ponto no sistema')
            return None

        # IMPRIME OS CARTÕES DE PONTO
        for Id in data.dynamicTimeCards:
            emp = data.dynamicDataBase[Id]
            print(f'\n{Id} : {emp.getName()}')
            for timecard in data.dynamicTimeCards[Id]:
                print(f'{timecard}')
        print()

    @staticmethod
    def printSellResults():
        """imprime os resultados de vendas de todos os empregados"""

        # VERIFICA SE HÁ RESULTADOS DE VENDAS
        if not data.dynamicSellResults:
            print('Não há resultados de vendas no sistema')
            return None

        # IMPRIME OS RESULTADOS DE VENDAS
        for Id in data.dynamicSellResults:
            emp = data.dynamicSellResults[Id]
            print(f'\n{Id} : {emp.getName()}')
            for result in data.dynamicSellResults[Id]:
                print(f'{result}')
        print()
