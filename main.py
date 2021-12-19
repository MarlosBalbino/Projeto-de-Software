################################################################################
## Projeto de Software - 2021.1
##
## FOLHA DE PAGAMENTO
##
################################################################################

from dataBase import data
from management.Imports import *


class Main:

    @staticmethod
    def caseHandle(case):
        switch = {1: EmployeeCRUD.add,
                  2: EmployeeCRUD.remove,
                  3: TimeCard.setTimeCard,
                  4: SellResult.setSellResult,
                  # 5: setServiceRate,
                  6: EmployeeCRUD.update,
                  # 7: payRoll,
                  # 8: undoRedo,
                  # 9: paymentSchedule,
                  # 10: newPaymentSchedules,
                  11: PrintData.printDataBase,
                  12: PrintData.printTimeCards,
                  13: PrintData.printSellResults}
        switch[case]()

    @staticmethod
    def run():
        data.DataBaseManager.readDataBase()
        while True:
            try:
                print(36 * '=')
                case = eval(input('1 - Adicionar empregado\n'
                                  '2 - Remover empregado\n'
                                  '3 - Lançar cartão de ponto\n'
                                  '4 - Lançar um resultado de venda\n'
                                  '5 - Lançar taxa de serviço\n'
                                  '6 - Alterar os dados do empregado\n'
                                  '11 - Listar todos os empregados\n'
                                  '12 - Listar cartões de ponto\n'
                                  '13 - Listar resultados de vendas\n'
                                  '0 - sair\n'))
                print(36 * '=')
                if not case:
                    break
                Main.caseHandle(case)
            except SyntaxError:
                print('Digite um número válido.\nErro #1')
            except NameError:
                print('Digite um número válido.\nErro #2')
            except KeyError:
                print('Digite uma das opções acima.')


if __name__ == '__main__':
    Main.run()

