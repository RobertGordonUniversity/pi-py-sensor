from sense_hat import SenseHat
import time

# connects our Pi to the SenseHat
sense = SenseHat()

while True:
    # display the humidity
	humidity = sense.get_humidity()
	print("Humidity: %s"%humidity)
	# display the temperature
	temp = sense.get_temperature()
	print("Temperature: %sC"%temp)
	# display the air pressure
	pressure = sense.get_pressure()
	print("Air pressure: %s millibars"%pressure)
	# wait for a second before continuing
	time.sleep(1)
