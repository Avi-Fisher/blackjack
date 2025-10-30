import random



def build_standard_deck() -> list[dict]:

    deck = []
    suite = ["H","C","D","S"]
    ranc = ["J","Q","K","A"]

    for i in range(2,11):
        for j in range(4):
            card = {"rank":str(i), "suite":suite[j]}
            deck.append(card)

    for i in range(4):
        for j in range(4):
            card = {"rank":ranc[i], "suite":suite[j]}
            deck.append(card)


    return deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:

    while swaps > 0:

        i = random.randint(0,51)
        j = random.randint(0,51)

        if i == j:
            continue

        card1 = deck[i]
        card2 = deck[j]

        if check_card(card1) or check_card(card2):
            continue

        deck[i],deck[j] = deck[j],deck[i]
        swaps -= 1

    return deck

def check_card(card):
    check = 0

    match card["suite"]:
        case "H":
            check = 5
        case "C":
            check = 3
        case "D":
            check = 2
        case "S":
            check = 7

    try:
        if int(card) % check != 0:
            return True
    except:
        if card["rank"] == "J" or card["rank"] == "Q" or card["rank"] == "K":
                if 10 % check != 0:
                    return True












