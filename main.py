# Version 1.2

if __name__ == "__main__": # Главная функция

	# ------------------------
	# Gathering commands block
	# ------------------------

	# Импортируем глобальные переменные
	from globals import commands, User
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

	if isfile(join("snorlax-cli", "usersettings.py")):
		print("Usersettings found successfully.")
	else:
		print("I can't find the usersettings.py file, so it seems\nthat this is a first launch of the snorlax-cli. Let me gather some informaion about you, please.")
		print("What is your name?")
		nameanswer = input()
		print("What is your age?")
		ageanswer = input()
		f = open(join("snorlax-cli", "usersettings.py"), "a+")
		f.write(nameanswer)
		f.write("\n")
		f.write(ageanswer)
		f.write("\n")
		f.close()
		
	f = open(join("snorlax-cli", "usersettings.py"), "r")
	filelines = f.readlines()
	user = User(filelines[0], filelines[1])

	print("""
     ^ ^
 ("\\(-_-)/")
  ((     ))
((...) (...))""")

	print("===============")
	print("  Snorlax CLI")
	print("===============")
	print("Greetings, " + user.name)

	loop = True # Условие выхода из цикла
	while loop: # Старт главного цикла
		print("Чем могу помочь?")
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