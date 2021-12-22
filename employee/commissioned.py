from employee.salaried import Salaried


class Commissioned(Salaried):
    """representa empregado comissionado"""

    # estende o método __init__ da super classe
    def __init__(self, name='None', address='None', type='None', id=0, syndicate=0, payment='None', salary=0,
                 periodCommission=0, commission=0):
        super().__init__(name, address, type, id, syndicate, payment, salary)
        self.periodCommission = periodCommission
        self.commission = commission

    def setCommission(self, commission):
        self.commission = commission

    def setPeriodCommission(self, periodCommission):
        self.periodCommission += periodCommission

    def getPeriodCommission(self):
        """retorna comissão"""
        return self.periodCommission

    def getCommission(self):
        """retorna o percentual de comissão"""
        return self.commission

    def getData(self):
        return f"{super().getData()}\n" + \
               f"Comissão do período: R$ {self.periodCommission:.2f}\n" + \
               f"Percentual de comissão: {self.commission} %"

    def _repr(self):
        return f"{super()._repr()}, " + \
               f"{self.periodCommission}, " + \
               f"{self.commission}"

    def __repr__(self):
        return f"Commissioned({self._repr()})"

    def __str__(self):
        return f"Commissioned({self._repr()})"
