import random

#( x, y)

def turn(board, symbol):
	#setup Variable
	global matrix
	matrix=[[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0 ,0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0]]
	#fill matrix
	bewerten( board, symbol)
	strategy( board, symbol)
	#choose turn

def bewerten( board, symbol):
	print("bewerten")
	punkte = 0
	#matrix ändern   matrix[x][y]=7
	oben = False
	rechts = False
	unten = False
	links = False
	for x in range(8):
		for y in range(8):
			if getboard( board, x, y) == '#':
				#nach oben
				for i in range(y):
					if getboard( board, x, i) == symbol:
						oben = True
					if oben and getboard( board, x, i) != '#' and getboard( board, x, i) != symbol:
						punkte += 1

				#nach rechts
				for i in range(7-x):
					if getboard( board, 7-x, y) == symbol:
						rechts = True
					if rechts and getboard( board, 7-x, y) != '#' and getboard( board, 7-x, y) != symbol:
						punkte += 1

				#nach unten
				for i in range(7-y):
					if getboard( board, x, 7-y) == symbol:
						unten = True
					if unten and getboard( board, x, 7-y) != '#' and getboard( board, x, 7-y) != symbol:
						punkte += 1

				#nach links
				for i in range(x):
					if getboard( board, i, y) == symbol:
						links = True
					if links and getboard( board, i, y) != '#' and getboard( board, i, y) != symbol:
						punkte += 1
				matrix[x][y] = punkte

def strategy( board, symbol):
	print("Strategy")
	for i in range(6):
		matrix[0][i+1]+=1
	for i in range(6):
		matrix[7][i+1]+=1
	for i in range(6):
		matrix[i+1][7]+=1
	for i in range(6):
		matrix[i+1][0]+=1

	if getboard( board, 0, 0) != '#' and getboard( board, 1, 1) != symbol and board[1][1] == '#': matrix[1][2]+=2
	if getboard( board, 0, 7) != '#' and getboard( board, 6, 1) != symbol and board[6][1] == '#': matrix[1][6]+=2
	if getboard( board, 7, 0) != '#' and getboard( board, 1, 6) != symbol and board[6][1] == '#': matrix[6][1]+=2
	if getboard( board, 7, 7) != '#' and getboard( board, 6, 6) != symbol and board[6][1] == '#': matrix[6][6]+=2
