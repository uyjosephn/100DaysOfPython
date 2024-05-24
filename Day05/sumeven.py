target = int(input("Enter a number: "))

even_sum = 0
for n in range(2, target + 1, 2):
    even_sum += n

print(even_sum)