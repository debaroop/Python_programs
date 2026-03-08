#Discount decorator
def discount_decorator(func):
    def wrapper(base_price):
        price=func(base_price)
        discounted_price=price -(price*0.10)
        return discounted_price
    return wrapper

#Tax decorator
def tax_decorator(func):
    def wrapper(base_price):
        price=func(base_price)
        final_price=price + (price*0.18)
        return final_price
    return wrapper

#Base function
@tax_decorator
@discount_decorator
def calculate_flight_price(base_price):
    return base_price

base_price=float(input("Enter the base flight price:"))
final_price=calculate_flight_price(base_price)

print("Final ticket price", final_price)
        