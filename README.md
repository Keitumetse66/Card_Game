# War Card Game

The "War" card game is a simple game played with a standard deck of 52 cards. The deck is shuffled and divided evenly between two players. In each round of the game, each player draws the top card from their deck and reveals it. The player with the higher card wins the round and takes both cards. If the two cards are of equal value, a "war" occurs, where each player puts the next three cards from their deck face down and then draws a fourth card, with the higher value card winning the war and taking all the cards on the table. The game continues until one player has all the cards in the deck.

# Files

card_game.py: This file contains the implementation of the War card game.
test_card_game.py: This file contains unit tests for the card game implementation.

# Dependencies
- Python 3

# How to Run the Game

To play the War card game, run the card_game.py file in a Python 3 environment. The game will automatically start and continue until one player has all the cards in the deck.

# How to Run the Unit Tests

To run the unit tests for the War card game implementation, run the test_card_game.py file in a Python 3 environment. The tests will automatically run and display the results in the terminal.

# Implementation Details

The card_game.py file contains the implementation of the War card game. It uses the random module to shuffle the deck of cards and the unittest module to run unit tests. The game is implemented using the following steps:

Initialize the deck of cards by creating a list of tuples, where each tuple represents a card and contains two strings: the value and the suit of the card.
Shuffle the deck of cards using the random.shuffle() function.
Split the deck of cards evenly between two players.
Repeat the following steps until one player has all the cards:
Each player draws the top card from their deck and reveals it.
If one card has a higher value than the other card, the player with the higher card takes both cards and adds them to the bottom of their deck.
If the two cards have the same value, a "war" occurs:
Each player puts the next three cards from their deck face down on the table.
Each player draws a fourth card and reveals it.
If one card has a higher value than the other card, the player with the higher card takes all the cards on the table and adds them to the bottom of their deck.
If the two cards have the same value, another war occurs.
If one player has all the cards, the game ends.
The test_card_game.py file contains unit tests for the War card game implementation. It tests the following:

- That the card values and suits are set up correctly.
- That the deck has the correct number of cards and each card is unique.
- That the game ends correctly when one player has all the cards.



