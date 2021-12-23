################################################################################
## Projeto de Software - 2021.1
##
## FOLHA DE PAGAMENTO
##
################################################################################
from dataBase import data
from management.extraModules.exit import ZeroError
from management.caseHandle import CaseHandle
from management.undoRedo import UndoRedo
from os import system


class Main:

    @staticmethod
    def menu():
        data.DataBaseManager.readDataBase()
        UndoRedo.saveState()
        while True:
            try:
                system('cls')
                print(f"{19*'='} Menu {20*'='}\n")
                case = eval(input('1 - Adicionar empregado\n'
                                  '2 - Remover empregado\n'
                                  '3 - Lançar cartão de ponto\n'
                                  '4 - Lançar um resultado de venda\n'
                                  '5 - Lançar taxa de serviço\n'
                                  '6 - Alterar os dados do empregado\n'
                                  '7 - Rodar folha de pagamento\n'
                                  '8 - Escolher agenda de pagamento\n'
                                  '9 - Criar uma nova agenda de pagamento\n'
                                  '10 - Listar todos os empregados\n'
                                  '11 - Listar cartões de ponto\n'
                                  '12 - Listar resultados de vendas\n'
                                  '13 - Listar empregados associados ao sindicato\n'
                                  '14 - Listar agenda de pagamento dos empregados\n'
                                  '15 - Listar agendas\n'
                                  '16 - Listar contracheques\n'
                                  '17 - Desfazer\n'
                                  '18 - Refazer\n'
                                  '0 - sair\n'))
                system('cls')
                done = CaseHandle.switch(case)
                if done is not None:
                    UndoRedo.saveState()
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

