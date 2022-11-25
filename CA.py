class Employee:
    #constructor
    def __init__(self,name,weeklyhours,rate,overtimeRate,weeklytaxcredit):
        self.name=name
        self.weeklyhours=weeklyhours
        self.rate=rate
        self.overtimeRate=overtimeRate
        self.weeklytaxcredit=weeklytaxcredit


    #Created a method computeWeeklyPay (self,hours)
    def computeWeeklyPay(self,hours):
        grossPay=(self.weeklyhours*self.rate)+(self.overtimeRate*hours)
        print(grossPay)


    #craeted a method computeTax(self,grossPay) 
    def computeTax(self,grossPay):
        computeTax=(0.4*grossPay)-self.weeklytaxcredit
        print(computeTax)

#creating objects of the class
e1=Employee('febin',35,11,15,70)

#returning the grosspay pay
e1.computeWeeklyPay(4)

#returns the tax due at 40% on the gross pay, reduced by the tax credit
e1.computeTax(grossPay=445)

