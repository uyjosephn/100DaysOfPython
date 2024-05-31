loop = True

bids = {}

while loop:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))

    bids[name] = bid

    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bids == "no":
        loop = False
        winner = max(bids, key=bids.get)
        print(f"The winner is {winner} with a bid of ${bids[winner]}")


