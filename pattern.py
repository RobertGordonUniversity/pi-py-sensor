
from sense_hat import SenseHat

# connects our Pi to the SenseHat
sense = SenseHat()

# define two colours and them draw them on the matrix
r = [255, 0, 0]
y = [255, 255, 0]

# the "image" to be displayed
cross = [
 	r, y, y, y, y, y, y, r,
 	y, r, y, y, y, y, r, y,
 	y, y, r, y, y, r, y, y,
 	y, y, y, r, r, y, y, y,
 	y, y, y, r, r, y, y, y,
 	y, y, r, y, y, r, y, y,
 	y, r, y, y, y, y, r, y,
 	r, y, y, y, y, y, y, r,
 ];

# display the image
sense.set_pixels(cross)
