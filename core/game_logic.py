from core.player_io import ask_player_action


def calculate_hand_value(hand: list[dict]) -> int:
    value = 0

    for i in hand["hand"]:
        try:
            value += int(i["rank"])
        except:
            if i["rank"] == "A":
                value += 1
            else:
                value += 10

    return value

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:

    for i in range(2):
        player["hand"].append(deck.pop(0))
    print(f"your value is {calculate_hand_value(player)}")

    for i in range(2):
        dealer["hand"].append(deck.pop(0))
    print(f"dealer value is {calculate_hand_value(dealer)}")

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    value = calculate_hand_value(dealer)

    while value < 17:
        dealer["hand"].append(deck.pop(0))
        value = calculate_hand_value(dealer)
        print(f"value dealer is {value}")

    if value > 21:
        return False
    elif value <= 21 and value >= 17:
        return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    value_plyer = calculate_hand_value(player)

    while True:
        user_play = ask_player_action()

        if user_play == "H":
            player["hand"].append(deck.pop(0))
            value_plyer = calculate_hand_value(player)
            print(f"your vlaue is {value_plyer}")

            if value_plyer > 21:
                print("you lose!")
                exit("goodbye")

        elif user_play == "S":
            dealer_value = calculate_hand_value(dealer)

            if dealer_value > value_plyer:
                print("you lose")
                exit("goodbye!")

            if not dealer_play(deck,dealer):
                dealer_value = calculate_hand_value(dealer)
                print("you winnn ! ! ! !")
                exit("goodbye")
            else:
                dealer_value = calculate_hand_value(dealer)


            if dealer_value < value_plyer:
                print("you winnn !!!!!")
                exit("goodbye")

            elif dealer_value > value_plyer:
                print("you loseeeee")
                exit("delear take all your muney")

            elif value_plyer == dealer_value:
                print("tako no one win")
                exit("goodbye")


