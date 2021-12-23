from dataBase import data as dt
from employee.Imports import *
from management.extraModules.mycalendar import Calendar
from management.paycheck.paycheck import Paycheck
from management.extraModules.findInSyndicate import FindSyndicate
from os import system


class PayRoll:

    INSS = 7.5
    FGTS = 8
    payed = 0

    @classmethod
    def __pay(cls, Id):
        employee = dt.dynamicDataBase[Id]
        name = employee.getName()
        payment = employee.getPayment()
        unionFee = 0
        serviceFee = 0
        hourlySalary = 0
        workingHours = 0
        extraHours = 0
        commission = 0
        periodCommission = 0

        find = FindSyndicate()
        find.search(Id)
        if find.found() == 1:
            syndicateId = find.getSyndicateId()
            syndicate = dt.dynamicSyndicateDB[syndicateId]
            serviceFee = syndicate.getServiceFee()
            unionFee = syndicate.getUnionFee()

        if type(employee) == Hourly:
            workingHours = employee.getWorkingHours()
            extraHours = employee.getExtraWorkingHours()
            hourlySalary = employee.getHourlySalary()

            salary = hourlySalary * workingHours
            extraRate = ((1.5/100) * hourlySalary) + hourlySalary
            extraSalary = extraRate * extraHours
            grossSalary = salary + extraSalary

        elif type(employee) == Salaried:
            salary = employee.getSalary()
            grossSalary = salary

        else:
            salary = employee.getSalary()
            commission = employee.getCommission()
            periodCommission = employee. getPeriodCommission()
            grossSalary = salary + periodCommission

        serviceDiscount = (serviceFee/100) * grossSalary
        unionDiscount = (unionFee/100) * grossSalary
        INSSDiscount = (cls.INSS/100) * grossSalary
        FGTSDiscount = (cls.FGTS/100) * grossSalary

        totalDiscounts = serviceDiscount + unionDiscount + INSSDiscount + FGTSDiscount
        netSalary = grossSalary - totalDiscounts

        paycheck = Paycheck(name, Id, unionFee, serviceFee, cls.INSS, cls.FGTS, grossSalary,
                            netSalary, totalDiscounts, hourlySalary, workingHours, extraHours,
                            commission, periodCommission, payment)

        paycheck.setDiscounts(serviceDiscount, unionDiscount, INSSDiscount, FGTSDiscount)
        print(f"{16*'='} Contracheque {16*'='}")
        print(paycheck.payCheck())
        print(paycheck.printDiscounts())
        print()
        dt.paycheckDB[Id] = paycheck
        dt.DataBaseManager.writePaycheckDB()
        system('pause')

    @classmethod
    def __weekly(cls, day, Id):
        if day == Calendar.currentDay():
            cls.__pay(Id)
            cls.payed = 1

    @classmethod
    def __monthly(cls, day, Id):
        lastMonthDay = Calendar.lastMonthDay()
        currentMonthDay = Calendar.currentMonthDay()
        if day == currentMonthDay or day > lastMonthDay:
            cls.__pay(Id)
            cls.payed = 1

        secondDay = day + 14
        if secondDay > lastMonthDay:
            secondDay = secondDay - lastMonthDay
        if secondDay == currentMonthDay:
            cls.__pay(Id)
            cls.payed = 1

    @classmethod
    def run(cls):
        for Id in dt.scheduleDB:
            day = dt.scheduleDB[Id][2]
            scheduleType = dt.scheduleDB[Id][1]
            switch = {1: cls.__weekly,
                      2: cls.__monthly,
                      3: cls.__monthly}
            switch[scheduleType](day, Id)
        if cls.payed == 0:
            print('Não há nem um pagamento agendado pra hoje.')
            system('pause')
            return None
        return 1

