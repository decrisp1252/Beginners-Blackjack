import logging
import random


#  This function is used to set up my logging system where I can debug the program without having to go through piles
#  of print statements! The results can be found in logFile.log that will create once the program starts. It will
#  over-write the file every time you run it however.
def setup_debug_log():
    # creates log format and generates a quick message
    logging.basicConfig(filename="logFile.log", filemode="w",
                        format="%(asctime)s %(name)s %(levelname)s %(message)s", level=logging.DEBUG)
    logging.info("Ran setup_debug_log. I did my job!")


#  This function determines how many packs the user wants in their game. It throws a value error and quits the program
#  if the user tries to enter anything else rather then an integer.
# noinspection PyUnboundLocalVariable
def determine_card_packs():
    try:
        card_packs_menu: int = int(input("How many card decks would you like?\n> "))
    except ValueError:  # this throws an error if the user enters a string, boolean etc.
        logging.critical("VALUE_ERROR - User entered an incompatible number of decks. Shutting down.")
        print("Please enter a number! Shutting down program.")
        quit()
        # my IDE says that this is referenced before assignment. It's not, but it is used in a try loop and therefore
        # not on the same indentation, which may be why it is throwing me a warning
    card_packs_f = card_packs_menu

    return card_packs_f


# This function generates and shuffles the card packs that the user asked for. Details below!
def generate_card_deck(card_packs_f):
    logging.debug("generate_card_deck running")
    counter: int = 0  # a counter variable for later
    card_holder = list()  # sets main card holder for the decks of cards
    card_pack = [["A", 11], ["2", 2], ["3", 3], ["4", 4], ["5", 5], ["6", 6], ["7", 7], ["8", 8], ["9", 9], ["10", 10],
                 ["J", 10], ["Q", 10], ["K", 10]]  # a default list for the adding loop

    #  This section adds a pack of cards for every pack the player wants e.g. if the player wants 2 packs, then it
    #  would repeat 2 times.
    while counter != card_packs_f:
        card_holder += card_pack
        counter += 1
        logging.info("Card pack added to holder successfully")
    else:
        logging.debug("Finished with generating cards")

    #  This section is for shuffling the cards using the random module imported, then returns the list for use below.
    random.shuffle(card_holder)
    logging.info("Cards shuffled successfully")
    return card_holder


# This function is used to generate the hands for the player and the dealer. It works by first taking the first card
# the deck generated earlier and then adding it to the player's hand (which is also a list.) It then removes that card
# from the list. The function then repeats the same for the dealer and adds to the counter, which is used to cancel the
# loop. It then returns the hands.

def generate_hands(card_holder, game_started):
    counter = 0
    if not game_started:
        player_score_f = 0
        dealer_score_f = 0
        player_ace_counter_f = 0
        dealer_ace_counter_f = 0
        player_hand_f = []
        dealer_hand_f = []
    else:
        player_score_f = player_score
        dealer_score_f = dealer_score
        player_ace_counter_f = player_ace_counter
        dealer_ace_counter_f = dealer_ace_counter
        player_hand_f = player_hand
        dealer_hand_f = dealer_hand
    while True:
        player_hand_f.append(card_holder[counter])
        card_holder.pop(0)
        player_score_f += player_hand_f[counter][1]
        if player_hand_f[counter][0] == "A":
            player_ace_counter_f += 1

        dealer_hand_f.append(card_holder[counter])
        card_holder.pop(0)
        dealer_score_f += dealer_hand_f[counter][1]
        if dealer_hand_f[counter][0] == "A":
            dealer_ace_counter_f += 1
        counter += 1
        logging.info("Added to player and dealer hand successfully")
        if not game_started:
            if counter == 2:
                logging.debug("Finished with generating hands")
                break
        else:
            if counter == 1:
                logging.debug("Generated another card")
                break

    return player_hand_f, player_score_f, dealer_hand_f, dealer_score_f, player_ace_counter_f, dealer_ace_counter_f


# This function assigns the variables to each of the cards the player has. Using the match to stop endless 'elif'
# statements, it then adds this to a score tally which will be used to calculate the result in the back end. Aces also
# have a variable, meaning that it can be properly modelled in the program

def play_game(player_hand_f, dealer_hand_f, player_ace_value, dealers_ace_value):
    print(f"Your hand is {player_hand[0][0]} and {player_hand[1][0]}. The dealer is showing a {dealer_hand[0][0]}")
    if player_hand_f == 21:
        print("Blackjack!")

    if player_hand[0] == player_hand[1]:
        menu1 = str(input("You can:\n1. Stand\n2. Hit\n3. Double\n4. Split\n>"))
    else:
        menu1 = str(input("You can:\n1. Stand\n2. Hit\n3. Double\n>"))
    menu1.lower()

    generate_hands(card_deck, game_started=True)
    print(player_hand[0][0], player_hand[1][0], player_ace_value)


if __name__ == "__main__":
    setup_debug_log()
    card_packs = determine_card_packs()
    card_deck = generate_card_deck(card_packs)
    game_started = False
    player_hand, player_score, dealer_hand, dealer_score, player_ace_counter, dealer_ace_counter = generate_hands(
        card_deck, game_started=False)
    play_game(player_hand, dealer_hand, player_ace_counter, dealer_ace_counter)
    # ------------------------------------------
    logging.info("End of code, program exiting")
    quit()
