#!/usr/bin/python

cardDeck = []
suits = ['CLUB', 'DIAMOND', 'HEARTS', 'SPADES']

# initialise the card deck as a collection of dictionary items
for suit in suits:
	for i in range(1, 14):
		cardDeck.append({'suit': suit, 'value': i})

# Print the carddeck
for card in cardDeck:
	print(card)

# Get the size of the deck
print(len(cardDeck))

# Pick a random card from the deck
# Cards
cardDeck = list(range(52))
print(cardDeck)


def f(x):
	return x+1

for x in cardDeck:
	print(f(x))


