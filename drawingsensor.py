from sense_har import SenseHat

# connects our Pi to the SenseHat
sense = SenseHat()

# define two colours
r = [255, 0, 0]
y = [255, 255, 0]

humidity = sense.get_humidity()
sense.show_message("Humidity: %s"%humidity, scroll_speed=.01, text_colour=r, back_colour=y)
