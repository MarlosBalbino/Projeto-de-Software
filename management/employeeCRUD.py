from management.fill_employee_data.fillData import *
from management.fill_employee_data.updateOptions import Change
from management.fill_employee_data.removeOptions import Remove
from management.extraModules.verifyEmployee import verifyEmployee
from management.extraModules.exit import ZeroError
from management.undoRedo import UndoRedo
from dataBase import data


class EmployeeCRUD:

    @staticmethod
    def add():
        """adiciona um novo empregado ao banco de dados"""

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

        print('Empregado cadastrado com sucesso!!')
        return 1

    @staticmethod
    def remove():
        """remove um empregado do banco de dados"""

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

                print('Empregado removido com sucesso.')
                return 1
            else:
                print('Operação abortada!')

    @staticmethod
    def update():
        """altera os dados de um empregado"""

        Id = verifyEmployee()
        if Id != -1:
            try:
                employee = data.dynamicDataBase[Id]

                # INTERAÇÃO COM O USUÁRIO
                while True:
                    try:
                        case = eval(input('Digite a opção que deseja alterar:\n'
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
                print('Dados alterados com sucesso!!')
                return 1

            except:
                print('Não foi possível alterar os dados do empregado')

    @staticmethod
    def eraseDataBase():
        opt = eval(input('Tem certeza que deseja apagar o banco de dados?\n'
                         '1 - Sim. 0 - Não.\n'))
        if opt == 1:
            opt = eval(input('Todos os dados serão apagados permanentemente. Deseja continuar mesmo assim?\n'
                             '1 - Sim. 0 - Não.\n'))
            if opt == 1:
                data.DataBaseManager.eraseDataBase()
                print('Os dados foram deletados!!!')
                return 1
            else:
                print('Operação abortada.')
        else:
            print('Operação abortada.')
