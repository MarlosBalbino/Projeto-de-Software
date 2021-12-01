import os
import time
import data
import random
from employee import *
from mytime import Time


def employeeInfo():
    """returna uma lista com a classe e uma string indicando o tipo do empregado"""

    while True:
        opt = eval(input('Digite o tipo de empregado:\n'
                         '1 - Horista\n'
                         '2 - Salariado\n'
                         '3 - Comissionado\n'))
        if opt == 1:
            return [Hourly, 'Horista', eval(input('Salário horário:\n'))]
        elif opt == 2:
            return [Salaried, 'Salariado', eval(input('Salário mensal:\n'))]
        elif opt == 3:
            return [Commissioned, 'Comissionado', eval(input('Comissão:\n'))]
        else:
            print('Tipo de empregado inválido, digite novamente:')


def addEmployee():
    """adiciona um novo empregado ao banco de dados"""
    name = input('Digite o nome de um empregado\n')
    address = input('Digite o endereço\n')
    empInfo = employeeInfo()  # recebe uma lista = [tipo (classe), tipo em string, Remuneração)]

    Id = random.randrange(100000)
    while str(Id) in data.readFromDataBase(opt='Ids'):  # recebe uma lista com todas as Ids existentes
        Id = random.randrange(100000)

    emp = empInfo[0](name, address, empInfo[1], Id, empInfo[2])
    data.writeToDataBase(emp)  # escreve dados do empregado no banco de dados
    print('Empregado cadastrado com sucesso')


def removeEmployee():
    """remove um empregado do banco de dados"""

    Id = verifyEmployee()
    if Id != -1:
        opt = eval(input('Tem certeza que deseja remover esse empregado?\n'
                         '1 - Sim\n'
                         '0 - Não\n'))
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

        # LÊ EMPREGADO NO BANCO DE DADOS
        file = open(f'dataBase\\employees.db\\{Id}', 'r', encoding='utf8')
        emp = eval(file.read())
        file.close()

        # VERIFICA SE É DO TIPO HORÁRIO
        if type(emp) != Hourly:
            print('Esse empregado não é horista')
            return None

        try:
            new_timecard = time.strftime('%d/%m/%y %H:%M')
            timecardList = data.readTimeCardsFromDataBase(opt='timecards')
            timecards = []

            # RECUPERA CARTÕES DE PONTO, CASO EXISTAM
            if str(Id) in timecardList:
                file = open(f'dataBase\\timecard.db\\{Id}', 'r', encoding='utf8')
                timecards = file.read().splitlines()
                file.close()

                # CALCULA AS HORAS TRABALHADAS NO DIA
                if len(timecards) % 2 != 0:
                    last_timecard = timecards[-1]  # pega o último cartão de ponto registrado
                    h_final = new_timecard.split()[-1]  # obtém a hora final
                    h_initial = last_timecard.split()[-1]  # obtém a hora inicial
                    # Δh = hora_final - hora_inicial
                    h_final = Time(h_final)
                    h_initial = Time(h_initial)
                    delta_h = h_final - h_initial
                    emp.setWorkingHours(delta_h.getHours())
                    data.writeToDataBase(emp)

            # ADICIONA NOVO CARTÃO DE PONTO
            timecards.append(new_timecard)
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
            sellresultList = data.readSellResultsFromDataBase(opt='sellresults')
            sellresults = []
            if str(Id) in sellresultList:
                file = open(f'dataBase\\sellresults.db\\{Id}', 'r', encoding='utf8')
                sellresults = file.read().splitlines()
                file.close()
            sellresults.append(sellresult)
            data.writeSellToDataBase(sellresults, Id)
            print('Venda adicionada com sucesso.')

        except FileNotFoundError:
            print(FileNotFoundError('Não foi possível adicionar venda'))


def setServiceRate():
    """Lança uma taxa de serviço"""
    pass


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
            empInfo = []

            # armazena as informações do tipo de empregado em empInfo
            if type(emp) == Hourly:
                empInfo.append(Hourly)
                empInfo.append(Type)
                empInfo.append(emp.getHourlySalary())

            elif type(emp) == Salaried:
                empInfo.append(Salaried)
                empInfo.append(Type)
                empInfo.append(emp.getSalary())

            else:
                empInfo.append(Commissioned)
                empInfo.append(Type)
                empInfo.append(emp.getCommission())

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
                    empInfo = employeeInfo()  # recebe uma lista = [tipo (classe), tipo (em string), remuneração]
                else:
                    break

            # ATUALIZA OS DADOS DOS EMPREGADOS
            # empInfo[0]: tipo do empregado
            # empInfo[1]: string do tipo do empregado
            # empInfo[2]: remuneração
            updatedEmp = empInfo[0](name, address, empInfo[1], Id, empInfo[2])
            data.writeToDataBase(updatedEmp)

        except FileNotFoundError:
            print(FileNotFoundError('Não foi possível alterar os dados do empregado'))


def payRoll():
    """roda a folha de pagamento"""
    pass


def UndoRedo():
    """desfaz e refaz ação"""
    pass


def paymentSchedule():
    """cria uma agenda de pagamento"""
    pass


def newPaymentSchedules():
    """cria novas agendas de pagamento"""
    pass


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
            sameNameEmp = {}  # dicionário para empregados de mesmo nome.
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
    """imprime os dados dos empregados"""

    # VERIFICA SE HÁ EMPREGADOS CADASTRADOS
    dataBase = data.readFromDataBase()
    if not dataBase:
        print('Não há empregados cadastrados no sistema')
        return None

    # IMPRIME OS DADOS PESSOAIS DOS EMPREGADOS
    for Id in dataBase:
        print(f'{dataBase[Id].getData()}\n')


def printTimeCards():
    """imprime os cartões de ponto de todos os empregados"""

    # VERIFICA SE HÁ EMPREGADOS CADASTRADOS
    dataBase = data.readFromDataBase()
    if not dataBase:
        print('Não há empregados cadastrados no sistema')
        return None

    # VERIFICA SE HÁ CARTÕES DE PONTO
    timeCards = data.readTimeCardsFromDataBase()
    if not timeCards:
        print('Não há cartões de ponto no sistema')
        return None

    # IMPRIME OS CARTÕES DE PONTO
    for Id in timeCards:
        emp = dataBase[Id]
        print(f'\n{Id} : {emp.getName()}')
        for timecard in timeCards[Id]:
            print(f'{timecard}')
    print()


def printSellResults():
    """imprime os resultados de vendas de todos os empregados"""

    # VERIFICA SE HÁ EMPREGADOS CADASTRADOS
    dataBase = data.readFromDataBase()
    if not dataBase:
        print('Não há empregados cadastrados no sistema')
        return None

    # VERIFICA SE HÁ RESULTADOS DE VENDAS
    sellResults = data.readSellResultsFromDataBase()
    if not sellResults:
        print('Não há resultados de vendas no sistema')
        return None

    # IMPRIME OS RESULTADOS DE VENDAS
    for Id in sellResults:
        emp = dataBase[Id]
        print(f'\n{Id} : {emp.getName()}')
        for result in sellResults[Id]:
            print(f'{result}')
    print()


if __name__ == "__main__":
    pass

