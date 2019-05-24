# Magic8ball v0.1
import addons._example
import random, time

class Command(addons._example.Command):
	name = "magicball"
	desc = "The Magic 8 Ball"
	def function(self, user_input):
		messages = ["It is certain.",
			"It is decidedly so.",
			"Without a doubt.",
			"Yes - definitely.",
			"You may rely on it.",
			"As I see it, yes.",
			"Most likely.",
			"Outlook good.",
			"Yes.",
			"Signs point to yes.",
			"Reply hazy, try again.",
			"Ask again later.",
			"Better not tell you now.",
			"Cannot predict now.",
			"Concentrate and ask again.",
			"Don't count on it.",
			"My reply is no.",
			"My sources say no.",
			"Outlook not so good.",
			"Very doubtful.",]
		msg="The inscription on the magic ball reads: "
		for char in msg:
			print(char, end="", flush=True)
			time.sleep(0.05)
		time.sleep(1)
		msg=messages[random.randint(0, len(messages) - 1)]
		for char in msg:
			print(char, end="", flush=True)
			time.sleep(0.05)
		print("\n")
		