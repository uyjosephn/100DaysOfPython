line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print(f"{line1}\n{line2}\n{line3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizontal - 1] = "X"
print(f"{line1}\n{line2}\n{line3}")
