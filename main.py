# Version 1.2

if __name__ == "__main__": # Главная функция

	# ------------------------
	# Gathering commands block
	# ------------------------

	# Импортируем глобальные переменные
	from globals import commands, User, path
	# Импортируем модули для работы с файлами:
	from pathlib import Path

	#Получаем текущую директорию
	path = Path().absolute()

	# Составляем список файлов в папке addons
	onlyfiles = [f.name for f in Path(path/"addons").glob('[a-z, A-Z, 0-9]*.py')]
	print(onlyfiles)
	
	# Блок сбора словаря
	for module in onlyfiles:
		exec("import addons." + module[:-3])
		exec("obj = addons." + module[:-3] + ".Command()")
		commands[obj.name] = obj
	# print(commands)

	if Path.exists(path/"usersettings"):
			print("Usersettings found successfully.")
	else:
		print("I can't find the usersettings file, so it seems\nthat this is a first launch of the snorlax-cli. Let me gather some informaion about you, please.")
		print("What is your name?")
		nameanswer = input()
		print("What is your age?")
		ageanswer = input()
		f = open(path/"usersettings", "a+")
		f.write(nameanswer)
		f.write("\n")
		f.write(ageanswer)
		f.write("\n")
		f.close()
		
	f = open(path/"usersettings", "r")
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