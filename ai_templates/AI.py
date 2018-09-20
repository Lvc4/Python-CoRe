# CoRe Turn

import random

def randomZug( board, symbol):
	print("randomZug")
	while 1:
		x = random.choice(range(8))
		y = random.choice(range(8))
		if getboard(board, x, y) == '#': return ( x, y)
		
def catchCorners( board, symbol):
	print("catchCorners")
	if getboard( board, 0, 0) != '#' and getboard( board, 0, 0) != symbol and board[1][1] == '#': return ( 1, 1)
	if getboard( board, 0, 7) != '#' and getboard( board, 0, 7) != symbol and board[1][6] == '#': return ( 1, 6)
	if getboard( board, 7, 0) != '#' and getboard( board, 7, 0) != symbol and board[6][1] == '#': return ( 6, 1)
	if getboard( board, 7, 7) != '#' and getboard( board, 7, 7) != symbol and board[6][6] == '#': return ( 6, 6)
	return( -1, -1)

def catchNext(board,symbol):
	print("catchNextFreeStone")
	for x in range(8):
		for y in range(8):
			if getboard( board, x, y+1) == '#': return ( x, y+1)
			if getboard( board, x+1, y) == '#': return ( x+1, y)
			if getboard( board, x, y-1) == '#': return ( x, y-1)
			if getboard( board, x-1, y) == '#': return ( x-1, y)
	return( -1,-1)
	
def catchMost( board, symbol):	
	print("catchMost")
	return(0,0)

def catchBoarder( board, symbol):
	print("catchBoarder")
	for i in range(6):
		if getboard(board, 0, i+1) == '#': return ( 0, i+1)
	for i in range(6):
		if getboard(board, 7, i+1) == '#': return ( 7, i+1)
	for i in range(6):
		if getboard(board, i+1, 7) == '#': return ( i+1, 7)
	for i in range(6):
		if getboard(board, i+1, 0) == '#': return ( i+1, 0)
	return( -1, -1)
	

def turn(board, symbol):
	# first try to catch corners
	x,y=catchCorners( board, symbol)
	print(x,y)
	print(" ")
	if x != -1:return( x, y)
	#if no corners available catch border Stones
	x,y=catchBoarder( board, symbol)
	print(x,y)
	print(" ")
	if x != -1:return( x, y)
	
	# chose random strategy
	randomStategy = random.choice(range(2))
	if randomStategy == 0: 
		return(randomZug( board, symbol))
		print(x,y)
		print(" ")
	elif randomStategy == 1: 
		return(catchNext( board, symbol))
		print(x,y)
		print(" ")
	elif randomStategy == 2: 
		return(catchMost( board, symbol))