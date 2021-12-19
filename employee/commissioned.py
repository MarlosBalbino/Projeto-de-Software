from employee.salaried import Salaried


class Commissioned(Salaried):
    """representa empregado comissionado"""

    # estende o método __init__ da super classe
    def __init__(self, name='None', address='None', type='None', id=0, salary=0, commission=0, percentage=0):
        super().__init__(name, address, type, id, salary)
        self.commission = commission
        self.percentage = percentage

    def setCommission(self, commission):
        self.commission += commission

    def getCommission(self):
        """retorna comissão"""
        return self.commission

    def getPercentage(self):
        """retorna o percentual de comissão"""
        return self.percentage

    def getData(self):
        return f"{super().getData()}\n" + \
               f"Comissão: R$ {self.commission:.2f}\n" + \
               f"Percentual de comissão: {self.percentage} %"

    def _repr(self):
        return f"{super()._repr()}, " + \
               f"{self.commission}, " + \
               f"{self.percentage}"

    def __repr__(self):
        return f"Commissioned({self._repr()})"

    def __str__(self):
        return f"Commissioned({self._repr()})"
