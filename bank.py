class bank:
    def __init__(self):
        self.bankBalance==0
    def registerCustomer(self):
        self.accNo=input("Enter Account Number\n")
        self.name=input("Enter Name\n")
        self.branchName=input("Enter Branch Name\n")
    def depositCash(self):
        self.depositCash=input("Enter amount deposited\n")
        self.depositCash+=self.depositCash
    def withdrawCash(self):
        self.withdrawCash=input("Enter the amount withdrawn\n")
        self.bankBalance-=self.withdrawCash
    def checkBalance(self):
        print(f"Enter the back balance of\t{self.accNo}:{self.name} is {self.bankBalance}")
#Continuation