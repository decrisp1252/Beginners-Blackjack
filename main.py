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
    card_pack = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]  # a default list for the adding loop

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
def generate_hands(card_holder):
    counter = 0
    player_hand_f = []
    dealer_hand_f = []
    while True:
        player_hand_f.append(card_holder[counter])
        card_holder.pop(0)
        dealer_hand_f.append(card_holder[counter])
        card_holder.pop(0)
        counter += 1
        logging.info("Added to player and dealer hand successfully")
        if counter == 2:
            logging.debug("Finished with generating hands")
            break
    return player_hand_f, dealer_hand_f


# This function assigns the variables to each of the cards the player has. Using the match to stop endless 'elif'
# statements, it then adds this to a score tally which will be used to calculate the result in the back end. Aces also
# have a variable, meaning that it can be properly modelled in the program
def assign_values(players_input, dealers_input):
    player_score = 0
    player_ace_counter = 0
    dealer_score = 0
    dealer_ace_counter = 0

    if players_input != 0:
        counter = 0
        while True:
            match player_hand[counter]:
                case "2":
                    player_score += 2
                    logging.info("Added score 2 to card")
                    counter += 1
                case "3":
                    player_score += 3
                    logging.info("Added score 3 to card")
                    counter += 1
                case "4":
                    player_score += 4
                    logging.info("Added score 4 to card")
                    counter += 1
                case "5":
                    player_score += 5
                    logging.info("Added score 5 to card")
                    counter += 1
                case "6":
                    player_score += 6
                    logging.info("Added score 6 to card")
                    counter += 1
                case "7":
                    player_score += 7
                    logging.info("Added score 7 to card")
                    counter += 1
                case "8":
                    player_score += 8
                    logging.info("Added score 8 to card")
                    counter += 1
                case "9":
                    player_score += 9
                    logging.info("Added score 9 to card")
                    counter += 1
                case "10":
                    player_score += 10
                    logging.info("Added score 10 to card")
                    counter += 1
                case "J":
                    player_score += 10
                    logging.info("Added score J to card")
                    counter += 1
                case "Q":
                    player_score += 10
                    logging.info("Added score Q to card")
                    counter += 1
                case "K":
                    player_score += 10
                    logging.info("Added score K to card")
                    counter += 1
                case "A":
                    player_ace_counter += 1
                    player_score += 11
                    logging.info("Added score A to card")
                    counter += 1
            if counter == 3:
                break
    if dealers_input != 0:
        counter = 0
        while True:
            match dealer_hand[counter]:
                case "2":
                    dealer_score += 2
                    logging.info("Added score 2 to card")
                    counter += 1
                case "3":
                    dealer_score += 3
                    logging.info("Added score 3 to card")
                    counter += 1
                case "4":
                    dealer_score += 4
                    logging.info("Added score 4 to card")
                    counter += 1
                case "5":
                    dealer_score += 5
                    logging.info("Added score 5 to card")
                    counter += 1
                case "6":
                    dealer_score += 6
                    logging.info("Added score 6 to card")
                    counter += 1
                case "7":
                    dealer_score += 7
                    logging.info("Added score 7 to card")
                    counter += 1
                case "8":
                    dealer_score += 8
                    logging.info("Added score 8 to card")
                    counter += 1
                case "9":
                    dealer_score += 9
                    logging.info("Added score 9 to card")
                    counter += 1
                case "10":
                    dealer_score += 10
                    logging.info("Added score 10 to card")
                    counter += 1
                case "J":
                    dealer_score += 10
                    logging.info("Added score J to card")
                    counter += 1
                case "Q":
                    dealer_score += 10
                    logging.info("Added score Q to card")
                    counter += 1
                case "K":
                    dealer_score += 10
                    logging.info("Added score K to card")
                    counter += 1
                case "A":
                    dealer_ace_counter += 1
                    dealer_score += 11
                    logging.info("Added score A to card")
                    counter += 1
            if counter == 3:
                break

        return player_score, player_ace_counter, dealer_score, dealer_ace_counter


def play_game(players_value, dealers_value, players_ace_value, dealers_ace_value):
    print(f"Your hand is {player_hand[0]} and {player_hand[1]}. The dealer is showing a {dealer_hand[0]}")
    if player_hand[0] == player_hand[1]:
        menu1 = str(input("You can:\n1. Stand\n2. Hit\n3. Double\n4. Split\n>"))
    else:
        menu1 = str(input("You can:\n1. Stand\n2. Hit\n3. Double\n>"))
    menu1.lower()

    if menu1 == "stand":
        print("Placeholder")
    elif menu1 == "hit":
        print("Placeholder")


if __name__ == "__main__":
    setup_debug_log()
    card_packs = determine_card_packs()
    card_deck = generate_card_deck(card_packs)
    player_hand, dealer_hand = generate_hands(card_deck)
    players_value, dealers_value, players_ace_value, dealers_ace_value = assign_values(player_hand, dealer_hand)
    play_game(players_value, dealers_value, players_ace_value, dealers_ace_value)
    # ------------------------------------------
    logging.info("End of code, program exiting")
    quit()
