################################################################################
## Projeto de Software - 2021.1
##
## FOLHA DE PAGAMENTO
##
################################################################################

from management import *
import data


def caseHandle(case):
    switch = {1: addEmployee,
              2: removeEmployee,
              3: setTimeCard,
              4: setSellResult,
              5: setServiceRate,
              6: changeEmployeeData,
              7: payRoll,
              8: undoRedo,
              9: paymentSchedule,
              10: newPaymentSchedules,
              11: printDataBase,
              12: printTimeCards,
              13: printSellResults}
    switch[case]()


def main():
    data.DynamicDataBase().read_db()
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
            caseHandle(case)
        except SyntaxError:
            print('Digite um número válido1')
        # except NameError:
        #     print('Digite um número válido2')
        except KeyError:
            print('Digite um número válido3')


# manutenção e teste
if __name__ == '__main__':
    main()

