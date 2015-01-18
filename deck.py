from card import Card
from random import shuffle
import copy

class Deck:
	'''
		Handling the deck of card - suffling, dealing.
	'''
	def __init__(self):
		self.list_of_cards = list()
		# fill the deck
		for color in range(0, 4):
			for value in range(2, 15):
				self.list_of_cards.append(Card(color, value))
				
	def shuffle_deck(self):
		shuffle(self.list_of_cards)
		self.deck_to_deal = copy.deepcopy(self.list_of_cards)
		# print(len(self.list_of_cards))

	def write_deck(self):
		for c in self.list_of_cards:
			print(c, end=" ")
		print()

	def sort_deck(self):
		self.list_of_cards.sort()

	def get_cards_middle(self):
		return self.get_cards(5)
	
	def get_cards_player(self):
		return self.get_cards(2)

	def get_cards(self, count):
		tmp = []
		for i in range(0, count):
			tmp.append(self.deck_to_deal.pop())
		return tmp
