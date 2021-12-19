from dataBase import data
import time
from employee.commissioned import Commissioned
from management.verifyEmployee import verifyEmployee


class SellResult:

    @staticmethod
    def setSellResult():
        """lança um cartão de ponto"""
        Id = verifyEmployee()
        if Id != -1:
            employee = data.dynamicDataBase[Id]
            if type(employee) != Commissioned:
                print('Esse empregado não é comissionado')
                return None

            try:
                sell = eval(input('Digite o valor da venda:\n'))
                sellResult = time.strftime('%d/%m/%y %H:%M:%S') + '  R$' + str(sell)
                data.dynamicSellResults[Id] = sellResult

                percentage = employee.percentage()
                commission = (percentage/100) * sell
                employee.setCommission(commission)
                data.dynamicDataBase[Id] = employee

            except:
                print('Não foi possível lançar resultado de venda!!')
