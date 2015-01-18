import operator
from card import Card

class Player:

	NO_COMBO = (False, 0, 0) # isCombo, ValueOfCombo, HighCard

	def __init__(self, player_name):
		self.name = player_name
		self.wins = 0

	def get_cards(self, cards):
		self.hand = cards

	def show_cards(self):
		for c in self.hand:
			print(c, end=" ")
		print()
		
	def add_win(self):
		self.wins += 1

	def evaluate(self, middle):
		# empty control variables
		high_card = 0
		win_value = 20

		# generate all possible fives
		i = 6
		while i >= 0:
			j = i-1
			while j >= 0:
				tmp = middle + self.hand
				del tmp[i]
				del tmp[j]
				best_combo = self.find_best_combo(tmp)
				if (win_value > best_combo[0]):
					win_value = best_combo[0]
					high_card = best_combo[1]
				elif (win_value == best_combo[0]):
					if (high_card < best_combo[1]):
						high_card = best_combo[1]
				j -= 1
			i -= 1

		return (win_value, high_card)

	# finds best hand player has
	def find_best_combo(self, five):
		five.sort()

		kind = self.isNOfKind(five)
		win_value = kind[1]
		high_card = kind[2]

		flush = self.isFlush(five)
		straight = self.isStraight(five)

		if (flush[0] and straight[0]):
			royal = self.isRoyal(five)

			if (royal[0]):
				win_value = royal[1]
				high_card = royal[2]

			else:
				win_value = 2
				high_card = five[-1]

		elif (win_value > 6):
			if (flush[0]):
				win_value = flush[1]			
				high_card = flush[2]
			elif (straight[0]):
				win_value = straight[1]
				high_card = straight[2]
		return (win_value, high_card)

	def isRoyal(self, five):
		# after isStraightFlush evaluation

		if(five[-1].value == 14 and five[-2].value == 13):
			return (True, 1, 14)
		else:
			return (False, 0, 0)

	def isFlush(self, five):
		tmpColor = five[0].color
		for c in five:
			if (c.color != tmpColor):
				return self.NO_COMBO

		return (True, 5, five[4].value)

	def isStraight(self, five):
		tmpValue = five[0].value
		for c in range(1, 5):
			diff = five[c].value - tmpValue
			if (diff > 1 or diff == 0):
				return self.NO_COMBO

			tmpValue = five[c].value

		return (True, 6, five[4].value)

	def isNOfKind(self, five):
		tmp = {}

		for c in five:
			if (c.value in tmp):
				tmp[c.value] += 1
			else:
				tmp[c.value] = 1

		sorted_tmp = sorted(tmp.items(), key=operator.itemgetter(1))

		if (sorted_tmp[-1][1] == 4):
			return (True, 3, sorted_tmp[-1][0])
		elif (sorted_tmp[-1][1] == 3):
			if (sorted_tmp[-2][1] == 2):
				return (True, 4, sorted_tmp[-1][0])
			else:
				return (True, 7, sorted_tmp[-1][0])
		elif (sorted_tmp[-1][1] == 2):
			if (sorted_tmp[-2][1] == 2):
				t = sorted_tmp[-1][0] if sorted_tmp[-1][0]>sorted_tmp[-2][0] else sorted_tmp[-2][0]
				return (True, 8, t)
			else:
				return (True, 9, sorted_tmp[-1][0])
		else:
			return (True, 10, five[-1].value)