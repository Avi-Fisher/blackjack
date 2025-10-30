def calculate_hand_value(hand: list[dict]) -> int:

    card = hand[0]["rank"]
    value = 0

    try:
        value = int(card)
    except:
        if card == "A":
            value = 1
        else:
            value = 10

    return value

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:

    for i in range(2):
        value = calculate_hand_value(deck)
        card = deck.pop(0)
        player.append(card)

    for i in range(2):
        value = calculate_hand_value(deck)
        card = deck.pop(0)
        dealer.append(card)








# def dealer_play(deck: list[dict], dealer: dict) -> bool:
#
# def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
