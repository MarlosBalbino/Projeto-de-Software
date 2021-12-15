import sqlite3


class DataBase:

    def __init__(self, name = 'dataBase\\banco.db'):
        """define o nome e o caminho do banco de dados"""
        self.name = name

    def connect(self):
        """conecta ao banco de dados"""
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        """fecha a conexão com o banco de dados"""
        self.connection.close()

    def createTable(self, table):
        cursor = self.connection.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table}(
                NOME TEXT,
                ENDEREÇO TEXT,
                TIPO_DE_EMPREGADO TEXT,
                ID INTEGER,
                
                PRIMARY KEY(ID));  
        """)

    def registerEmployee(self, data, table):
        fieldTable = ('NOME', 'ENDEREÇO', 'TIPO_DE_EMPREGADO', 'ID')

        qnt = '?, ?, ?, ?'
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT OR IGNORE INTO {table} {fieldTable}
            VALUES({qnt})""", data)

            self.connection.commit()
            return "Registrado com sucesso"
        except NameError:
            return "Não foi possível registrar no banco de dados"

    def selectAllEmployees(self, table):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM {table} ORDER BY ID")
            employees = cursor.fetchall()
            return employees
        except:
            print(f'não foi possível acessar a tabela: {table}')
            return -1

    def removeEmployee(self, Id, table):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM {table} WHERE ID = {Id}")
            self.connection.commit()

            return "Empregado removido com sucesso"
        except:
            return "Erro ao remover empregado"

    def updateEmployee(self, data, table):

        # ENDEREÇO = '{data[1]}',
        # TIPO_DE_EMPREGADO = '{data[2]}',
        # ID = {data[3]},
        try:
            cursor = self.connection.cursor()

            cursor.execute(f""" UPDATE {table} SET
                NOME = '{data[0]}',
                ENDEREÇO = '{data[1]}',
                TIPO_DE_EMPREGADO = '{data[2]}',
                ID = {data[3]}                
                
                WHERE ID = {data[3]}""")

            self.connection.commit()
            return "Dados atualizados com sucesso"

        except NameError:
            return "Não foi possível atualizar dados"
