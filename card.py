class Card:
	'''Class for card, keeping their values
			Color - 0 Hearts 1 Diamonds 2 Spades 3 Clubs
			Value - 2 - 10 (cards), 11 J 12 Q 13 K 14 A
	'''

	def __init__(self, color, value):
		self.color = color
		self.value = value

	def get_card(self):
		return [color, value]

	def __str__(self):
		if (self.color == 0):
			c = 'S'
		elif (self.color == 1):
			c = 'K'
		elif (self.color == 2):
			c = 'L'
		else:
			c = 'P'

		if (self.value >= 2 and self.value <= 10):
			v = str(self.value)
		elif (self.value == 11):
			v = 'J'
		elif (self.value == 12):
			v = 'Q'
		elif (self.value == 13):
			v = 'K'
		else:
			v = 'A'

		return(c + v)

	def __eq__(self, other):
		return (self.value == other.value)

	def __lt__(self, other):
		return (self.value < other.value)

	def __gt__(self, other):
		return (self.value > other.value)

	def __ne__(self, other):
		return (self.value != other.value)