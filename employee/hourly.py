from employee.employee_ import __Employee


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

    def setHourlySalary(self, hourlysalary):
        """determina o salário horário"""
        self.hourlysalary = hourlysalary

    def getWorkingHours(self):
        """retorna as horas de trabalho"""
        return self.hours

    def extraWorkingHours(self):
        """retorna as horas extras de trabalho"""
        pass

    def getHourlySalary(self):
        """retorna salário horário"""
        return self.hourlysalary

    def getData(self):
        return f"{super().getData()}" + \
               f"Salário horário: R$ {self.hourlysalary:.2f}\n" \
               f"Horas Trabalhadas: {self.hours} horas"

    def _repr(self):
        return f"{super()._repr()}, " + \
               f"{self.hourlysalary}, " \
               f"{self.hours}"

    def __repr__(self):
        return f"Hourly({self._repr()})"

    def __str__(self):
        return f"Hourly({self._repr()})"
