
from sense_hat import SenseHat

# connects our Pi to the SenseHat
sense = SenseHat()

# define two colours
r = [255, 0, 0]
y = [255, 255, 0]

# display a message
sense.clear()
sense.show_message("hello!!", scroll_speed=0.1, text_colour=r, back_colour=y)
