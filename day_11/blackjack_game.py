import random
import card_art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if 11 in cards:
        while sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

    return sum(cards)


def compare(player_score, computer_score):
    if (17 <= player_score <= 21) and (17 <= computer_score <= 21):
        if player_score == computer_score:
            return "That's a draw!"
        elif player_score == 21:
            return "You Win with a Black Jack!"
        elif computer_score == 21:
            return "Lose! Opponent has Black Jack!"
        elif player_score > computer_score:
            return "You Win"
        else:
            return "Opponent Win"
    elif player_score > 21:
        return "You went over. Opponent Win!"
    elif (17 <= player_score <= 21) and computer_score > 21:
        return "Opponent went over. You Win!"
    elif (17 <= player_score <= 21) and computer_score < 17:
        return "Opponent don't have enough score. You Win!"
    elif (17 <= computer_score <= 21) and player_score < 17:
        return "You don't have enough score. Opponent Win!"
    else:
        return "That's a draw."


def balck_jack_game():
    game = {"player": {"cards": [], "score": 0}, "computer": {"cards": [], "score": 0}}
    player_cards = game["player"]["cards"]
    player_score = game["player"]["score"]
    computer_cards = game["computer"]["cards"]
    computer_score = game["computer"]["score"]
    should_show_art = True

    choice = input(
        "Do you want to play a game of Blackjack with me? Type 'y' for yes or 'n' for no.\n"
    ).lower()

    while choice == "y":
        if should_show_art:
            print(card_art.art)

        for _ in range(2):
            player_cards.append(deal_card())
            computer_cards.append(deal_card())

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        player_turn_over = False

        while not player_turn_over:
            print(f"Your cards {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if (
                player_score == 21
                or computer_score == 21
                or player_score > 21
                or len(player_cards) >= 5
            ):
                player_turn_over = True
            else:
                deal_another_card = input(
                    "Type 'y' to get another card or 'n' to pass: "
                ).lower()

                if deal_another_card == "y":
                    player_cards.append(deal_card())
                    player_score = calculate_score(player_cards)
                else:
                    player_turn_over = True

        while computer_score != 21 and computer_score < 17 and len(computer_cards) < 5:
            # get another card for computer if total score is less than 17
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        result = compare(player_score, computer_score)

        print(
            f"Your final hand: {game["player"]["cards"]}, final score: {player_score}"
        )
        print(
            f"Computer's final hand: {game["computer"]["cards"]}, final score: {computer_score}"
        )

        print(result)

        choice = input(
            "Do you want to restart the game? Type 'y' for yes or 'n' for quit.\n"
        ).lower()
        
        if choice == "y":
            print("\033c", end="")
            should_show_art = False
            player_cards = []
            player_score = 0
            computer_cards = []
            computer_score = 0
        
    print("Good bye 👋")
    print("Thanks for playing with me 🙇")


balck_jack_game()
