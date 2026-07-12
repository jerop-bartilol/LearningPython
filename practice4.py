def addProduct():
    productName = input("Enter the product name: ")
    productDescription = input("Enter the product description: ")
    productCategory = input("Enter the product category: ")
    price = float(input("Enter the price: "))

    return productName, productDescription, productCategory, price


def findProduct():
    search = input("Enter the product name to search: ")
    category = input("Enter the product category: ")
    minimumPrice = float(input("Enter the minimum price: "))
    maximumPrice = float(input("Enter the maximum price: "))

    return search, category, minimumPrice, maximumPrice


def myCart(productName, productDescription, productCategory, price):
    print("\n******** MY CART ********")
    print(f"Product Name:\t\t{productName}")
    print(f"Description:\t\t{productDescription}")
    print(f"Category:\t\t{productCategory}")
    print(f"Price:\t\t\t{price}")


def exitMenu():
    print("Thank you for using Deals Poa Catalogue.")