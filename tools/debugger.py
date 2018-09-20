turncount = 0

def turn(board, symbol):
	global turncount

	if turncount == 0:
		print('Your Symbol Is ' + symbol)
	turncount += 1

	print('{} 0 1 2 3 4 5 6 7'.format(symbol))
	for i,line in enumerate(list(map(' '.join, board))):
		print('{} {}'.format(i,line))

	while 1:
		try:
			result = eval(input('> '))
			assert isinstance(result, tuple), "Input Must Be Tuple"
			assert len(result) == 2, "Tuple Must Be Length-2"
			assert isinstance(result[0], int), "First Tuple Value Must Be Integer"
			assert isinstance(result[1], int), "Second Tuple Value Must Be Integer"
			assert result[0] in range(8), "First Tuple Value Must Be In Range(8)"
			assert result[1] in range(8), "Second Tuple Value Must Be In Range(8)"
			return result
		except KeyboardInterrupt:
			exit()
		except Exception as e:
			print(e)
			continue
