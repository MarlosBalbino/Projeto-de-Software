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
                  8: Schedule.schedules,
                  9: Schedule.newSchedules,
                  10: PrintData.printDataBase,
                  11: PrintData.printTimeCards,
                  12: PrintData.printSellResults,
                  13: PrintData.printSyndicate,
                  14: PrintData.printSchedules,
                  15: PrintData.printScheduleList,
                  16: PrintData.printPaychecks,
                  17: UndoRedo.undo,
                  18: UndoRedo.redo,
                  -1: EmployeeCRUD.eraseDataBase,
                  -2: TimeCard.setHours,
                  -3: TimeCard.setExtra,
                  0: Exit.end}
        done = switch[case]()
        if done is not None:
            return 1
