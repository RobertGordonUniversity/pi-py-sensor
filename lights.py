
from sense_hat import SenseHat


# connects our Pi to the SenseHat
sense = SenseHat()


# define an x and y value and a colour
x = 3
y = 3
red = [255, 0, 0]

# set a single pixel
sense.set_pixel(x, y, red)
