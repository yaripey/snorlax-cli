# Version: 1.0

import addons._example
class Command(addons._example.Command):
	def function(self, user_input):
		for f in user_input:
			print(f, end=" ")
		print()
	name = "test"

