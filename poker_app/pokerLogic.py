# Evlauate the best hand from the cards dealt
def  evaluate(hand):
	if len(hand) < 5:
		# TODO: Throw an exception
		print('Atleast 5 cards must be in the hand')
	straight = getStraightFlush(hand)
	if (not straight) :
		print('Straight Flush')
		return straight

# Return the best straight flush from the hand
def getStraightFlush(hand):
	straight = getStraight(hand)
	return None

# Return the best flush from the hand
def getFlush(hand):
	return None

# Return the cards that make the best straight from the hand
def getStraight(hand):
	hand = sorted(set([x%13 for x in hand])) # Get the value of each card, then remove duplicates, then sort
	if hand[0]==0: # We have an ace so append to the end of the list for ace high straight
		hand.append(13)
	print(hand)
	if len(hand) < 5:
		print('Not enough unique vaule cards for a straight')
		return None
	i=0
	straight=None
	while (i+4) < len(hand):
		testHand=hand[i:i+5]
		if((testHand[4]-testHand[0])==4):
			print('Straight found: ', testHand)
			straight=testHand
		i+=1
	return straight
 
# Return the best four of a kind cards from the hand 
def getPoker(hand):
	return None

# Return the best full house from the hand
def getFullHouse(hand):
	return None

# Return the best 3 of a kind hand from the hand
def get3OfAKind(hand):
	return None

# Return the best 2pair from the hand
def get2Pair(hand):
	return None

# Return the best pair from the hand
def getPair(hand):
	return None

# Return the high card from the hand
def getHighCard(hand):
	return None

