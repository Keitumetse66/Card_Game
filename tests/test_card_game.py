import unittest
from card_game import values, suits, deck

class TestWarGame(unittest.TestCase):
    
    def test_values(self):
        # check that card values are correct
        self.assertEqual(values['2'], 2)
        self.assertEqual(values['10'], 10)
        self.assertEqual(values['J'], 11)
        self.assertEqual(values['Q'], 12)
        self.assertEqual(values['K'], 13)
        self.assertEqual(values['A'], 14)
    
    def test_suits(self):
        # check that card suits are correct
        self.assertEqual(suits[0], 'Hearts')
        self.assertEqual(suits[1], 'Diamonds')
        self.assertEqual(suits[2], 'Spades')
        self.assertEqual(suits[3], 'Clubs')
    
    def test_deck(self):
        # check that deck has the correct number of cards
        self.assertEqual(len(deck), 52)
        # check that each card is unique
        self.assertEqual(len(set(deck)), 52)
    
    def test_war_game(self):
        # simulate a game and check that it ends correctly
        from card_game import player1_hand, player2_hand
        while len(player1_hand) > 0 and len(player2_hand) > 0:
            player1_card = player1_hand[0]
            player2_card = player2_hand[0]
            if values[player1_card[0]] > values[player2_card[0]]:
                player1_hand.extend([player1_card, player2_card])
                player1_hand.pop(0)
                player2_hand.pop(0)
            elif values[player1_card[0]] < values[player2_card[0]]:
                player2_hand.extend([player1_card, player2_card])
                player1_hand.pop(0)
                player2_hand.pop(0)
            else:
                player1_war_cards = [player1_card]
                player2_war_cards = [player2_card]
                while True:
                    for i in range(3):
                        if len(player1_hand) == 0 or len(player2_hand) == 0:
                            break
                        player1_war_cards.append(player1_hand.pop(0))
                        player2_war_cards.append(player2_hand.pop(0))
                    if len(player1_war_cards) < 4 or len(player2_war_cards) < 4:
                        if sum([values[c[0]] for c in player1_war_cards]) > sum([values[c[0]] for c in player2_war_cards]):
                            player1_hand.extend(player1_war_cards + player2_war_cards)
                            for i in range(len(player1_war_cards) + len(player2_war_cards)):
                                player1_hand.pop(0)
                        else:
                            player2_hand.extend(player1_war_cards + player2_war_cards)
                            for i in range(len(player1_war_cards) + len(player2_war_cards)):
                                player2_hand.pop(0)
                        break
        self.assertTrue(len(player1_hand) == 0 or len(player2_hand) == 0)

if __name__ == '__main__':
    unittest.main()
