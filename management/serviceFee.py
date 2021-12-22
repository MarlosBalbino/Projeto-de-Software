from management.extraModules.verifyEmployee import verifyEmployee
from management.extraModules.findInSyndicate import FindSyndicate
from employee.Imports import *
from dataBase import data


def nothing():
    Syndicate()


class Service:

    @staticmethod
    def setServiceFee():
        Id = verifyEmployee()
        if Id != -1:
            find = FindSyndicate()
            find.search(Id)

            if find.found() == 1:
                syndicateId = find.getSyndicateId()
                syndicateEmp = data.dynamicSyndicateDB[syndicateId]
                while True:
                    try:
                        serviceFee = eval(input('Digite a taxa de serviço:\n'))
                        syndicateEmp.setServiceFee(serviceFee)
                        break
                    except:
                        print('Digite um número inteiro ou ponto flutuante')

                data.DataBaseManager.writeSyndicateDB()
            else:
                print('Empregado não possui vinculo com o sindicato')
