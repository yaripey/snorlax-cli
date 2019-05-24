# Heads or tails v0.1
import addons._example
import random

class Command(addons._example.Command):
	name = "coin"
	desc = "Flip coin"
	def function(self, user_input):
		# if len(user_input) == 0:
		if random.randint(0, 1) == 1:
			print('Heads!')
		else:
			print('Tails!')
		# else:
		# 	heads = 0
		# 	for i in range(user_input):
		# 		if random.randint(0, 1) == 1:
		# 			heads = heads + 1
		# 	print('Heads came up ' + str(heads) + ' times.')

				

