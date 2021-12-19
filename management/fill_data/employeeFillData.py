import random
from dataBase import data
from employee.Imports import *


class FillEmployee:
    """preenche os dados do novo empregado"""

    def __init__(self, init=1):
        if init:
            self.name = input('Digite o nome de um empregado\n')
            self.address = input('Digite o endereço\n')
            info = FillEmployee.Info()
            self.class_ = info[0]
            self.type_ = info[1]

            self.Id = random.randrange(100000)
            while self.Id in data.dynamicDataBase.keys():  # recebe uma lista com todas as Ids existentes
                self.Id = random.randrange(100000)

    def setName(self):
        self.name = input('Digite o nome de um empregado\n')

    def setAddress(self):
        self.address = input('Digite o endereço\n')

    def setInfo(self):
        info = FillEmployee.Info()
        self.class_ = info[0]
        self.type_ = info[1]

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getClass(self):
        return self.class_

    def getType(self):
        return self.type_

    def getId(self):
        return self.Id

    @staticmethod
    def Info():
        """returna uma lista com a classe e uma string indicando o tipo do empregado"""

        while True:
            opt = eval(input('Digite o tipo de empregado:\n'
                             '1 - Horista\n'
                             '2 - Salariado\n'
                             '3 - Comissionado\n'))
            if opt == 1:
                return [Hourly, 'Horista']
            elif opt == 2:
                return [Salaried, 'Salariado']
            elif opt == 3:
                return [Commissioned, 'Comissionado']
            else:
                print('Tipo de empregado inválido, digite novamente:')


class FillHourly:
    def __init__(self):
        self.hourlysalary = eval(input('Digite o salário horário:\n'))

    def getHourlySalary(self):
        return self.hourlysalary


class FillSalaried:
    def __init__(self):
        self.salary = eval(input('Digite o salário mensal:\n'))

    def getSalary(self):
        return self.salary


class FillCommissioned(FillSalaried):

    def __init__(self):
        super().__init__()
        self.percentage = eval(input('Digite a taxa de comissão:\n'))

    def getPercentage(self):
        return self.percentage

