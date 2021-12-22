from dataBase.data import scheduleList


class InvalidDayError(Exception):
    pass


class FillSchedule:

    def __init__(self):
        self.__type_ = None
        self.__day = None
        self.__description = None
        self.__key = None
        self.__list_ = 0

    def setSchedule(self):
        while True:
            try:
                self.__type_ = eval(input('O pagamento será feito:\n'
                                          '1 - semanalmente\n'
                                          '2 - mensalmente\n'
                                          '3 - bi-mensalmente\n'))
                break
            except:
                print('Digite umas das opções acima.')

        if self.__type_ == 1:
            while True:
                try:
                    self.__day = eval(input('Digite o dia da semana:\n'
                                            '1 - segunda\n'
                                            '2 - terca\n'
                                            '3 - quarta\n'
                                            '4 - quinta\n'
                                            '5 - sexta\n'
                                            '6 - sabado\n'))
                    break
                except:
                    print('Digite umas das opções acima')

        elif self.__type_ == 2:
            while True:
                try:
                    self.__day = eval(input('Digite um dia do mês:\n'))
                    if self.__day < 1 or self.__day > 31:
                        print('Digite um número entre 1-31')
                        continue
                    break
                except:
                    print('Digite um número entre 1-31')

        else:
            while True:
                try:
                    self.__day = eval(input('Digite um dia do mês:\n'))
                    if self.__day < 1 or self.__day > 31:
                        print('Digite um número entre 1-31')
                        continue
                    break
                except:
                    print('Digite um número entre 1-31')

            second_day = self.__day + 14
            if second_day > 31:
                second_day = second_day - 31
                print(f'O pagamento será feito no dia {self.__day} e no dia {second_day} do próximo mês')
            else:
                print(f'O pagamento será feito no dia {self.__day} e no dia {second_day}')

        self.__description = input('Digite uma descrição para a agenda (em string):\n')

    @staticmethod
    def list():
        while True:
            opt = eval(input('Deseja listar as agendas existentes?\n'
                             'Digite: 1 - Sim.'
                             '        0 - Não.\n'))
            if opt == 1 or opt == 0:
                return opt
            else:
                print('Digite 0 ou 1')

    def setScheduleKey(self):
        print(18 * '=' + ' Agendas ' + 18 * '=')
        for key in scheduleList:
            description = scheduleList[key][0]
            print(f'{key} - {description}')
        print(f'\nDigite uma opção de 1 a {len(scheduleList)} ou 0 para sair:')

        while True:
            try:
                opt = eval(input())
                if opt == 0:
                    return None
                if opt in scheduleList:
                    break
            except:
                print('Digite uma das opções acima ou 0 para sair')
        self.__key = opt

    def getKey(self):
        return self.__key

    def getScheduleType(self):
        return self.__type_

    def getDay(self):
        return self.__day

    def getDescription(self):
        return self.__description



