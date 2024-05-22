import pymongo
client = pymongo.MongoClient()

mydb = client["OnlineStore"]

def getUserInfo():
    print("\nEnter your first name:")
    fname = input()
    print("\nEnter your last name")
    lname = input()
    print("\nEnter your email:")
    email = input()
    print("\nEnter your phone number")
    phone = input()
    print("\nEnter your date of birth")
    dob = input()
    data = {'first name' :fname,'last name':lname, 'email':email,'phone': phone,'date of birth': dob}
    return data

def insertUser(data):
    mydb["Users"].insert_one(data)

def findByCategory(category):
    for x in mydb["Products"].find({'category': category}):
        print(x)
        print("\n")

def findByID(id):
    product = mydb["Products"].find_one({'id': id})
    return product

def viewCart():
    for x in mydb["Shopping Cart"].find():
        print(x)
        print("\n")

def addToCart(product):
    mydb["Shopping Cart"].insert_one(product)

def removeFromCart(id):
    mydb["Shopping Cart"].delete_one({'id':id})

def getOrderSummary():
    x = 0
    for product in mydb["Shopping Cart"].find():
        x = x + 1
    print("Total Number of Products: " + str(x))

def Menu():
    user = getUserInfo()
    insertUser(user)
    while True:
        print("\nWelcome to General Goods Online")
        print("What can we help you with today loyal customer?")
        print("\n1.Browse by Category\n2.Search by product id\n3.View cart\n4.Exit")
        choice = int(input())
        if choice == 1:
            print("\nEnter a Category")
            cat = input()
            findByCategory(cat)
        elif choice == 2:
            print("\nEnter a product id")
            id = int(input())
            product = findByID(id)
            print(product)
            print("\nWould you like to add this to your cart?")
            addChoice = input()
            if (addChoice == "yes"):
                addToCart(product)
                print("\nAdded to Cart")
            else:
                print("\nNo Problem")
        elif choice == 3:
            viewCart()
            print("\nWould you like to remove an item from your cart?")
            deleteChoice = input()
            if (deleteChoice == "yes"):
                print("\nEnter the id of the product you'd like to delete")
                id = int(input())
                removeFromCart(id)
                print("\nProduct Removed")
            else:
                print("\nNo problem")
        else:
            getOrderSummary()
            print("\nHave a nice day!")
            break

Menu()
