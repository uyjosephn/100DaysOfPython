num_char = len(input("What is your name? "))
print(type(num_char))

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")


height = float(input("Height: "));
weight = int(input("Weight: "));

bmi = weight / height ** 2

bmi_as_int = int(bmi)
print(bmi_as_int)

#f-String
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


age = int(input("What is your current age? "))
years_remaining = 90 - age
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {weeks_remaining} weeks, {years_remaining} years, and {months_remaining} months left.")

