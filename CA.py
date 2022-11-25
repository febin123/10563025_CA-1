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
        computeWeeklyPay=(self.weeklyhours*self.rate)+(self.overtimeRate*hours)
        print(computeWeeklyPay)



#creating objects of the class
e1=Employee('febin',35,11,15,20)

#returning the computeWeekly pay
e1.computeWeeklyPay(4)

