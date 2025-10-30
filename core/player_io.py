def ask_player_action() -> str:
    while True:
        user_int = input("please press 'S' or 'H'")
        if user_int == "S" or user_int == "H":
            return user_int
        else:
            print("only 'S' or 'H'")






