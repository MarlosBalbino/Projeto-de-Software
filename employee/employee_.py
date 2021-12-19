class __Employee:  # Private
    """representa o topo da hierarquia de empregado"""

    def __init__(self, name='None', address='None', type='None', id=0):
        self.name = name
        self.address = address
        self.type = type
        self.id = id
        self.syndicate = 0

    def _repr(self):
        return f"'{self.name}', "\
               f"'{self.address}', "\
               f"'{self.type}', "\
               f"{self.id}"

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

    def setSyndicate(self):
        self.syndicate = 1

    def getSyndicate(self):
        return self.syndicate

    def getData(self):
        return f'Nome: {self.name}\n' \
               f'Endereço: {self.address}\n' \
               f'Tipo de empregado: {self.type}\n' \
               f'Id: {self.id}\n' \
               f'Pertence ao sindicato: {self.syndicate}'
