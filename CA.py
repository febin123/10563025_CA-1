class Employee:
    #constructor
    def __init__(self,name,weeklyhours,rate,overtimeRate,weeklytaxcredit):

         #checks the overtimeRate cannot be less than 0 
        if(overtimeRate<0):
            raise ValueError('Please enter correct input;It cannot be less than 0') 


        self.name=name
        self.weeklyhours=weeklyhours
        self.rate=rate
        self.overtimeRate=overtimeRate
        self.weeklytaxcredit=weeklytaxcredit

       

    #Created a method computeWeeklyPay (self,hours)
    def computeWeeklyPay(self,hours):
        grossPay=(self.weeklyhours*self.rate)+(self.overtimeRate*hours)

        # grossPay=-20 tested negative value

          #checks the grosspay cannot be less than 0
        if(grossPay<0):
            raise ValueError('Value is negative; Please enter correct input')

        print(grossPay)

      


    #craeted a method computeTax(self,grossPay) 
    def computeTax(self,grossPay):
        computeTax=(0.4*grossPay)-self.weeklytaxcredit

        # computeTax=-20 tested negative value

         #checks the tax cannot be less than 0
        if(computeTax<0):
            raise ValueError('Value is negative; Please enter correct input')

        print(computeTax)

       



#creating objects of the class
e1=Employee('febin',35,11,15,70)

#returning the grosspay pay
e1.computeWeeklyPay(4)

#returns the tax due at 40% on the gross pay, reduced by the tax credit
e1.computeTax(grossPay=445)

