# Version: 1.0

import addons._example
class Command(addons._example.Command):
	name = "test"
	def function(self, user_input):
		for f in user_input:
			print(f, end=" ")
		print()

