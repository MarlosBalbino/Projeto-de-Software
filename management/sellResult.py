from dataBase import data
import time
from employee.commissioned import Commissioned
from management.extraModules.verifyEmployee import verifyEmployee


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

                print('Resultado de venda adicionado com sucesso!!')

            except:
                print('Não foi possível lançar resultado de venda!!')
