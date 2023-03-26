import random

# define card values
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# define card suits
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

# define deck of cards
deck = [(value, suit) for value in values for suit in suits]

# shuffle deck
random.shuffle(deck)

# divide deck between players
player1_hand = deck[:26]
player2_hand = deck[26:]

# play game
while len(player1_hand) > 0 and len(player2_hand) > 0:
    player1_card = player1_hand.pop(0)
    player2_card = player2_hand.pop(0)
    print("Player 1:", player1_card)
    print("Player 2:", player2_card)
    if values[player1_card[0]] > values[player2_card[0]]:
        print("Player 1 wins the round!")
        player1_hand.extend([player1_card, player2_card])
    elif values[player1_card[0]] < values[player2_card[0]]:
        print("Player 2 wins the round!")
        player2_hand.extend([player1_card, player2_card])
    else:
        print("War!")
        player1_war_cards = [player1_card]
        player2_war_cards = [player2_card]
        while True:
            for i in range(3):
                if len(player1_hand) == 0 or len(player2_hand) == 0:
                    break
                player1_war_cards.append(player1_hand.pop(0))
                player2_war_cards.append(player2_hand.pop(0))
            print("Player 1 cards:", player1_war_cards)
            print("Player 2 cards:", player2_war_cards)
            if len(player1_war_cards) < 4 or len(player2_war_cards) < 4:
                if sum([values[c[0]] for c in player1_war_cards]) > sum([values[c[0]] for c in player2_war_cards]):
                    print("Player 1 wins the war!")
                    player1_hand.extend(player1_war_cards + player2_war_cards)
                else:
                    print("Player 2 wins the war!")
                    player2_hand.extend(player1_war_cards + player2_war_cards)
                break
