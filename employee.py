class __Employee:  # Private
    """representa o topo da hierarquia de empregado"""

    def __init__(self, name='None', address='None', type='None', id=0):
        self.name = name
        self.address = address
        self.type = type
        self.id = id

    def __repr__(self):
        return f"('{self.name}', "\
               f"'{self.address}', "\
               f"'{self.type}', "\
               f"{self.id}, "

    def __str__(self):
        """retorna representação de string canônica"""

        return f"('{self.name}', "\
               f"'{self.address}', "\
               f"'{self.type}', "\
               f"{self.id}, "

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

    def getData(self):
        return f'Nome: {self.name}\n' \
               f'Endereço: {self.address}\n' \
               f'Tipo de empregado: {self.type}\n' \
               f'Id: {self.id}\n'


class Hourly(__Employee):
    """representa empregado horista"""

    # estende o método __init__ da super classe
    def __init__(self, name='None', address='None', type='None', id=0, hourlysalary=0, hours=0):
        super().__init__(name, address, type, id)
        self.hourlysalary = hourlysalary
        self.hours = hours
        self.extra_hours = 0

    def setWorkingHours(self, hours):
        """determina horas trabalhadas"""

        self.hours += hours

    def getWorkingHours(self):
        """retorna as horas de trabalho"""
        return self.hours

    def __extraWorkingHours(self):
        """retorna as horas extras de trabalho"""
        pass

    def getHourlySalary(self):
        """retorna salário horário"""
        return self.hourlysalary

    def getData(self):
        return f"{super().getData()}" + \
               f"Salário horário: R$ {self.hourlysalary:.2f}\n" \
               f"Horas Trabalhadas: {self.hours} horas"

    def __repr__(self):
        return f"Hourly{super().__str__()}" + \
               f"{self.hourlysalary}, " \
               f"{self.hours})"

    def __str__(self):
        return f"Hourly{super().__str__()}" + \
               f"{self.hourlysalary}, " \
               f"{self.hours})"


class Salaried(__Employee):
    """representa empregado salariado"""

    # estende o método __init__ da super classe
    def __init__(self, name='None', address='None', type='None', id=0, salary=0):
        super().__init__(name, address, type, id)
        self.salary = salary

    def getSalary(self):
        """retorna salário do empregado"""
        return self.salary

    def getData(self):
        return f"{super().getData()}" + \
               f"Salário: R$ {self.salary:.2f}"

    def __repr__(self):
        return f"Salaried{super().__str__()}" + \
               f"{self.salary})"

    def __str__(self):
        return f"Salaried{super().__str__()}" + \
               f"{self.salary})"


class Commissioned(__Employee):
    """representa empregado comissionado"""

    # estende o método __init__ da super classe
    def __init__(self, name='None', address='None', type='None', id=0, commission=0):
        super().__init__(name, address, type, id)
        self.commission = commission

    def getCommission(self):
        """retorna comissão"""
        return self.commission

    def getData(self):
        return f"{super().getData()}" + \
               f"Comissão: {self.commission}%"

    def __repr__(self):
        return f"Commissioned{super().__str__()}" + \
               f"{self.commission})"

    def __str__(self):
        return f"Commissioned{super().__str__()}" + \
               f"{self.commission})"