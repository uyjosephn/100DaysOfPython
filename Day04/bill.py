import random

names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
print(random.choice(names) + " is going to buy the meal today!")

random_int = random.randint(0, len(names) - 1)
print(names[random_int] + " is going to buy the meal today!")


