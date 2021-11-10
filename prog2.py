# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def show_Price():
    _aPrice = 20
    _oPrice = 25
    print(f"The price of an apple is {_aPrice} pesos.")
    print(f"The price of an orange is {_oPrice} pesos.")
    return _aPrice, _oPrice

def get_the_Quantities():
    aQuantity = int(input("How many apples will you buy? "))
    oQuantity = int(input("How many oranges will you buy? "))
    return aQuantity, oQuantity

def total_price(_aPrice, _oPrice, aQuantity, oQuantity):
    totalPriceA = _aPrice * aQuantity
    totalPriceO = _oPrice * oQuantity
    total_price = totalPriceA + totalPriceO
    return total_price

def display(totalP):
    print(f"The total amount is {totalP} pesos.")

# steps
# 1. show the price of an apple and an orange
aPrice, oPrice = show_Price()
# 2. ask how many apples and oranges will they buy
amountA, amountO = get_the_Quantities()
# 3. solve for the total price
totalP = total_price(aPrice, oPrice, amountA, amountO)
# 4. display the total price
display(totalP)