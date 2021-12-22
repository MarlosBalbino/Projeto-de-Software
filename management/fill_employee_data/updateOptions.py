from management.extraModules.exit import Exit
from management.fill_employee_data.fillData import *
from management.fill_employee_data.removeOptions import Remove
from management.extraModules.findInSyndicate import FindSyndicate


class Change:
    def __init__(self, employee):
        self.fill = FillEmployee(init=0)
        self.employee = employee

    def __name(self):
        self.fill.setName()
        name = self.fill.getName()
        self.employee.setName(name)

    def __address(self):
        self.fill.setAddress()
        address = self.fill.getAddress()
        self.employee.setAddress(address)

    def __employeeType(self):
        # SALVA DADOS ANTERIORES DO EMPREGADO
        name = self.employee.getName()
        address = self.employee.getAddress()
        Id = self.employee.getId()
        syndicate = self.employee.getSyndicate()
        payment = self.employee.getPayment()

        # PREENCHE NOVOS DADOS
        self.fill.setInfo()
        class_ = self.fill.getClass()
        type_ = self.fill.getType()
        self.employee = class_(name, address, type_, Id, syndicate, payment)
        self.employee = SpecialAttrib.attrib(class_, self.employee)

        # DELETA CARTÕES DE PONTO OU RESULTADOS DE VENDA, CASO EXISTAM
        Remove.timeCardsData(Id)
        Remove.sellResultsData(Id)

    def __payment(self):
        self.fill.setPayment()
        payment = self.fill.getPayment()
        self.employee.setPayment(payment)

    def __signInOutSyndicate(self):
        def __signIn(Id):
            fill = FillSyndicate(Id)
            fill.signIn(Id)

        def __signOut(Id):
            Remove.syndicateData(Id)

        Id = self.employee.getId()
        if self.employee.getSyndicate() == 1:
            self.fill.setSyndicate(1)
            syndicate = self.fill.getSyndicate()
            if syndicate == 0:
                __signOut(Id)

        else:
            self.fill.setSyndicate(0)
            syndicate = self.fill.getSyndicate()
            if syndicate == 1:
                __signIn(Id)

        self.employee.setSyndicate(syndicate)

    def __getSyndicateEmployee(self):
        Id = self.employee.getId()
        find = FindSyndicate()
        find.search(Id)
        syndicateId = find.getSyndicateId()
        return data.dynamicSyndicateDB.pop(syndicateId)

    def __syndicateId(self):
        if self.employee.getSyndicate() == 1:
            syndicateEmp = self.__getSyndicateEmployee()

            fill = FillSyndicate(init=0)
            fill.setSyndicateId()
            syndicateId = fill.getSyndicateId()
            syndicateEmp.setSyndicateId(syndicateId)
            data.dynamicSyndicateDB[syndicateId] = syndicateEmp
            data.DataBaseManager.writeSyndicateDB()
        else:
            print('Esse empregado não está vinculado ao sindicato.')

    def __unionFee(self):
        """altera a taxa sindical"""
        if self.employee.getSyndicate() == 1:
            syndicateEmp = self.__getSyndicateEmployee()

            fill = FillSyndicate(init=0)
            fill.setUnionFee()
            unionFee = fill.getUnionFee()
            syndicateEmp.setUnionFee(unionFee)
            data.dynamicSyndicateDB[syndicateEmp.getSyndicateId()] = syndicateEmp
            data.DataBaseManager.writeSyndicateDB()
        else:
            print('Esse empregado não está vinculado ao sindicato.')

    def switch(self, case):
        switch = {1: self.__name,
                  2: self.__address,
                  3: self.__employeeType,
                  4: self.__payment,
                  5: self.__signInOutSyndicate,
                  6: self.__syndicateId,
                  7: self.__unionFee,
                  0: Exit.end}
        switch[case]()

    def getEmployee(self):
        """retorna empregado com os dados alterados"""
        return self.employee
