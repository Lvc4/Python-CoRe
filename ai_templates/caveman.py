
# CoRe Turn
def turn(board, symbol):
	for x in range(8):
		for y in range(8):
			if getboard(board,x,y) == '#': # Empty
				return (x,y)
			elif getboard(board,x,y) == symbol: # Self
				pass
			else: # Other
				pass
