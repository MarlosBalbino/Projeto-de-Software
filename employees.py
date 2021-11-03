import random

def emptyEmployees():
    '''Cria e retorna uma lista vazia de empregados'''

    employees = {}
    return employees

def addEmployee(employees):
    '''Adiciona um novo empregado e seus dados'''

    name = input("Digite o nome do novo empregado:\n")
    adress = input("Digite o endereço:\n")
    employeeType = input("Digite o tipo de empregado:\n")
    atrib = input("Digite o salário:\n")


    if employees: #verifica se a lista de empregados está vazia

        id = random.randrange(0, 10000) #gera um id aleatório.
        while True:
            if id in employees.keys():  #verifica se o id gerado já está na lista
                id = random.randrange(0, 10000) #caso esteja, gera um novo id.
            else:
                break
    else:
        id = 0

    aux = {
        id: [name, adress,
        employeeType, atrib, id]} #dicionário auxiliar - serve como update para employees.

    employees.update(aux)         #atualiza a lista de empregados.

    print('\n..Empregado adicionado com sucesso')
    print()

def removeEmployee(employees):
    '''Remove um empregado'''

    key = eval(input('Digite o id do empregado:\n'))

    if key in employees.keys():
        employees.pop(key)
        print('\n..Empregado removido com sucesso')
    else:
        print('Empregado não encontrado')

    print()
