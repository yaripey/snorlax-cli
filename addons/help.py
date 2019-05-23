# Version: 1.2

import addons._example
from globals import commands
class Command(addons._example.Command):
	name = "help"
	desc = "help shows you all available commands"
	def function(self, user_input):
		if user_input != []:
			print(commands[user_input[0]].desc)
		else:	
			for f in commands:
				print(f)
				print("-------")
				print(commands[f].desc)
				print()
