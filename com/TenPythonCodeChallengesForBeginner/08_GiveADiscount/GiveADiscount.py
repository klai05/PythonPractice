'''

Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.

The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

'''

def calculate_discount(price:int, discount_rate:int) -> float:
    discount = 100 - discount_rate
    final_price = price * discount / 100
    return final_price


if __name__ == "__main__":
    discounted_price = calculate_discount(150, 20)
    print(discounted_price)
