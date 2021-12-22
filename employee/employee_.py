class __Employee:  # Private
    """representa o topo da hierarquia de empregado"""

    def __init__(self, name='None', address='None', type='None', id=0, syndicate=0, payment='None'):
        self.name = name
        self.address = address
        self.type = type
        self.id = id
        self.syndicate = syndicate
        self.payment = payment

    def _repr(self):
        return f"'{self.name}', "\
               f"'{self.address}', "\
               f"'{self.type}', "\
               f"{self.id}, " \
               f"{self.syndicate}, " \
               f"'{self.payment}'"

    def __repr__(self):
        return f"Employee({self._repr()})"

    def __str__(self):
        """retorna representação de string canônica"""
        return f"Employee('{self._repr()})'"

    def setName(self, name):
        """define o nome do empregado"""
        self.name = name

    def setAddress(self, address):
        """define o endereço do empregado"""
        self.address = address

    def setType(self, type):
        """define o tipo do empregado"""
        self.type = type

    def setPayment(self, payment):
        """determina a forma de pagamento"""
        self.payment = payment

    def getName(self):
        """retorna o nome do empregado"""
        return self.name

    def getAddress(self):
        """retorna o nome do empregado"""
        return self.address

    def getEmployeeType(self):
        """retorna o tipo do empregado"""
        return self.type

    def getId(self):
        """retorna o id do empregado"""
        return self.id

    def setSyndicate(self, syndicate):
        self.syndicate = syndicate

    def getSyndicate(self):
        return self.syndicate

    def getPayment(self):
        return self.payment

    def __belongsSyndicate(self):
        if self.syndicate == 1:
            return 'Sim'
        else:
            return 'Não'

    def getData(self):
        return f'Nome: {self.name}\n' \
               f'Endereço: {self.address}\n' \
               f'Tipo de empregado: {self.type}\n' \
               f'Id: {self.id}\n' \
               f'Pertence ao sindicato: {self.__belongsSyndicate()}\n' \
               f'Forma de pagamento: {self.payment}\n'
