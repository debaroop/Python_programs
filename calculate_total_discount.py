discount=10
def display_product(Id, prodName, price):
    global discount
    print("Product ID:",Id)
    print("Product Name:",prodName)
    print("Price:", price-(price*discount/100))
    
def calculate_price(qty, price):
        global discount
        total=price*qty
        discounted_total=total -(total*discount/100)
        print("Discounted total:", discounted_total)

display_product(123,"abc",5000)
calculate_price(2,5000)

