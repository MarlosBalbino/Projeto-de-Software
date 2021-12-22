from employee.employee_ import __Employee


class Salaried(__Employee):
    """representa empregado salariado"""

    # estende o método __init__ da super classe
    def __init__(self, name='None', address='None', type='None', id=0, syndicate=0, payment='None', salary=0):
        super().__init__(name, address, type, id, syndicate, payment)
        self.salary = salary

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        """retorna salário do empregado"""
        return self.salary

    def getData(self):
        return f"{super().getData()}" + \
               f"Salário: R$ {self.salary:.2f}"

    def _repr(self):
        return f"{super()._repr()}, " + \
               f"{self.salary}"

    def __repr__(self):
        return f"Salaried({self._repr()})"

    def __str__(self):
        return f"Salaried({self._repr()})"
