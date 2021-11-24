import os
import time
import random
from employee import *
from data import DataBase as data


def addEmployee():
    """adiciona um novo empregado ao banco de dados"""

    name = input('Digite o nome de um empregado\n')
    address = input('Digite o endereço\n')
    empType = employeeType()  # recebe uma lista = [Tipo classe), Tipo em string)]
    remuneration = eval(input('Digite o salário horário, salário mensal ou comissão:\n'))

    Id = random.randrange(100000)
    while str(Id) in data.readFromDataBase(opt='Ids'):
        Id = random.randrange(100000)

    emp = empType[0](name, address, empType[1], Id, remuneration)
    data.writeToDataBase(emp)
    print('Empregado cadastrado com sucesso')


def removeEmployee():
    """remove um empregado do banco de dados"""

    Id = verifyEmployee()
    if Id != -1:
        opt = eval(input('Tem certeza que deseja remover esse empregado?\n'
                         '1 - Sim\n'
                         '0 - Não'))
        if opt == 1:
            try:
                os.remove(f'dataBase\\employees.db\\{Id}')
                print('Empregado removido com sucesso')
            except OSError:
                print(f"Erro: {OSError('não foi possível remover o empregado')}")
            try:
                os.remove(f'dataBase\\timecard.db\\{Id}')
            except OSError:
                pass
        else:
            print('Operação abortada!')


def setTimeCard():
    """lança um cartão de ponto"""
    Id = verifyEmployee()
    if Id != -1:
        try:
            timecard = time.strftime('%d/%m/%y %H:%M')
            timeCardList = data.readFromDataBase(opt='timecards')
            timecards = []
            if str(Id) in timeCardList:
                file = open(f'dataBase\\timecard.db\\{Id}', 'r', encoding='utf8')
                timecards = file.read().splitlines()
                file.close()
            timecards.append(timecard)
            data.writeTimeCardToDataBase(timecards, Id)
            print('Cartão de ponto adicionado com sucesso.')

        except FileNotFoundError:
            print(FileNotFoundError('Não foi possível lançar o cartão de ponto'))


def setSellResult():
    """lança um cartão de ponto"""
    Id = verifyEmployee()
    if Id != -1:
        try:
            sellresult = input('Forneça um comprovante de venda:\n')
            sellResultList = data.readFromDataBase(opt='sellresults')
            sellresults = []
            if str(Id) in sellResultList:
                file = open(f'dataBase\\sellresults.db\\{Id}', 'r', encoding='utf8')
                sellresults = file.read().splitlines()
                file.close()
            sellresults.append(sellresult)
            data.writeSellToDataBase(sellresults, Id)
            print('Venda adicionada com sucesso.')

        except FileNotFoundError:
            print(FileNotFoundError('Não foi possível adicionar venda'))


def changeEmployeeData():
    """altera os dados de um empregado"""

    Id = verifyEmployee()
    if Id != -1:
        try:
            file = open(f'dataBase\\employees.db\\{Id}', 'r', encoding='utf8')
            emp = eval(file.read())
            file.close()

            # RECUPERA DADOS DO EMPREGADO
            name = emp.getName()
            address = emp.getAddress()
            Type = emp.getEmployeeType()
            auxType = []

            # armazena o tipo de empregado (classe) no índice 0 de auxType
            if type(emp) == Hourly:
                remuneration = emp.getWorkingHours()
                auxType.append(Hourly)
            elif type(emp) == Salaried:
                remuneration = emp.Salary()
                auxType.append(Salaried)
            else:
                remuneration = emp.Commission()
                auxType.append(Commissioned)

            # armazena o tipo de empregado em string no índice 1 de auxType
            auxType.append(Type)

            # INTERAÇÃO COM O USUÁRIO
            while True:
                opt = eval(input('Digite a opção que deseja alterar:\n'
                                 '1 - nome:\n'
                                 '2 - endereço\n'
                                 '3 - tipo de empregado\n'
                                 '0 - sair\n'))

                if opt == 1:
                    name = input('Digite um novo nome:\n')
                elif opt == 2:
                    address = input('Digite um novo endereço:\n')
                elif opt == 3:
                    auxType = employeeType()  # recebe uma lista = [Tipo classe), Tipo em string)]
                else:
                    break

            # ATUALIZA OS DADOS DOS EMPREGADOS
            updatedEmp = auxType[0](name, address, auxType[1], Id, remuneration)
            data.writeToDataBase(updatedEmp)

        except FileNotFoundError:
            print(FileNotFoundError('Não foi possível alterar os dados do empregado'))


def employeeType():
    """returna uma lista com a classe e uma string indicando o tipo do empregado"""
    employees = {1: [Hourly, 'Horista'],
                 2: [Salaried, 'Salariado'],
                 3: [Commissioned, 'Comissionado']}
    while True:
        try:
            opt = eval(input('Digite o tipo de empregado:\n'
                             '1 - Horista\n'
                             '2 - Salariado\n'
                             '3 - Comissionado\n'))
            return employees[opt]

        except KeyError:
            print('Tipo de empregado inválido')


def verifyEmployee():
    """verifica se o empregado existe no banco de dados"""

    dataBase = data.readFromDataBase()
    if not dataBase:
        print('Não há empregados cadastrados no sistema')
        return -1

    else:
        empId = input('Digite a Id ou nome do empregado:\n')
        try:
            # verifica se empId é um número.
            empId = eval(empId)
            if empId in dataBase.keys():
                return empId
            else:
                print('Empregado não foi encontrado')
                return -1

        except:
            # caso empId seja um nome, procura todos os empregados de mesmo nome no banco de dados.
            sameNameEmp = {}  # dicionário com empregados de mesmo nome.
            for key in dataBase.keys():
                emp = dataBase[key]
                if empId == emp.getName():
                    sameNameEmp[key] = dataBase[key]

            if len(sameNameEmp) == 1:
                for key in sameNameEmp.keys():
                    empId = key

            elif len(sameNameEmp) > 1:  # verifica se existe mais de um empregado com o mesmo nome.
                print(f'Empregados com o nome {empId}:\n')
                for key in sameNameEmp.keys():
                    print(f'{sameNameEmp[key].getData()}\n')

                empId = eval(input('Escolha um empregado digitando sua Id:\n'))
                while empId not in sameNameEmp.keys():
                    empId = eval(input('Id inválida. Digite novamente:\n'))

            else:
                print('Empregado não foi encontrado')
                return -1
            return empId


def printDataBase():
    """imprime todos empregados"""
    dataBase = data.readFromDataBase()
    for key in dataBase:
        print(f'{dataBase[key].getData()}\n')


def printTimeCards():
    """imprime o cartão de ponto de todos os empregados"""
    timeCards = data.readFromDataBase(opt='alltimecards')
    for key in timeCards:
        print(f'\n{key}:')
        for timecard in timeCards[key]:
            print(f'{timecard}')
    print()



if __name__ == "__main__":
    #addEmployee()
    print(verifyEmployee())
    #changeEmployeeData()
    # print(verifyEmployee())

