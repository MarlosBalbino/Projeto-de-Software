from employee.syndicate import Syndicate
from dataBase import data


class FindSyndicate:
    def __init__(self):
        self.__found = 0
        self.__syndicateId = -1

    def search(self, Id):
        syndicateDB = data.dynamicSyndicateDB
        for key in syndicateDB.keys():
            value = syndicateDB[key]
            if value.getId() == Id:
                self.__found = 1
                self.__syndicateId = key
                break

    def found(self):
        """retorna 1 se trabalhador foi encontrado no sindicato.
        retorna 0 caso contrário"""
        return self.__found

    def getSyndicateId(self):
        """retorna Id do sindicato"""
        return self.__syndicateId
