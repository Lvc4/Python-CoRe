import gamelib
import timeout

def initialize_board():
	board = []
	for x in range(8):
		board.append([])
		for y in range(8):
			board[x].append('#')
	return board

def board_is_full(board):
	for line in board:
		for item in line:
			if item == '#': return False
	return True

def score(board):
	player_1 = 0
	player_2 = 0
	for line in board:
		for item in line:
			if item == 'X': player_1 += 1
			if item == 'O': player_2 += 1
	return (player_1, player_2)

def flip_the_shit_out_of_it(board, x, y, player, other):
	# corner kill
	if x == 1 and y == 1 and board[0][0] == other: board[0][0] = player
	if x == 1 and y == 6 and board[7][0] == other: board[7][0] = player
	if x == 6 and y == 1 and board[0][7] == other: board[0][7] = player
	if x == 6 and y == 6 and board[7][7] == other: board[7][7] = player
	# right side of it
	found = False
	for i in range(x+1,8):
		if board[y][i] == player: found = True
	if found:
		flipped = False
		for i in range(x+1,8):
			if board[y][i] == player: break
			elif board[y][i] == other:
				flipped = True
				board[y][i] = player
		if flipped: gamelib.report('Flip right!')
	# left side of it
	found = False
	for i in range(x)[::-1]:
		if board[y][i] == player: found = True
	if found:
		flipped = False
		for i in range(x)[::-1]:
			if board[y][i] == player: break
			elif board[y][i] == other:
				flipped = True
				board[y][i] = player
		if flipped: gamelib.report('Flip left!')
	# bottom side of it
	found = False
	for i in range(y+1,8):
		if board[i][x] == player: found = True
	if found:
		flipped = False
		for i in range(y+1,8):
			if board[i][x] == player: break
			elif board[i][x] == other:
				flipped = True
				board[i][x] = player
		if flipped: gamelib.report('Flip bottom!')
	# upper side of it
	found = False
	for i in range(y)[::-1]:
		if board[i][x] == player: found = True
	if found:
		flipped = False
		for i in range(y)[::-1]:
			if board[i][x] == player: break
			elif board[i][x] == other:
				flipped = True
				board[i][x] = player
		if flipped: gamelib.report('Flip top!')

@gamelib.game('CoRe', 'The Board Game')
def game(*ai_list):
	board = initialize_board()
	player = 1 # becomes 0 at first switch
	strike = [False, False]
	while True:
		if board_is_full(board): break
		gamelib.turn() # <- increases a counter value
		player = 1-player # switch player
		symbol = 'XO'[player]
		try:
			pos_x, pos_y = gamelib.get(ai_list[player], 'turn')(gamelib.copy_board(board), symbol)
			assert isinstance(pos_x, int), "X Position is not <int> object"
			assert isinstance(pos_y, int), "Y Position is not <int> object"
		except Exception as e:
			gamelib.report('Player {} loses because of raised exception: {}'.format(player+1,str(e)))
			return
		if pos_x in range(8) and pos_y in range(8) and board[pos_y][pos_x] == '#':
			gamelib.report('Player {} moved to {},{}'.format(player+1,pos_x+1,pos_y+1))
			board[pos_y][pos_x] = symbol
			flip_the_shit_out_of_it(board, pos_x, pos_y, player=symbol, other='OX'[player])
		else:
			gamelib.report('Player {} can not move to {},{}'.format(player+1,pos_x+1,pos_y+1))
			if strike[player]:
				gamelib.report('Player {} loses because of wrong gameplay.'.format(player+1))
				return
			else: strike[player] = True
		gamelib.display_board(board)
	(player_1, player_2) = score(board)
	gamelib.report('Score: {} / {}'.format(player_1, player_2))
	if player_1 > player_2:
		gamelib.report('Player 1 won!')
	if player_2 > player_1:
		gamelib.report('Player 2 won!')
	if player_1 == player_2:
		gamelib.report("It's a tie!")
