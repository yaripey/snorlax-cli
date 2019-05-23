# sendmail v0.3

from getpass import getpass
import smtplib, ssl
import addons._example
class Command(addons._example.Command):
	name = "sendmail"
	desc = "Позвляет отправлять почту с ящика Gmail."
	def function(self, user_input):
		print("Введите вашу почту gmail:")
		mylogin = input()
		mypass = getpass('Введите ваш пароль:')
		print("Ввелите тему письма:")
		subject = input()
		print("Введите сообщение, которое вы хотите отправить:")
		massage = input()
		choice = 0
		while choice != "Y" and choice != "y":
			print("Ваше сообщение:")
			print(massage)
			print()
			print("Вы довольны вашем сообщением? [Y/n]")
			choice = input()
		print("Введите почту получателя:")
		reciever = input()

		context = ssl.create_default_context()
		try:
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.starttls(context=context)
			server.login(mylogin, mypass)
			fullmessage = "Subject: "+subject+"\n"+massage
			server.sendmail(mylogin, reciever, fullmessage)
		except Exception as error:
			print(error)
		finally:
			server.quit()
