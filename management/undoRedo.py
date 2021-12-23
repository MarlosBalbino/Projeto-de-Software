from dataBase import data as dt
from os import system
import copy


class UndoRedo:

    state = list()
    index = -1

    @classmethod
    def saveState(cls):

        lst = copy.deepcopy([dt.dynamicDataBase, dt.dynamicTimeCards, dt.dynamicSellResults,
                             dt.dynamicSyndicateDB, dt.scheduleDB, dt.scheduleList, dt.paycheckDB])
        cls.state.append(lst)
        cls.index += 1

    @classmethod
    def __loadState(cls):
        print(45*'=')
        lst = copy.deepcopy(cls.state[cls.index])
        dt.dynamicDataBase = lst[0]
        dt.dynamicTimeCards = lst[1]
        dt.dynamicSellResults = lst[2]
        dt.dynamicSyndicateDB = lst[3]
        dt.scheduleDB = lst[4]
        dt.scheduleList = lst[5]
        dt.paycheckDB = lst[6]
        dt.DataBaseManager.writeAll()
        print('Feito!!\n')
        system('pause')

    @classmethod
    def undo(cls):
        if cls.index > 0:
            cls.index -= 1
        cls.__loadState()
    
    @classmethod
    def redo(cls):
        if cls.index < len(cls.state)-1:
            cls.index += 1
        cls.__loadState()

