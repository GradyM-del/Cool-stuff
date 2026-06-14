"""------BlackJack-----"""

from random import *
from time import sleep

print("-----BLackJAck-----")
print("Try to get close to 21 as much as you can")
print()

def main():

    suits = ["♣️", "♠️", "♥️", "♦️"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    deck = create_deck(suits, ranks)
    
    shuffle(deck)


    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0

    for i in range(2):
        player_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))
    
    player_score = tally_score(player_hand)
    dealer_score = tally_score(dealer_hand) 

    print("Your hand: ", end = '')
    for i in player_hand:
        print(i, end = "  ")
    print("Your score:", player_score)
   
    print("Dealer's hand: ", dealer_hand[0], " ##")

    #Player's turn
    while player_score < 21 :
        #Asking if player wants to hit or stay
        choice = input("Would you Hit or Stand reply with H or S: ").lower()
        if choice == "s":
            break
        #Draw card
        card = deal_card(deck)
        print("You drew", card)
        #Increase score and Special case if close to 21
        if card[0] == "A" and player_score + 10 > 21:
            player_score += 1
        else:
            player_score += compute_score(card)
        
        player_hand.append(card)
        
        print("Your hand:", player_hand)
        print("Your score", player_score)
        #Check score condition
    if player_score > 21:
        print("BUST!!! YOU LOSE")
        print("Better luck next time")
        return None
    print()

    #Dealer's turn
    print("Dealer's hand: ", dealer_hand)
    print("Dealer's score: ", dealer_score)
    sleep(3)
    while dealer_score < 17:
        #Draw a card for dealer
        card = deal_card(deck)
        print("You drew", card)
        #Increase score and Special case if close to 17 and draw an ace
        if card[0] == "A" and dealer_score + 10 > 17:
            dealer_score += 1
        else:
            dealer_score += compute_score(card)
        
        dealer_hand.append(card)
        
        print("Dealer'shand:", dealer_hand)
        print("Dealer's score", dealer_score)
        if dealer_score > 21:
            print("Dealer's bust You win!!!")
            return None
        sleep(5)
    
    print("------Final results-----")
    print("Your score:", player_score)
    print("Dealer's score:", dealer_score)
    if player_score > dealer_score:
        print("You win!!!")
    elif player_score < dealer_score:
        print("You lose, better luck next time")
    else: print("It's a draw try again to win")

    return None


    

def tally_score(hand):
    """Computes the total of a hand"""
    total = 0
    for i in hand:
        total+= compute_score(i)
    return total

def compute_score(card):
    """Compute the score based on what the card is"""
    if card[0] == "A":
        return 10
    elif card[0] in ["1", "J", "K", "Q"]:
        return 10
    else:
        return int(card[0])
            

def deal_card(deck):
    """Deals a card"""
    card = deck.pop(randrange(len(deck)))
    return card

def create_deck(suits, ranks):
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    return deck


if __name__ == "__main__":
    main()
