from dataBase import data


def verifyEmployee():
    """verifica se o empregado existe no banco de dados"""

    if not data.dynamicDataBase:
        print('Não há empregados cadastrados no sistema')
        return -1

    else:
        empId = input('Digite a Id ou nome do empregado:\n')
        try:
            # verifica se empId é um número.
            empId = eval(empId)
            if empId in data.dynamicDataBase:
                return empId
            else:
                print('Empregado não foi encontrado')
                return -1

        except:
            # caso empId seja um nome, procura todos os empregados de mesmo nome no banco de dados.
            sameNameEmp = {}  # dicionário para empregados de mesmo nome.
            for key in data.dynamicDataBase.keys():
                emp = data.dynamicDataBase[key]
                if empId == emp.getName():
                    sameNameEmp[key] = data.dynamicDataBase[key]

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