class Middle:
	'''
	middle - public cards
	'''
	def set_cards(self, cards):
		self.cards = cards

	def get_cards(self):
		return self.cards

	def show_cards(self):
		for c in self.cards:
			print(c, end=" ")
		print()