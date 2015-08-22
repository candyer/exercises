from PIL import Image

def make_shape(func, width=300, height=100):
	'''
	take a function and use it to draw a shape :D
	the function will receive the arguments:
	- pixels: a 2d list
	- width: the width of the image
	- height: the eight of the image
	- black_pixel: a black pixel that can be put inside "pixels"
	'''
	img = Image.new('RGB', (width, height), "white") # create a new black image
	pixels = img.load() # create the pixel map
	black_pixel = (0, 0, 0)
	func(pixels, width, height, black_pixel)
	img.show()

def example_random_pixels(pixels, width, height, black_pixel):
	''' example drawing function that put 2000 points at random '''
	from random import randint
	for i in range(2000):
		pixels[randint(0, width - 1), randint(0, height - 1)] = black_pixel

# we run it with example_random_pixels
make_shape(example_random_pixels)

# make it run with an horizontal line


# make it run with a vertical line


# make it run with a cross


# make it run with stripes


# make it run with a chess board


# make it run with a circle :)






