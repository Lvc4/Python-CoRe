
# CoRe Turn
def turn(board, symbol):
	for x in range(8):
		for y in range(8):
			if getboard(board,x,y) != '#' and getboard(board,x,y) != symbol:
				if x == 0 and y == 0 and board[1][1] == '#': return (1,1)
				if x == 0 and y == 7 and board[6][1] == '#': return (1,6)
				if x == 7 and y == 0 and board[1][6] == '#': return (6,1)
				if x == 7 and y == 7 and board[6][6] == '#': return (6,6)
				else:
					if getboard(board,x,y+1) == '#': return (x,y+1)
					if getboard(board,x+1,y) == '#': return (x+1,y)
					if getboard(board,x,y-1) == '#': return (x,y-1)
					if getboard(board,x-1,y) == '#': return (x-1,y)
	return (0,0)
