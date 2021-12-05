import sqlite3


class DataBase:

    def __init__(self, name = 'dataBase\\banco.db'):
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            print('sla0')
            pass

    def createTableEmployee(self):
        cursor = self.connection.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS Employees(
                NOME TEXT,
                ENDEREÇO TEXT,
                TIPO_DE_EMPREGADO TEXT,
                ID INTEGER,
                
                PRIMARY KEY(ID));  
        """)

    def registerEmployee(self, data):
        fieldTable = ('NOME', 'ENDEREÇO', 'TIPO_DE_EMPREGADO', 'ID')

        qnt = '?, ?, ?, ?'
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Employees {fieldTable}
            VALUES({qnt})""", data)
            self.connection.commit()
            return "Registrado com sucesso"
        except NameError:
            return "Não foi possível registrar no banco de dados"

    def selectAllEmployees(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Employees ORDER BY ID")
            employees = cursor.fetchall()
            return employees
        except:
            print('sla1')
            pass

    def removeEmployee(self, Id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Employees WHERE ID = {Id}")
            self.connection.commit()

            return "Empregado removido com sucesso"
        except:
            return "Erro ao remover empregado"

    def updateEmployee(self, data):

        # ENDEREÇO = '{data[1]}',
        # TIPO_DE_EMPREGADO = '{data[2]}',
        # ID = {data[3]},
        try:
            cursor = self.connection.cursor()

            cursor.execute(f""" UPDATE Employees SET
                NOME = '{data[0]}',
                ENDEREÇO = '{data[1]}',
                TIPO_DE_EMPREGADO = '{data[2]}',
                ID = {data[3]}                
                
                WHERE ID = {713}""")

            self.connection.commit()
            return "Dados atualizados com sucesso"

        except NameError:
            return "Não foi possível atualizar dados"
