# weathercheck: 1.1
import requests, json
import addons._example
class Command(addons._example.Command):
	name = "weather"
	desc = "Allows you to check current weather in the chosen city."
	def function(self, user_input):
		if len(user_input) < 1:
			print("Usage: weatherinput [wanted city]")
		else:
			# Creating a request
			api_key = "41a74fd652e6e9dd9928565d822b400f"
			base_url = "http://api.openweathermap.org/data/2.5/weather?"
			city_name = user_input[0]
			complete_url = base_url + "appid=" + api_key + "&q=" + city_name

			# Using request to get a response
			response = requests.get(complete_url)
			x = response.json()
			# Checking if the city exists
			if x["cod"] != "404":
				y = x["main"]
				# Getting weather info
				current_temperature = int(y["temp"] - 273.15)
				current_pressure = y["pressure"]
				current_humidity = y["humidity"]
				z = x["weather"]
				weather_description = z[0]["description"]
				print(" Temperature (in celsius unit) = " +
					str(current_temperature) +
				"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
				"\n humidity (in percentage) = " +
					str(current_humidity) +
				"\n description = " +
					str(weather_description))
			else:
				print("City not found")

