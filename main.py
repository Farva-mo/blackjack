import random
import art

#case to handle when a user has an ace, in blackjack ace represents either 1 or 11
# whichever one benefits the player the most and returns that favorable hand
def compareTo(hand):

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return hand

# function that makes the dealer draw, hard stop between 16-21
# compares between player total and returns results
def dealerTurn(player,dealer):

    playerTotal = sum(player)
    dealerDrawing = True

    while dealerDrawing:
        dealer = compareTo(dealer)

        dealerTotal = sum(dealer)

        if dealerTotal > 21:
            print(f"your hand: {player} {playerTotal}")
            print(f"dealers hand is {dealer} {dealerTotal}")
            return 'WON'

        elif dealerTotal == 21:
            print(f"your hand: {player} {playerTotal}")
            print(f"dealers hand is {dealer} {dealerTotal}")
            return 'LOST'

        elif dealerTotal > playerTotal:
            print(f"your hand: {player} {playerTotal}")
            print(f"dealers hand is {dealer} {dealerTotal}")
            return 'LOST'

        # dealer stops drawing cards at 17 and evaluates between one of three scenarios
        elif dealerTotal >= 17 and dealerTotal <= 21:
            if dealerTotal == playerTotal:
                print(f"your hand: {player} {playerTotal}")
                print(f"dealers hand is {dealer} {dealerTotal}")
                return 'TIED'

            elif dealerTotal > playerTotal:
                print(f"your hand: {player} {playerTotal}")
                print(f"dealers hand is {dealer} {dealerTotal}")
                return 'LOST'

            elif dealerTotal < playerTotal:
                print(f"your hand: {player} {playerTotal}")
                print(f"dealers hand is {dealer} {dealerTotal}")
                return 'WON'

        # dealer keeps drawing
        else:
            dealer.append(random.choice(cards))
            print(f"your hand: {player} {playerTotal}")
            print(f"dealers new hand is {dealer} {dealerTotal}\n")

def playerDraws(player,playerTotal):
    #player will be drawing
    player.append(random.choice(cards))
    player = compareTo(player)

    return sum(player)


cards = [11,2,3,4,5,6,7,8,9,10,10,10]

play = input("do you want to play blackjack 'y' or 'n'? ").lower()

logo = art.logo

while play == 'y':

    print(logo)
    #hand out the cards
    dealer=[random.choice(cards),random.choice(cards)]
    player=[random.choice(cards),random.choice(cards)]

    player = compareTo(player)
    playerTotal = sum(player)

    dealerTotal = sum(dealer)

    if playerTotal == 21:

        print(f"your hand: {player} {playerTotal}")
        print(f"dealer hand: {dealer[0]}")
        play = input("you win!, do you want to play again? 'y' or 'n' ").lower()

    else:
        print(f"your current hand: {player} {playerTotal}")
        print(f"dealer hand: {dealer[0]}")
        draw_again = input("do you want to draw another hand? 'y' or 'n' ")

        while draw_again == 'y':

            playerTotal = playerDraws(player,playerTotal)
            if playerTotal > 21:
                draw_again = 'n'
                game_result = 'BUSTED'
                print(f"your hand: {player} {playerTotal}")
                print(f"dealers hand is {dealer[0]}")
            else:
                print(f"your hand: {player} {playerTotal}")
                print(f"dealers hand is {dealer[0]}")
                draw_again = input("do you want to draw another hand? 'y' or 'n' ")

        # if player hasn't busted, its now the dealers turn
        if playerTotal <= 21:
            game_result = dealerTurn(player, dealer)

        # print the game results, and ask the player if they want to play again
        print(f"you {game_result}!\n")
        play = input("Do you want to play again? 'y' or 'n' ").lower()
        if play == 'y':
            print("\n"*20)