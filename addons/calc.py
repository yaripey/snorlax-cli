# Version: 1.1


import addons._example
class Command(addons._example.Command):
	name = "calc"
	desc = "Calculating simple mathemical expressions.\nYou can use +, -, /, * и %, and also ( )."
	def function(self, user_input):
		if len(user_input) > 1:
			print("Expression incorrect, please try again.")
		print(eval(str(user_input[0])))
	



