size = input("What size pizza do you want? S, M, or L ")

pizza_price = 0
if(size == "S"):
    pizza_price = 15
elif(size == "M"):
    pizza_price = 20
else:
    pizza_price = 25

add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if(add_pepperoni == "Y"):
    pizza_price += 2

if(extra_cheese == "Y"):
    pizza_price += 1

print(f"Your final bill is: ${pizza_price}")