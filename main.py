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
    card_packs = card_packs_menu

    return card_packs


# This function generates and shuffles the card packs that the user asked for. Details below!
def generate_card_deck(card_packs):
    logging.debug("generate_card_deck running")
    counter: int = 0  # a counter variable for later
    card_holder = list()  # sets main card holder for the decks of cards
    card_pack = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]  # a default list for the adding loop

    #  This section adds a pack of cards for every pack the player wants e.g. if the player wants 2 packs, then it
    #  would repeat 2 times.
    while counter != card_packs:
        card_holder += card_pack
        counter += 1
        logging.info("Card pack added to holder successfully")
    else:
        logging.debug("Finished with generating cards")

    #  This section is for shuffling the cards using the random module imported, then returns the list for use below.
    random.shuffle(card_holder)
    logging.info("Cards shuffled successfully")
    return card_holder


# This function is used to generate the hands for the player and the dealer.
def generate_hands(card_holder):
    counter = 0
    player_hand = []
    dealer_hand = []
    while True:
        player_hand.append(card_holder[counter])
        card_holder.pop(0)
        dealer_hand.append(card_holder[counter])
        card_holder.pop(0)
        counter += 1
        logging.info("Added to player and dealer hand successfully")
        if counter == 2:
            logging.debug("Finished with generating hands")
            break
    return player_hand, dealer_hand

def play_game(player_hand, dealer_hand):
    print("Placeholder")  # To be continued here


if __name__ == "__main__":
    setup_debug_log()
    generate_hands(generate_card_deck(determine_card_packs()))
    # ------------------------------------------
    logging.info("End of code, program exiting")
    quit()
