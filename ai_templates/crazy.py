
import random

# CoRe
def turn(board, symbol):
	while 1:
		x = random.choice(range(8))
		y = random.choice(range(8))
		if getboard(board,x,y) == '#': return (x,y)
