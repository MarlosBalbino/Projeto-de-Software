from management.fill_employee_data.fillData import *
from management.fill_employee_data.updateOptions import Change
from management.fill_employee_data.removeOptions import Remove
from management.extraModules.verifyEmployee import verifyEmployee
from management.extraModules.exit import ZeroError
from dataBase import data
from os import system


class EmployeeCRUD:

    @staticmethod
    def add():
        """adiciona um novo empregado ao banco de dados"""
        print(f"{13 * '='} Novo empregado {14 * '='}\n")

        fill = FillEmployee()
        name = fill.getName()
        address = fill.getAddress()
        type_ = fill.getType()
        class_ = fill.getClass()
        Id = fill.getId()
        employee = class_(name, address, type_, Id)
        employee = SpecialAttrib.attrib(class_, employee)

        fill.setPayment()
        payment = fill.getPayment()
        employee.setPayment(payment)

        fill.setSyndicate(contained=0)
        syndicate = fill.getSyndicate()
        employee.setSyndicate(syndicate)

        data.dynamicDataBase[Id] = employee  # escreve dados do novo empregado no banco de dados dinâmico.
        data.DataBaseManager.writeDataBase()  # escreve os dados no banco de dados.

        if syndicate == 1:
            fill = FillSyndicate(Id)
            fill.signIn(Id)

        print('\nEmpregado cadastrado com sucesso!!\n')
        system('pause')
        return 1

    @staticmethod
    def remove():
        """remove um empregado do banco de dados"""

        print(f"{13 * '='} Remover empregado {13 * '='}\n")
        Id = verifyEmployee()
        if Id != -1:
            opt = eval(input('Tem certeza que deseja remover esse empregado?\n'
                             '1 - Sim\n'
                             '0 - Não\n'))
            if opt == 1:
                Remove.employeeData(Id)
                Remove.timeCardsData(Id)
                Remove.sellResultsData(Id)
                Remove.syndicateData(Id)
                Remove.scheduleData(Id)

                print('Empregado removido com sucesso.\n')
                system('pause')
                return 1
            else:
                print('Operação abortada!\n')
        system('pause')

    @staticmethod
    def update():
        """altera os dados de um empregado"""

        print(f"{12 * '='} Atualizar empregado {12 * '='}\n")
        Id = verifyEmployee()
        if Id != -1:
            try:
                employee = data.dynamicDataBase[Id]

                # INTERAÇÃO COM O USUÁRIO
                while True:
                    try:
                        case = eval(input('\nDigite a opção que deseja alterar:\n'
                                          '1 - nome:\n'
                                          '2 - endereço:\n'
                                          '3 - tipo de empregado:\n'
                                          '4 - forma de pagamento:\n'
                                          '5 - sair ou entrar no sindicato:\n'
                                          '6 - identificação no sindicato:\n'
                                          '7 - taxa sindical:\n'
                                          '0 - sair:\n'))

                        changer = Change(employee)
                        changer.switch(case)
                        employee = changer.getEmployee()
                        system('cls')

                    except SyntaxError:
                        print('Digite um número válido.\nErro #3')
                    except NameError:
                        print('Digite um número válido.\nErro #4')
                    except KeyError:
                        print('Digite uma das opções acima #1.')
                    except ZeroError:
                        break

                # ATUALIZA OS DADOS DOS EMPREGADOS
                data.dynamicDataBase[Id] = employee
                data.DataBaseManager.writeDataBase()
                print('\nDados alterados com sucesso!!\n')
                system('pause')
                return 1

            except:
                print('\nNão foi possível alterar os dados do empregado\n')
        system('pause')

    @staticmethod
    def eraseDataBase():
        print(f"{10 * '='} Deletar banco de dados!!! {10 * '='}\n")

        opt = eval(input('Tem certeza que deseja apagar o banco de dados?\n'
                         '1 - Sim. 0 - Não.\n'))
        if opt == 1:
            opt = eval(input('Todos os dados serão apagados permanentemente. Deseja continuar mesmo assim?\n'
                             '1 - Sim. 0 - Não.\n'))
            if opt == 1:
                data.DataBaseManager.eraseDataBase()
                print('Os dados foram deletados!!!\n')
                system('pause')
                return 1
            else:
                print('Operação abortada.\n')
        else:
            print('Operação abortada.\n')
        system('pause')
