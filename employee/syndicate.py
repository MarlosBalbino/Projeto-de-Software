class Syndicate:
    """representa o empregado que pertence ao sindicato"""

    def __init__(self, unionfee=0, servicefee=0, Id=0, syndicateid=0):
        self.unionFee = unionfee
        self.serviceFee = servicefee
        self.Id = Id
        self.syndicateId = syndicateid

    def getUnionFee(self):
        """retorna a taxa sindical"""
        return self.unionFee

    def getServiceFee(self):
        """retorna a taxa de serviço"""
        return self.serviceFee

    def getId(self):
        """retorna a Id da folha de pagamento"""
        return self.Id

    def getSyndicateId(self):
        """retorna a Id do sindicato"""
        return self.syndicateId

    def getData(self):
        """retorna todos os dados pertinentes ao sindicato"""
        return f"Taxa sindical: {self.unionFee}\n" \
               f"Taxa de serviço: {self.serviceFee}\n" \
               f"Id - Folha de pagamento: {self.Id}\n" \
               f"Id - Sindicato: {self.syndicateId}"

    def __repr__(self):
        """retorna a representação de string canônica"""
        return f"Syndicate({self.unionFee}, {self.serviceFee}, {self.Id}, {self.syndicateId})"

    def __str__(self):
        """retorna a representação de string canônica"""
        return self.__repr__()

