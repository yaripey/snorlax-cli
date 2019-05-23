# Version: 1.0
# to-do list:
# Добавить возможность обрабатывать запросы с пробелами


import addons._example
class Command(addons._example.Command):
	name = "calc"
	desc = "Вычисление простых математических выражений.\nМожно использовать знаки +, -, /, * и %, а также скобки."
	def function(self, user_input):
		if len(user_input) > 1:
			print("Некорректный ввод, попробуйте ещё раз.")
		print(eval(str(user_input[0])))
	



