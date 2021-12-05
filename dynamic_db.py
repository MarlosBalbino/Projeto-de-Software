from dataBase import DataBase
from employee import *

dynamicDataBase = {}


class Initialize:

    def started(self):
        """obtém os dados do banco de dados e armazena em um dicionário"""

        # CONECTA AO BANCO DE DADOS
        self.db = DataBase()
        self.db.connect()

        # OBTÉM UMA LISTA COM TODOS OS DADOS DE TODOS OS EMPREGADOS
        allEmployees = self.db.selectAllEmployees()

        # PERCORRE CADA EMPREGADO NA LISTA E OBTÉM SEUS RESPECTIVOS DADOS
        for value in allEmployees:
            name = value[0]
            address = value[1]
            emptype = value[2]
            Id = value[3]
            Type = value[-1]

            emp = eval(Type)(name, address, emptype, Id)

            # INSERE O OBJETO EMPREGADO NO DICIONÁRIO
            dynamicDataBase[Id] = emp

    def finished(self):
        """atualiza o banco de dados quando o sistema é encerrado"""
        updatedEmployee = []
        for key in dynamicDataBase.keys():
            # OBTÉM O OBJETO EMPREGADO DO DICIONÁRIO
            emp = dynamicDataBase[key]

            # OBTÉM OS DADOS DO EMPREGADO
            updatedEmployee.append(emp.getName())
            updatedEmployee.append(emp.getAddress())
            updatedEmployee.append(emp.getEmployeeType())
            updatedEmployee.append(emp.getId())

            # DETERMINA O TIPO DO EMPREGADO
            if type(emp) == Hourly:
                updatedEmployee.append('Hourly')
            elif type(emp) == Salaried:
                updatedEmployee.append('Salaried')
            else:
                updatedEmployee.append('Commissioned')

            # JOGA OS DADOS ATUALIZADOS DO EMPREGADO NO BANCO DE DADOS
            self.db.updateEmployee(updatedEmployee)

        self.db.close_connection()


