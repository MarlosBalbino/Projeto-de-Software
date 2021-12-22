from management.Imports import *


class CaseHandle:

    @staticmethod
    def switch(case):
        switch = {1: EmployeeCRUD.add,
                  2: EmployeeCRUD.remove,
                  3: TimeCard.setTimeCard,
                  4: SellResult.setSellResult,
                  5: Service.setServiceFee,
                  6: EmployeeCRUD.update,
                  7: PayRoll.run,
                  # 8: undoRedo.undo,
                  # 8.1: undoRedo.redo,
                  9: Schedule.schedules,
                  10: Schedule.newSchedules,
                  11: PrintData.printDataBase,
                  12: PrintData.printTimeCards,
                  13: PrintData.printSellResults,
                  14: PrintData.printSyndicate,
                  15: PrintData.printSchedules,
                  16: PrintData.printScheduleList,
                  -1: EmployeeCRUD.eraseDataBase,
                  -2: TimeCard.setHours,
                  -3: TimeCard.setExtra,
                  0: Exit.end}
        switch[case]()
