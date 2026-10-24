def place_order(item):
   print(f"Place your order: your order is {item}")

def get_order():
    print("Preparing your order")
    return"Your order ready"

def calculate_total(item):
    base_price = 25.50
    VAT = 0.15
    totalPrice = (base_price + len(item)) * 1.15
    return totalPrice
    

myFood = input("What would you like?")
place_order(myFood)
                  
#msg = get_order()
print(get_order())

order_total = calculate_total(myFood)
print(f"Your order costs: R{round(order_total, 2)}")