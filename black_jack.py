import black_module as black
import time
import random
# the below array represents the posibilities . when you shrink the range then the posibilities change
possibilities =[1,0,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1]

# capitalize your name
player = str.capitalize(input("Type your name : "))
game_finish = False
gameOver = False
stay = False
# game commands
print("'H' or 'h' to hit , 'S' or 's' to stand , 'E' or 'e'  to exit !\n")
# main game
while not game_finish:
    cards = []
    cards_played = []
    computers_cards = []
    # we create the total cards with the icon on the right
    for i in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
        for j in ["♤","♧","♡","♢"]:
            cards.append(i+j)
    # shuffle the card 2 times
    random.shuffle(cards)
    random.shuffle(cards)

    # black. is refered to external module
    computers_cards.append(black.rand_picker(cards))
    cards_played.append(black.rand_picker(cards))
    computers_cards.append(black.rand_picker(cards))
    cards_played.append(black.rand_picker(cards))
    # some delay
    time.sleep(1)
    print("\nComputer's cards : ",computers_cards[0] , "  *\n")
    time.sleep(1)
    black.card_print(cards_played)
    sum = black.sum_check(cards_played)

    # === Our turn to play
    # if we dont lose or if we want to stay
    while not gameOver and not stay:
        command = str.lower(input(f'\n\n{player}, would you hit or stand ? : '))

        if command == "s" or command =="S":
            stay = True
        elif command == "h" or command == "H":
            cards_played.append(black.rand_picker(cards))
            black.card_print(cards_played)
        elif command == "e" or command =="E":
            break
        else:
            print("You havent typed a valid command!")
        if black.sum_check(cards_played) > 21:
            gameOver = True

    if (black.sum_check(cards_played)) > 21:
        time.sleep(1)
        print("\n\nYou are Bust. Game Over")

    if not gameOver:
        print("\nComputer's Turn : \n")
        time.sleep(1)
        black.card_print(computers_cards)
    computersGameOver = False
    computerStay = False

    # ====  Computers turn
    while not computersGameOver and not computerStay and not gameOver:
        time.sleep(2)
        if black.sum_check(computers_cards) <= black.sum_check(cards_played) and black.sum_check(computers_cards) < 18:
            difference = 21 - black.sum_check(computers_cards)  # difference from 21 till our current total sum
            if difference > 6:  # if differnce is more than 6 then computer will take a card
                card = black.rand_picker(cards)
                computers_cards.append(card)
                print(" ",card, end=" ")
            elif difference <=6 and difference >=2:  # else if difference is 6 the it could stay or hit
                if random.choice(possibilities[0:difference*3]) == 1:
                    card = black.rand_picker(cards)
                    computers_cards.append(card)
                    print(" ", card, end=" ")
                else:
                    computerStay = True
            else:
                computerStay = True
        else:
            computerStay = True

    # determining the winner if the player was not busted from start
    if computerStay == True:
        time.sleep(1)
        print("\nComputer stands!")
    if black.sum_check(computers_cards) >21:
        computersGameOver = True
        time.sleep(0.3)
        print("\nComputer is Bust!You won!!")
    elif black.sum_check(computers_cards) <= 21 and black.sum_check(computers_cards) > black.sum_check(cards_played):
        time.sleep(1)
        print("\nComputer is the winner!")
        computersGameOver = True
    elif black.sum_check(cards_played) <= 21 and black.sum_check(cards_played) > black.sum_check(computers_cards):
        time.sleep(1)
        print("\nYou won!")
        computersGameOver = True
    elif black.sum_check(cards_played) == black.sum_check(computers_cards):
        time.sleep(1)
        print("\nIts a Push. Nobody wins!")
        computersGameOver = True

    command = str.lower(input(f'\n{player}, would you like to play again? '))
    if command == "y":
        gameOver = False
        computersGameOver = False
        computerStay = False
        stay = False
    elif command == "n":
        game_finish = True