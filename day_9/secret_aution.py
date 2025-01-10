from gavel_art import logo

def find_highest_bidder(bidding_dictionary):
    max_bid_amount = 0
    winner_name = ""
    for key in bids:
        bid_amount = bids[key]
        if bid_amount > max_bid_amount:
            max_bid_amount = bid_amount
            winner_name = key
    
    print(f"The winner is {winner_name} with a bid of ${max_bid_amount}")

print("Welcome to the secret aution program.")
print(logo)

continue_aution = True
bids = {}
while continue_aution:
    name = input("What is your name?\n")
    bid_amount = float(input("What's your bid?\n$"))
    bids[name] = bid_amount
    other_bidders = input("Are there any other biddres? Type 'yes' or 'no'.\n")
    if other_bidders == "yes":
        # to clear the screen
        print("\033c", end='')
    else:
        continue_aution = False
        find_highest_bidder(bids)