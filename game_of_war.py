import random
games_count = 0
player1_win_count = 0
opponent_win_count = 0
game_over = False


def get_card():
    return random.randint(0, 9)


# Welcome the player
print("=================================\n")
print("Python Game of War\n")
print("=================================\n")

# Determine if player wishes to play
wants_to_play = input("Type PLAY and press ENTER:")

if (wants_to_play != "PLAY"):
    print("Good bye")
else:
    # test if 20 rounds has been played
    while (games_count < 20):

        # Plays one round

        player1_card = get_card()
        opponent_card = get_card()
        print("\nYour card: "+str(player1_card) +
              "  Opponent's card: "+str(opponent_card) + "")

        if (player1_card > opponent_card):

            print("You won this round!")
            input("Press enter to continue")
            player1_win_count = player1_win_count+2
            games_count += 1

        elif (player1_card == opponent_card):

            print("\nWAR!")
            player1_card = get_card()
            opponent_card = get_card()

            if (player1_card > opponent_card):

                print("You won the war!")
                input("Press enter to continue")
                player1_win_count = player1_win_count+6
                games_count += 1
            else:
                print("Opponent won the war!")
                input("Press enter to continue")
                opponent_win_count = opponent_win_count+6
                games_count += 1

        else:

            print("Opponent won this round!")
            input("Press enter to continue")
            opponent_win_count = opponent_win_count+2
            games_count += 1

    # Display final score
    print("\nYour score:" + str(player1_win_count) +
          "   Opponeet's score:"+str(opponent_win_count))
    if (player1_win_count > opponent_win_count):
        print("You won!")
    else:
        print("You opponent won")
