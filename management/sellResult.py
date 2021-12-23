from dataBase import data
import time
from employee.commissioned import Commissioned
from management.extraModules.verifyEmployee import verifyEmployee
from os import system


class SellResult:

    @staticmethod
    def setSellResult():
        """lança um cartão de ponto"""
        print(f"{13 * '='} Resultado de venda {14 * '='}")

        Id = verifyEmployee()
        if Id != -1:
            employee = data.dynamicDataBase[Id]
            if type(employee) != Commissioned:
                print('\nEsse empregado não é comissionado\n')
                system('pause')
                return None

            try:
                sell = eval(input('\nDigite o valor da venda:\n'))
                new_sellresult = time.strftime('%d/%m/%y %H:%M:%S') + '  R$ ' + str(sell)
                sellresults = []
                if Id in data.dynamicSellResults:
                    sellresults = data.dynamicSellResults[Id]

                sellresults.append(new_sellresult)
                data.dynamicSellResults[Id] = sellresults
                data.DataBaseManager.writeSellResults()

                commission = employee.getCommission()
                periodCommission = (commission/100) * sell
                employee.setPeriodCommission(periodCommission)
                data.dynamicDataBase[Id] = employee
                data.DataBaseManager.writeDataBase()

                print('Resultado de venda adicionado com sucesso!!\n')
                system('pause')
                return 1

            except:
                print('Não foi possível lançar resultado de venda!!\n')
        system('pause')
