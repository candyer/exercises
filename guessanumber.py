def guess():
	mini = 0
	maxi = 100
	direction = 'whatever'
	print "Please think of a number between 0 and 100!"
	while direction != 'c':
		g = (mini + maxi) / 2
		print "Is your secret number ", g, "?"
		direction = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
		if direction == 'h':
			maxi = g
		elif direction == 'l':
			mini = g
		elif direction != 'c':
			print "Sorry, I did not understand your input."
	print "Game over. Your secret number was: ", g

guess()