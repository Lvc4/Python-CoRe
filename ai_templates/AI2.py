# CoRe Turn

import random

#matrix ändern   matrix[x][y]=7
global matrix = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0 ,0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
	
def bewerten( board, symbol):	
	print("bewerten")
	for x in range(8):
		for y in range(8):
			
			#nach oben
			for i in range(y):
				if getboard( board, x, y-i-1) == '#':
			
			#nach rechts
			for i in range(7-x):
				if getboard( board, x+i+1, y) == '#':
			
			#nach unten
			for i in range(7-y):
				if getboard( board, x, y+i+1) == '#':
				
			#nach links
			for i in range(x):
				if getboard( board, x-i-1, y) == '#':
	

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
		
	if getboard( board, 0, 0) != '#' and getboard( board, 1, 1) != symbol and board[1][1] == '#': matrix[1][2]+=1
	if getboard( board, 0, 7) != '#' and getboard( board, 6, 1) != symbol and board[6][1] == '#': matrix[1][6]+=1
	if getboard( board, 7, 0) != '#' and getboard( board, 1, 6) != symbol and board[6][1] == '#': matrix[6][1]+=1
	if getboard( board, 7, 7) != '#' and getboard( board, 6, 6) != symbol and board[6][1] == '#': matrix[6][6]+=1
	
	

def turn(board, symbol):
	#fill matrix
	bewerten( board, symbol)
	strategy( board, symbol)
	#choose turn
