shoppingCart = {}

while True:
    print("WELCOME TO THE AMANDO SHOPPING SITE")
    print("1. Add product to the cart.")
    print("2. Search the product.")
    print("3. Delete the product from the cart.")
    print("4. Quit.")

    choice = input("Enter your choice: ").upper()
    if choice == "1":
        total=int(input("Enter the Number of items to be added int he stationary shop:"))
        while total>0:
            total-=1
            if len(shoppingCart) >= 5:
                print("Cart is full")
            else:
                itemName = input("Enter an item: ")
                itemBrand = input("Enter the brand name: ")
                shoppingCart[itemName] = itemBrand
                print("You added following items to the cart:",itemName,":",itemBrand)
    
    elif choice == "2":
        itemName = input("Enter the item: ")
        if itemName in shoppingCart:
            itemBrand = shoppingCart[itemName]
            print(itemName,":",itemBrand," found in the cart")
        else:
            print("No product exists with this name")
    elif choice =="3":
        itemName = input("Enter the item: ")
        if itemName in shoppingCart:
            shoppingCart.pop(itemName)
            print("Item Deleted")
        elif len(shoppingCart)==0:
            print("Cart is empty, no item is found")
    elif choice=='4':
        break
    else:
        print("Wrong Option Entered"