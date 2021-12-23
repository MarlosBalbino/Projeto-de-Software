import random
from dataBase import data
from employee.Imports import *
from management.undoRedo import UndoRedo


class FillEmployee:
    """preenche os dados do novo empregado"""

    def __init__(self, init=1):
        if init:
            self.name = input('Digite o nome de um empregado\n')
            self.address = input('\nDigite o endereço\n')
            info = self.__classInfo()
            self.class_ = info[0]
            self.type_ = info[1]

            self.Id = random.randrange(100000)
            while self.Id in data.dynamicDataBase.keys():  # recebe uma lista com todas as Ids existentes
                self.Id = random.randrange(100000)

    def setName(self):
        self.name = input('Digite o nome do empregado:\n')

    def setAddress(self):
        self.address = input('\nDigite o endereço:\n')

    def setInfo(self):
        info = self.__classInfo()
        self.class_ = info[0]
        self.type_ = info[1]

    def setSyndicate(self, contained=0):
        self.syndicate = self.__syndicateInfo(contained)

    def setPayment(self):
        self.payment = self.__paymentInfo()

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

    def getSyndicate(self):
        return self.syndicate

    def getPayment(self):
        return self.payment

    @staticmethod
    def __classInfo():
        """retorna uma lista com a classe e uma string indicando o tipo do empregado"""

        while True:
            opt = eval(input('\nDigite o tipo de empregado:\n'
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
                print('\nTipo de empregado inválido, digite novamente:')

    @staticmethod
    def __paymentInfo():
        """retorna a forma de pagamento em string"""
        payment_1 = 'Depósito bancário'
        payment_2 = 'Cheque pelos correios'
        payment_3 = 'Cheque em mãos'
        while True:
            opt = eval(input('\nDigite a forma de pagamento desejada:\n'
                             f'1 - {payment_1}\n'
                             f'2 - {payment_2}\n'
                             f'3 - {payment_3}\n'))

            if opt == 1:
                return payment_1
            elif opt == 2:
                return payment_2
            elif opt == 3:
                return payment_3
            else:
                print('\nDigite uma opção válida:')

    @staticmethod
    def __syndicateInfo(contained):
        def Not(opt):
            if opt == 1:
                return 0
            else:
                return 1

        if contained == 0:
            while True:
                opt = eval(input('\nAderir ao sindicato?\n'
                                 'Digite: 1 - Sim.'
                                 '        0 - Não.\n'))
                if opt == 1 or opt == 0:
                    return opt
                else:
                    print('\nDigite 0 ou 1')
        else:
            while True:
                opt = Not(eval(input('\nSair do sindicato?\n'
                                     'Digite: 1 - Sim.'
                                     '        0 - Não.\n')))
                if opt == 1 or opt == 0:
                    return opt
                else:
                    print('\nDigite 0 ou 1')


class FillHourly:
    def __init__(self, init=1):
        if init == 1:
            self.hourlysalary = eval(input('\nDigite o salário horário:\n'))

    def getHourlySalary(self):
        return self.hourlysalary

    def setWorkingHours(self):
        self.hours = eval(input('\nDigite as horas trabalhadas:\n'))

    def setExtraWorkingHours(self):
        self.extra_hours = eval(input('\nDigite as horas extras:\n'))

    def getWorkingHours(self):
        return self.hours

    def getExtraWorkingHours(self):
        return self.extra_hours


class FillSalaried:
    def __init__(self):
        self.salary = eval(input('\nDigite o salário mensal:\n'))

    def getSalary(self):
        return self.salary


class FillCommissioned(FillSalaried):
    def __init__(self):
        super().__init__()
        self.commission = eval(input('\nDigite a taxa de comissão:\n'))

    def getCommission(self):
        return self.commission


class FillSyndicate:
    def __init__(self, Id=0, init=1):
        if init == 1:
            self.unionFee = eval(input('\nDigite o valor da taxa sindical:\n'))
            self.serviceFee = 0
            self.Id = Id

            self.syndicateId = random.randrange(10000)
            while self.syndicateId in data.dynamicSyndicateDB.keys():  # recebe uma lista com todas as Ids existentes
                self.syndicateId = random.randrange(10000)

    def setServiceFee(self):
        self.serviceFee = eval(input('\nDigite a taxa de serviço:\n'))

    def setSyndicateId(self):
        self.syndicateId = eval(input('\nDigite a nova Id do sindicato:\n'))

    def setUnionFee(self):
        self.unionFee = eval(input('\nDigite a nova taxa sindical:\n'))

    def getUnionFee(self):
        return self.unionFee

    def getServiceFee(self):
        return self.serviceFee

    def getSyndicateId(self):
        return self.syndicateId

    def signIn(self, Id):
        unionFee = self.getUnionFee()
        serviceFee = self.getServiceFee()
        syndicateId = self.getSyndicateId()
        employee = Syndicate(unionFee, serviceFee, Id, syndicateId)

        data.dynamicSyndicateDB[syndicateId] = employee
        data.DataBaseManager.writeSyndicateDB()


class SpecialAttrib:
    @staticmethod
    def attrib(class_, employee):
        Id = employee.getId()
        if class_ == Hourly:
            fill = FillHourly()
            employee.setHourlySalary(fill.getHourlySalary())

            data.scheduleDB[Id] = data.scheduleList[1]
            data.DataBaseManager.writeScheduleDB()

        elif class_ == Salaried:
            fill = FillSalaried()
            employee.setSalary(fill.getSalary())

            data.scheduleDB[Id] = data.scheduleList[2]
            data.DataBaseManager.writeScheduleDB()

        else:
            fill = FillCommissioned()
            employee.setSalary(fill.getSalary())
            employee.setCommission(fill.getCommission())

            data.scheduleDB[Id] = data.scheduleList[3]
            data.DataBaseManager.writeScheduleDB()

        return employee
