class Employee:
    #constructor
    def __init__(self,name,weeklyhours,rate,overtimeRate,weeklytaxcredit):
        self.name=name
        self.weeklyhours=weeklyhours
        self.rate=rate
        self.overtimeRate=overtimeRate
        self.weeklytaxcredit=weeklytaxcredit

#creating objects of the class
e1=Employee('febin',20,10,5,20)

print(e1.weeklyhours)
