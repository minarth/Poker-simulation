from deck import Deck
from player import Player
from middle import Middle

class Game:
	'''
	Class for playing the m times game with n players
	'''
	def __init__(self, count_of_players):
		self.deck = Deck()
		self.middle = Middle()
		self.count_of_players = count_of_players
		self.win_combinations = {}
		for i in range(1,11):
			self.win_combinations[i] = 0
		self.players = []
		for i in range(0, self.count_of_players):
			self.players.append(Player('Lama ' + str(i)))

	# playing one game
	def turn(self):

		# shuffle
		self.deck.shuffle_deck()
		best_hand = 20
		high_card = 0
		win_player = 0

		# deal
		self.middle.set_cards(self.deck.get_cards_middle())
		# self.middle.show_cards()
		for i in range(0, self.count_of_players):
			self.players[i].get_cards(self.deck.get_cards_player())
		
		# evaluate
		for i in range(0, self.count_of_players):
			e = self.players[i].evaluate(self.middle.get_cards())
			
			if (e[0] < best_hand):
				best_hand = e[0]
				high_card = e[1]
				win_player = i
			elif (e[0] == best_hand):
				if (e[1] > high_card):
					high_card = e[1]
					win_player = i

			# self.players[i].show_cards()
			# print(self.players[i].name + ' ' + str(e))
		# print('----------------')
		# print('Best hand: ' + str(best_hand) + ' ' + str(high_card))
		# print('Player: ' + str(win_player))
		self.win_combinations[best_hand] += 1
		self.players[win_player].add_win()

	def game(self, count_of_turns):
		for i in range(0, count_of_turns):
			self.turn()
			if (i % 400 == 0):
				print(i)
		self.results()

	def results(self):
		print(self.win_combinations)
		for i in range(0, self.count_of_players):
			print(self.players[i].wins)