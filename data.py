import os
from employee import *


def writeToDataBase(employee):
    """escreve os dados dos empregados no banco de dados"""
    file = open(f'dataBase\\employees.db\\{employee.getId()}', 'w', encoding='utf8')
    file.write(f"{employee}")
    file.flush()
    file.close()


def writeTimeCardToDataBase(timecards, Id):
    """escreve o cartão de ponto no banco de dados"""
    file = open(f'dataBase\\timecard.db\\{Id}', 'w', encoding='utf8')
    for timecard in timecards:
        file.write(f"{timecard}\n")
    file.flush()
    file.close()


def writeSellToDataBase(sellresults, Id):
    """escreve os resultados de vendas no banco de dados"""
    file = open(f'dataBase\\sellresults.db\\{Id}', 'w', encoding='utf8')
    for sell in sellresults:
        file.write(f"{sell}\n")
    file.flush()
    file.close()


def readFromDataBase(opt=None):
    """lê os dados dos empregados no banco dados e os retorna em um dicionário"""

    # APANHA APENAS AS IDS
    if opt == 'getIds':
        return os.listdir('dataBase\\employees.db')

    # APANHA TODOS OS DADOS PESSOAIS
    dataBase = {}
    for Id in os.listdir('dataBase\\employees.db'):  # lista todas as Ids presentes em dataBase\\employees.db
        file = open(f'dataBase\\employees.db\\{Id}', 'r', encoding='utf8')  # abre o arquivo com o nome da Id
        dataBase[eval(Id)] = eval(file.read())
        file.close()
    return dataBase


def readTimeCardsFromDataBase(opt=None):
    """lê os os cartões de ponto dos empregados no banco de dados e os retorna em um dicionário"""

    if opt == 'timecards':
        return os.listdir('dataBase\\timecard.db')

    # APANHA OS CARTÕES DE PONTO DE TODOS OS EMPREGADOS
    timeCards = {}
    for Id in os.listdir('dataBase\\timecard.db'):  # lista todas as Ids presentes em dataBase\\timecard.db
        file = open(f'dataBase\\timecard.db\\{Id}', 'r', encoding='utf8')  # abre o arquivo com o nome da Id
        timeCards[eval(Id)] = file.read().splitlines()
        file.close()
    return timeCards


def readSellResultsFromDataBase(opt=None):
    """lê os resultados de vendas no banco de dados e os retorna em um dicionário"""

    if opt == 'sellresults':
        return os.listdir('dataBase\\sellresults.db')

    # APANHA OS RESULTADOS DE VENDAS DE TODOS OS EMPREGADOS
    sellResults = {}
    for Id in os.listdir('dataBase\\sellresults.db'):  # lista todas as Ids presentes em dataBase\\timecard.db
        file = open(f'dataBase\\sellresults.db\\{Id}', 'r', encoding='utf8')  # abre o arquivo com o nome da Id
        sellResults[eval(Id)] = file.read().splitlines()
        file.close()
    return sellResults
