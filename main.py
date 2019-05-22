if __name__ == "__main__": # Главная функция

	# Импортируем глобальные переменные
	from globals import commands
	# Импортируем модули для работы с файлами:
	from os import listdir
	from os.path import isfile, join, dirname, abspath
	print(dirname(abspath(__file__))+"\\addons")

	# Составляем список файлов в папке addons/
	onlyfiles = [f for f in listdir(dirname(abspath(__file__))+"\\addons")]

	# Блок сбора словаря
	for module in onlyfiles:
		if module[-3:] != ".py":
			# Если файл не заканчивается на .py - пропускаем его
			continue
		if module.startswith("_"):
			# Если файл начинается с _ - пропускаем его
			continue
		
		# module_name = module.split(".")
		exec("import addons." + module[:-3])
		exec("obj = addons." + module[:-3] + ".Command()")
		commands[obj.name] = obj
	print(commands)

	# Блок тестирования

	print("""
     ^ ^
 ("\\(-_-)/")
  ((     ))
((...) (...))""")

	print("===============")
	print("  Snorlax CLI")
	print("===============")
	print("Здравствуй, путник! Как я могу тебе помочь?")

	loop = True # Условие выхода из цикла
	while loop: # Старт главного цикла
		
		# Ответ пользователя
		ask = str(input())
		# Разбиваем его на список
		ask_list = ask.split()
		# Первый элемент и есть наша команда
		ask_command = str(ask_list[0])
		# Если такой команды нет в списке, извиняемся
		if ask_command not in commands:
			print(" К сожалению, я не знаю такой команды")
		else:
			# Удаляем первый элемент из строки-запроса
			ask_list.pop(0)
			# Выполняем функцию
			if commands[ask_command].function(ask_list) == 1:
				loop = False
