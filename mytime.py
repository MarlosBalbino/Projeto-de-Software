import time
from datetime import timedelta


class TimeError(Exception):
    """Exceção é levantada quando
    há uma diferença de tempo cujo o subtraendo é maior que o minuendo.
    Ou seja, o resultado não pode ser negativo (tempo >= 0)"""
    pass


class Time:
    """classe de tempo definida pelo usuário"""

    def __init__(self, _hour=None):
        """captura a data e hora atual do sistema."""

        if not _hour:
            self.__date = time.strftime('%d/%m/%y %H:%M:%S')  # dia/mês/ano 00:00:00
            self.__hour = self.__date.split()[-1]  # 00:00:00
        else:
            self.__date = time.strftime('%d/%m/%y') + ' ' + _hour
            self.__hour = _hour

        # def formatToSeconds(_hour, ratio=(36000, 3600, None, 600, 60, None, 10, 1), index=-1):
        #     try:
        #         return eval(_hour[index]) * ratio[index] + formatToSeconds(_hour, ratio, index - 1)
        #     except SyntaxError:
        #         return formatToSeconds(_hour, ratio, index - 1)
        #     except IndexError:
        #         return 0

        def formatToSeconds(_hour):
            index = -1
            ratio = (36000, 3600, None, 600, 60, None, 10, 1)
            seconds = 0
            while True:
                try:
                    seconds += eval(_hour[index]) * ratio[index]
                except SyntaxError:
                    pass
                except IndexError:
                    break
                index -= 1
            return seconds

        self.__seconds = formatToSeconds(self.__hour)
        self.__hours = self.__seconds/3600

    def getHour(self):
        """retorna a hora no formato 00:00:00"""
        return self.__hour

    def getHours(self):
        """retorna as horas correntes"""
        return self.__hours

    def getDate(self):
        """retorna a data e hora"""
        return self.__date

    def getSeconds(self):
        """retorna a hora em segundos"""
        return self.__seconds

    @staticmethod
    def timeDelta(seconds=0):
        """retorna os segundos no formato 00:00:00"""
        return str(timedelta(seconds=seconds))

    def __repr__(self):
        return f'Time({str(timedelta(seconds=self.__seconds))})'

    def __str__(self):
        return f'{str(timedelta(seconds=self.__seconds))}'

    def __sub__(self, h_initial):
        """subtrai as horas"""
        if h_initial.__seconds > self.__seconds:
            raise TimeError('tempo final menor que o tempo inicial')
        return Time(str(timedelta(seconds=self.__seconds - h_initial.__seconds)))

