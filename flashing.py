
from sense_hat import SenseHat
import time
import random

# connects our Pi to the SenseHat
sense = SenseHat()

# define a colour
r = [255, 0, 0]

# set a frequence
frequency = 1

# clear the matrix before starting
sense.clear()

# while True - i.e. run forever
while True:
    # get two random numbers between 0 and 7
	x = random.randint(0, 7)
	y = random.randint(0, 7)
	# change the pixel at x,y
	sense.set_pixel(x, y, r)
	# wait for frequency before looping around again
	time.sleep(frequency)



