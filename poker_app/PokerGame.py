#!/usr/bin/python

import random

class CardDealer:
	
	def __init__(self):
		print('Initialising')
		self.cards = [x for x in range(1, 53)] # Define instance variable

	def shuffle(self):
		print('Shuffling cards')
		random.shuffle(self.cards) # In Place shuffle, returns None

	# Deal cards, if the number of cards to deal is not specified just deal a singel card
	def dealCards(self, numberOfCards=1):
		print('Dealing cards')
		dealtCards = []
		for i in (range(numberOfCards)):
			dealtCards.append(self.cards.pop())
		return dealtCards

