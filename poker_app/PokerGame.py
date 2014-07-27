#!/usr/bin/python

import random

import pokerLogic

class CardDealer:
	
	def __init__(self):
		print('Initialising')
		self.cards = [x for x in range(52)] # Define instance variable

	def shuffle(self):
		print('Shuffling cards')
		random.shuffle(self.cards) # In Place shuffle, returns None

	# Deal cards, if the number of cards to deal is not specified just deal a single card
	def dealCards(self, numberOfCards=1):
		print('Dealing cards')
		dealtCards = []
		for i in (range(numberOfCards)):
			dealtCards.append(self.cards.pop())
		return dealtCards

# Running application
dealer = CardDealer()
dealer.shuffle()
hand = dealer.dealCards(7)
pokerLogic.evaluate(hand)
