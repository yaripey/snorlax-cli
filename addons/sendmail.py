# sendmail v0.4

from getpass import getpass
import smtplib, ssl
import addons._example
class Command(addons._example.Command):
	name = "sendmail"
	desc = "Allows you to send Gmail letters."
	def function(self, user_input):
		print("Enter your gmail:")
		mylogin = input()
		mypass = getpass('Enter you password:')
		print("Enter you email topic:")
		subject = input()
		print("Enter your message:")
		message = input()
		choice = 0
		while choice != "Y" and choice != "y":
			print("Your message:")
			print(message)
			print()
			print("Are you okay with your message? [Y/n]")
			choice = input()
		print("Enter reciever email:")
		reciever = input()

		context = ssl.create_default_context()
		try:
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.starttls(context=context)
			server.login(mylogin, mypass)
			fullmessage = "Subject: "+subject+"\n"+message
			server.sendmail(mylogin, reciever, fullmessage)
		except Exception as error:
			print(error)
		finally:
			server.quit()
