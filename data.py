from dataBase import DataBase
from employee import *

dynamic_db = {}


class DynamicDataBase:

    def started(self):
        """obtém os dados do banco de dados e armazena em um dicionário"""

        # CONECTA AO BANCO DE DADOS
        self.db = DataBase()
        self.db.connect()

        # PERCORRE CADA EMPREGADO NO BANCO DE DADOS E OBTÉM SEUS RESPECTIVOS DADOS
        for table in ['Hourly', 'Salaried', 'Commissioned']:
            allEmployees = self.db.selectAllEmployees(table)
            if allEmployees == -1:
                continue

            for employee_data in allEmployees:
                name = employee_data[0]
                address = employee_data[1]
                emptype = employee_data[2]
                Id = employee_data[3]

                emp = eval(table)(name, address, emptype, Id)

                # INSERE O OBJETO EMPREGADO NO DICIONÁRIO
                dynamic_db[Id] = emp

    @staticmethod
    def read_db():
        try:
            file = open(f'dataBase\\employees.txt', 'r', encoding='utf8')
            global dynamic_db
            dynamic_db = eval(file.read())
            file.close()
        except FileNotFoundError:
            pass

    @staticmethod
    def write_db():

        file = open(f'dataBase\\employees.txt', 'w', encoding='utf8')
        file.write(f"{dynamic_db}")
        file.flush()
        file.close()



    def finished(self):
        """atualiza o banco de dados quando o sistema é encerrado"""

        for key in dynamic_db.keys():
            employeeData = []
            # OBTÉM O OBJETO EMPREGADO DO DICIONÁRIO
            emp = dynamic_db[key]

            # OBTÉM OS DADOS DO EMPREGADO
            employeeData.append(emp.getName())
            employeeData.append(emp.getAddress())
            employeeData.append(emp.getEmployeeType())
            employeeData.append(emp.getId())

            # JOGA OS DADOS ATUALIZADOS DO EMPREGADO NO BANCO DE DADOS
            if type(emp) == Hourly:
                self.db.updateEmployee(employeeData, 'Hourly')
                self.db.registerEmployee(employeeData, 'Hourly')
            elif type(emp) == Salaried:
                self.db.updateEmployee(employeeData, 'Salaried')
                self.db.registerEmployee(employeeData, 'Salaried')
            else:
                self.db.updateEmployee(employeeData, 'Commissioned')
                self.db.registerEmployee(employeeData, 'Commissioned')

        self.db.close_connection()


