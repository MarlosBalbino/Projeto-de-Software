################################################################################
## Projeto de Software - 2021.1
##
## FOLHA DE PAGAMENTO
##
################################################################################
from dataBase import data
from management.extraModules.exit import ZeroError
from management.caseHandle import CaseHandle
import os


class Main:

    @staticmethod
    def menu():
        data.DataBaseManager.readDataBase()
        while True:
            try:
                print(45*'=')
                case = eval(input('1 - Adicionar empregado\n'
                                  '2 - Remover empregado\n'
                                  '3 - Lançar cartão de ponto\n'
                                  '4 - Lançar um resultado de venda\n'
                                  '5 - Lançar taxa de serviço\n'
                                  '6 - Alterar os dados do empregado\n'
                                  '9 - Escolher agenda de pagamento\n'
                                  '10 - Criar uma nova agenda de pagamento\n'
                                  '11 - Listar todos os empregados\n'
                                  '12 - Listar cartões de ponto\n'
                                  '13 - Listar resultados de vendas\n'
                                  '14 - Listar empregados associados ao sindicato\n'
                                  '15 - Listar agenda de pagamento dos empregados\n'
                                  '16 - Listar agendas\n'
                                  '0 - sair\n'))
                print(45*'=')
                CaseHandle.switch(case)
            except SyntaxError:
                print('Digite um número válido.\nErro #1')
            except NameError:
                print('Digite um número válido.\nErro #2')
            except KeyError:
                print('Digite uma das opções acima.')
            except ZeroError:
                break


if __name__ == '__main__':
    Main.menu()

