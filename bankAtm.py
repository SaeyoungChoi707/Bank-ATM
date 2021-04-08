class Atm(object):
    def __init__(self,bank_name,card_number,pin_number):
        self.bank_name = bank_name
        self.card_number = card_number
        self.pin_number = pin_number
    
    def balanceEnquiry(self):
        print("Captain Pinepapple on Blueberry Island in the Syrup Ocean")
        

    def cashWithdrawl(self):
        print("Captain Meows versus Captain BarkBark on Island Radio")


blehSr = Atm("Fruity Bank", 7070606, 7070707)
print("Bank Name : ", blehSr.bank_name)
print("Card Number : ", blehSr.card_number)
print("Pin Number : ", blehSr.pin_number)

blehSr.balanceEnquiry()
blehSr.cashWithdrawl()
