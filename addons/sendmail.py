# Version: 0.1

from getpass import getpass
import smtplib
import addons._example
class Command(addons._example.Command):
	def function(self, user_input):
		smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
		smtpObj.ehlo()
		smtpObj.starttls()
		print("Введите вашу почту gmail:")
		mylogin = input()
		print("Введите ваш пароль:")
		mypass = getpass()
		if smtpObj.login(mylogin, mypass)[0] == 235:
			print("Ввелите тему письма:")
			subject = input()
			print("Введите сообщение, которое вы хотите отправить:")
			massage = input()
			choice = 0
			while choice != 1:
				print("Ваше сообщение:")
				print(massage)
				print()
				print("Вы довольны вашем сообщением? 1 - да, 0 - нет")
				choice = int(input())
			print("Введите почту получателя:")
			reciever = input()
			smtpObj.sendmail(mylogin, reciever, subject + "\n" + massage)
			smtpObj.quit()
		else:
			print("Неверный логин/пароль.")
		
	name = "sendmail"
	desc = "Позвляет отправлять почту с ящика Gmail."

