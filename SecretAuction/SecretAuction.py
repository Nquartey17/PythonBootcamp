import sys

import art
print(art.logo)

auctioneers = {}
end_bidding = False

while not end_bidding:
    name = input("Enter your name: ")
    bid = int(input("Enter your price: "))

    auctioneers[name] = bid

    keep_bidding = input("Add another bidder? Enter yes or no ").lower()

    if keep_bidding == "no":
        end_bidding = True

    print("\n" * 100)

highest_bidder = ""
highest_bid = -sys.maxsize -1

for name in auctioneers:
    if auctioneers[name] > highest_bid:
        highest_bid = auctioneers[name]
        highest_bidder = name

print(highest_bidder + " is the higgest bidder")
