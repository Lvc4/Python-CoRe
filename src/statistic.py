import gamelib_cs

ai_1 = ''
ai_2 = ''

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
	log_file = open('logfile_statistic_{}_v_{}.txt'.format(ai_1, ai_2), "a")
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
		if flipped: log_file.write('Flip right!\n')
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
		if flipped: log_file.write('Flip left!\n')
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
		if flipped: log_file.write('Flip bottom!\n')
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
		if flipped: log_file.write('Flip top!\n')

@gamelib_cs.game('CoRe', 'The Board Game')
def game(*ai_list):
	global ai_1
	global ai_2
	counter_1 = ai_list[4]
	counter_2 = ai_list[5]
	counter_tie = ai_list[6]
	ai_1 = ai_list[2]
	ai_2 = ai_list[3]
	ai_list = ai_list[0:2]
	board = initialize_board()
	player = 1 # becomes 0 at first switch
	strike = [False, False]
	while True:
		if board_is_full(board): break
		gamelib_cs.turn() # <- increases a counter value
		player = 1-player # switch player
		symbol = 'XO'[player]
		try:
			pos_x, pos_y = gamelib_cs.get(ai_list[player], 'turn')(gamelib_cs.copy_board(board), symbol)
			assert isinstance(pos_x, int), "X Position is not <int> object"
			assert isinstance(pos_y, int), "Y Position is not <int> object"
		except Exception as e:
			log_file = open('logfile_statistic_{}_v_{}.txt'.format(ai_1, ai_2), "a")
			log_file.write('Player {} loses because of raised exception: {}\n \n \n'.format(player+1,str(e)))
			log_file.close()
			if player%2==0:
				counter_2+=1
			if player%2==1:
				counter_1+=1
			return (counter_1, counter_2, counter_tie)
		if pos_x in range(8) and pos_y in range(8) and board[pos_y][pos_x] == '#':
			log_file = open('logfile_statistic_{}_v_{}.txt'.format(ai_1, ai_2), "a")
			log_file.write('Player {} moved to {},{}\n \n'.format(player+1,pos_x+1,pos_y+1))
			log_file.close()
			board[pos_y][pos_x] = symbol
			flip_the_shit_out_of_it(board, pos_x, pos_y, player=symbol, other='OX'[player])
		else:
			log_file = open('logfile_statistic_{}_v_{}.txt'.format(ai_1, ai_2), "a")
			log_file.write('Player {} can not move to {},{}\n \n'.format(player+1,pos_x+1,pos_y+1))
			log_file.close()
			if strike[player]:
				log_file = open('logfile_statistic_{}_v_{}.txt'.format(ai_1, ai_2), "a")
				log_file.write('Player {} loses because of wrong gameplay.\n \n \n'.format(player+1))
				log_file.close()
				if player%2==0:
					counter_2+=1
				if player%2==1:
					counter_1+=1
				return (counter_1, counter_2, counter_tie)
			else: strike[player] = True
		gamelib_cs.display_board(board, ai_1, ai_2)
	(player_1, player_2) = score(board)
	log_file = open('logfile_statistic_{}_v_{}.txt'.format(ai_1, ai_2), "a")
	log_file.write('Score: {} / {}\n \n \n'.format(player_1, player_2))
	if player_1 > player_2:
		log_file.write('Player 1 won!\n \n \n')
		counter_1+=1
	if player_2 > player_1:
		log_file.write('Player 2 won!\n \n \n')
		counter_2+=1
	if player_1 == player_2:
		log_file.write("It's a tie!\n \n \n")
		counter_tie+=1
	log_file.close()
	return (counter_1, counter_2, counter_tie)
	
