# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

def getAmountMPriceaA():
    _amountM = int(input("Please enter your current money balance: "))
    _priceA = int(input("Please enter the price of an apple: "))
    return _amountM, _priceA

def show_the_result(amountMoney, priceApple):
    maximumApples = amountMoney // priceApple
    change = amountMoney % priceApple
    return maximumApples, change 

def display(maximumApples, change):
    print(f"You can buy {maximumApples} apples and your change is {change} pesos.")

# steps
# 1. ask how many money you enter and ask what is the price of an apple
amountMoney, priceApple = getAmountMPriceaA()
# 2. show the result
maximumApples, change = show_the_result(amountMoney, priceApple)
# 3. display
display(maximumApples, change)