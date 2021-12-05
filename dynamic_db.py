from dataBase import DataBase
from employee import *

dynamicDataBase = {}


class Initialize:

    def started(self):
        self.db = DataBase()
        self.db.connect()
        allEmployees = self.db.selectAllEmployees()
        for value in allEmployees:
            name = value[0]
            address = value[1]
            emptype = value[2]
            Id = value[3]
            Type = value[-1]

            emp = eval(Type)(name, address, emptype, Id)

            dynamicDataBase[Id] = emp

    def finished(self):
        """função é chamada quando o sistema é encerrado"""
        updatedEmployee = []
        for key in dynamicDataBase.keys():
            emp = dynamicDataBase[key]
            updatedEmployee.append(emp.getName())
            updatedEmployee.append(emp.getAddress())
            updatedEmployee.append(emp.getEmployeeType())
            updatedEmployee.append(emp.getId())
            if type(emp) == Hourly:
                updatedEmployee.append('Hourly')
            elif type(emp) == Salaried:
                updatedEmployee.append('Salaried')
            else:
                updatedEmployee.append('Commissioned')

            self.db.updateEmployee(updatedEmployee)

        self.db.close_connection()


