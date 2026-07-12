def addProduct():
    productName=input("Enter the product name\n")
    productDescription=input("Enter the product description\n")
    productCategory=input("Enter the product category\n")
    price=input("Enter the price\n")
    
    return productName, productDescription, productCategory, price
    
def findProduct():
    search=input("Enter the product\n")
    category=input("Enter the category of the object\n")
    minimumPrice=float (input("Enter the minimum price\n"))
    maximumPrice=float(input("Enter the maximum price\n"))
    
    return search, category, minimumPrice, maximumPrice

def myCart(productName,productDescription,productCategory,price):
    print(f"Product name:{productName}\n")
    print(f"Product Description:{productDescription}\n")
    print(f"Product Category: {productCategory}\n")
    print(f"Product price:{price}\n")
def exitMenu():
    print("Thankyou for using Deals Poa Catalogue")

userchoice=1
while userchoice==1 or userchoice==2 or userchoice==3 :
    print("\t\t\tData Poa\n")
    print("\t\t1.Add New Product\n")
    print("\t\t2.Find Product\n")
    print("\t\t3.My Cart\n")
    print("\t\t4.Exit\n")
    userchoice=int(input("Select your choice\n"))
    if userchoice==1:
        productName, productDescription, productCategory, price=addProduct()
    elif userchoice==2:
        findProduct()
    elif userchoice==3:
        myCart(productName,productDescription,productCategory,price)
    else:
        exitMenu()