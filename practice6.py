
#Creating A class
class buy:
    def __init__(self):
        self.pName=""
        self.pDes=""
        self.pCategory=""
        self.pPrice=0
        self.pFound=False
    def addProduct(self):
        self.pName=input("Enter product name:\n")
        self.pDes=input("Enter product description:\n")
        self.pCategory=input("Enter product category:\n")
        self.pPrice=int(input("Enter the product price"))
        self.pFound=False
    def findProduct(self):
        if self.pName=="":
            print("\n not in the system\n")
            return
        self.sCategory=input("Search for Category:\n")
        self.minPrice=int(input("Enter minimum price:\n"))
        self.maxPrice=int(input("Enter Maximum price:\n"))
        if self.pCategory==self.sCategory and self.maxPrice :
            self.pFound=True
            print(f"Product\t{self.pName}\tfound\n")
        else:
            self.pFound=False
            print("No product Found\n")
    def myCart(self):
        if self.pFound and self.pName!="":
            print("\tProduct Name\t\tDescription\t\tCategory\t\tPrice")
            print(f"\t{self.pName}\t\t\t{self.Des}\t\t\t{self.pCategory}\t\t\t{self.pPrice}")
        else:
            print("Cart empty")
    def exitProgram(self):
        print("Exits Program\n")
b=buy()
runs=True
while runs:
    print("*"*50)
    print("\t\t\t1.Add New Product\n")
    print("\t\t\t2.Find Product\n")
    print("\t\t\t3.My cart\n")
    print("\t\t\t4.Exit\n")
    print("*"*50)
    userchoice=int(input("Select your choice\n"))
    if userchoice==1:
        b.addProduct()
    elif userchoice==2:
        b.findProduct()
    elif userchoice==3:
        b.myCart
    else:
        print("Invalid choice\n")
    if runs:
        input("\nPress Enter")