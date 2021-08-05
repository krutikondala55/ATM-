class atm(object):
    def _init_(self,CashWithdrawl, BalanceEnquiry, Atmcardnumber, Pincode):
        self.CashWithdrawl=CashWithdrawl
        self.BalanceEnquiry=BalanceEnquiry
        self.Atmcardnumber=Atmcardnumber
        self.Pincode=Pincode


    def CashWithdrawl(self):
        print('CashWithdrawled')
    
    def BalanceEnquiry(self):
        print('BalanceEnquiryed')

    def Atmcardnumber(self):
        print('ATM_Cardnumber')

    def Pincode(self,gear_type):
        print('pincode')


    