# Version: 1.0

import addons._example
class Command(addons._example.Command):
	name = "exit"
	def function(self, user_input):
		print("Выход из программы")
		return 1
