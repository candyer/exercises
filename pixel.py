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


#1 make it run with an horizontal line
def horizontal_line(pixels, width, height, black_pixel):
	"""
	this function will show you a horizontal line
	"""
	for w in range(0, width):
		pixels[w, height / 2] = black_pixel   # "height / 2" -> keep the line in the middle

make_shape(horizontal_line)


#2 make it run with a vertical line
def vertical_line(pixels, width, height, black_pixel):
	"""
	this function will show you a vertical line
	"""
	for h in range(0, height):
		pixels[width / 2, h] = black_pixel   # "width / 2" -> keep the line in the middle

make_shape(vertical_line)

		
#3 make it run with a cross
def cross(pixels, width, height, black_pixel):
	"""
	this function will show you a cross
	it only works if the image is a square
	"""
	w = 0
	h = 0
	while w < width and h < height:
		pixels[w, h] = black_pixel
		w = w + 1
		h = h + 1

	w = 0
	h = height
	while w < width and h >= 0:
		pixels[w, h-1] = black_pixel
		w = w + 1
		h = h - 1

make_shape(cross, width=300, height=300)	

#4 make a UK flag
def uk_flag(pixels, width, height, black_pixel):
	horizontal_line(pixels, width, height, black_pixel)
	vertical_line(pixels, width, height, black_pixel)
	cross(pixels, width, height, black_pixel)

make_shape(uk_flag, width=300, height=300)

#5 make it run with stripes
def stripes(pixels, width, height, black_pixel):
	""" this function will show you stripes """
	for h in range(0, height, 10):    # "10" -> the distance between the stripes
		for w in range(0, width):
			pixels[w, h] = black_pixel

make_shape(stripes)


#6 make fat stripes
def fat_stripes(pixels, width, height, black_pixel):
	""""  this function will show you fat stripes """
	stripe_size = 25      
	for h in range(0, height, stripe_size):
		for i in range(h, h + stripe_size / 2 + 1):  
			if i < height:
				for w in range(0, width):
 					pixels[w, i] = black_pixel
			
make_shape(fat_stripes)


#7 make it run with a chess board
def chess_board(pixels, width, height, black_pixel, white_pixel=(255,255,255)):
	""" this funtion will show you a chess board """
	horizontal_stripe_size = 35     
	for h in range(0, height, horizontal_stripe_size):
		for i in range(h, h + horizontal_stripe_size / 2 + 1):  
			if i < height:
				for w in range(0, width):
 					pixels[w, i] = black_pixel

 	vertical_stripe_size = 35    
	for w in range(0, width, vertical_stripe_size):
		for j in range(w, w + vertical_stripe_size / 2 + 1):  
			if j < width:
				for h in range(0, height):
					pixels[j, h] = black_pixel
					for n in range(0, height, horizontal_stripe_size):
						for m in range(n, n + horizontal_stripe_size / 2 + 1):
							if m < height:
								pixels[j, m] = white_pixel
 				
make_shape(chess_board)

#7-1 better solution
def example_chess(pixels, width, height, black_pixel):
	thick_w = width / 8.0
	thick_h = height / 8.0
	for w in range(width):
		for h in range(height):
			if (w // thick_w) % 2 == (h // thick_h) % 2:
				pixels[w, h] = black_pixel

make_shape(example_chess)


#8 make it run with a black circle:)
def black_circle(pixels, width, height, black_pixel):
	""" this function will show you a circle """
	import math
	if height < width:
		radius = height / 2
	else:
		radius = width / 2
	middle_pixel = [width / 2 , height / 2]
	for h in range(height):
		for w in range(width):	
			distance = math.sqrt((w - width / 2)**2 + (h - height / 2)**2)
			if distance <= radius:
				pixels[w , h] = black_pixel
	
make_shape(black_circle)


#9 make it run with an empty circle:)
def empty_circle(pixels, width, height, black_pixel):
	""" this function will show you a circle """
	import math
	if height < width:
		radius = height / 2
	else:
		radius = width / 2
	# or radius = min(width, height) / 2 
	for h in range(height):
		for w in range(width):	
			distance = math.sqrt((w - width / 2)**2 + (h - height / 2)**2)
			if abs(distance - radius) <= 1:
				pixels[w , h] = black_pixel
			
make_shape(empty_circle)