from management.fill_data.employeeFillData import *
from management.verifyEmployee import verifyEmployee


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
        employee = EmployeeCRUD.specialAttrib(class_, employee)

        data.dynamicDataBase[Id] = employee  # escreve dados do novo empregado no banco de dados dinâmico.
        data.DataBaseManager.writeDataBase()  # escreve os dados no banco de dados.

        print('Empregado cadastrado com sucesso!!')

    @staticmethod
    def remove():
        """remove um empregado do banco de dados"""

        Id = verifyEmployee()
        if Id != -1:
            opt = eval(input('Tem certeza que deseja remover esse empregado?\n'
                             '1 - Sim\n'
                             '0 - Não\n'))
            if opt == 1:
                try:
                    data.dynamicDataBase.pop(Id)
                    data.DataBaseManager.writeDataBase()
                    print('Empregado removido com sucesso')
                except:
                    print(f"Erro: não foi possível remover o empregado")

                # implementar remoção de cartão de ponto e resultado de vendas

            else:
                print('Operação abortada!')

    @staticmethod
    def update():
        """altera os dados de um empregado"""

        Id = verifyEmployee()
        if Id != -1:
            try:
                employee = data.dynamicDataBase[Id]
                # RECUPERA DADOS DO EMPREGADO
                name = employee.getName()
                address = employee.getAddress()

                # INTERAÇÃO COM O USUÁRIO
                while True:
                    opt = eval(input('Digite a opção que deseja alterar:\n'
                                     '1 - nome:\n'
                                     '2 - endereço:\n'
                                     '3 - tipo de empregado:\n'
                                     '0 - sair:\n'))

                    fill = FillEmployee(init=0)
                    if opt == 1:
                        fill.setName()
                        name = fill.getName()
                        employee.setName(name)
                    elif opt == 2:
                        fill.setAddress()
                        address = fill.getAddress()
                        employee.setAddress(address)
                    elif opt == 3:
                        fill.setInfo()
                        class_ = fill.getClass()
                        type_ = fill.getType()
                        employee = class_(name, address, type_, Id)
                        employee = EmployeeCRUD.specialAttrib(class_, employee)
                    else:
                        break

                # ATUALIZA OS DADOS DOS EMPREGADOS
                data.dynamicDataBase[Id] = employee
                data.DataBaseManager.writeDataBase()
                print('Dados alterados com sucesso!!')

            except:
                print('Não foi possível alterar os dados do empregado')

    @staticmethod
    def specialAttrib(class_, employee):
        if class_ == Hourly:
            fill = FillHourly()
            employee.hourlysalary = fill.getHourlySalary()

        elif class_ == Salaried:
            fill = FillSalaried()
            employee.salary = fill.getSalary()
        else:
            fill = FillCommissioned()
            employee.salary = fill.getSalary()
            employee.percentage = fill.getPercentage()

        return employee
