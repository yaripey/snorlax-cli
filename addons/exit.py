# Version: 1.1

import addons._example
class Command(addons._example.Command):
	name = "exit"
	def function(self, user_input):
		print("Good bye!")
		return 1
