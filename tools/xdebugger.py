import readline

def turn(board, symbol):
	def printfmt(string):
		self = symbol
		other = 'X' if symbol != 'X' else 'O'
		fmtstring = str(string)               \
			.replace('#', '.')                \
			.replace(self, '\033[92m☻\033[0m') \
			.replace(other, '\033[91m☻\033[0m')
		print(fmtstring)

	def printbrd(sym):
		printfmt('\n{} 0 1 2 3 4 5 6 7'.format(sym))
		for i,line in enumerate(list(map(' '.join, board))):
			printfmt('{} {}'.format(i,line))

	printbrd('X' if symbol != 'X' else 'O')

	while 1:
		try:
			result = eval('(' + input('\n> ') + ')')
			assert isinstance(result, tuple), "Input Must Be Tuple"
			assert len(result) == 2, "Tuple Must Be Length-2"
			assert isinstance(result[0], int), "First Tuple Value Must Be Integer"
			assert isinstance(result[1], int), "Second Tuple Value Must Be Integer"
			assert result[0] in range(8), "First Tuple Value Must Be In Range(8)"
			assert result[1] in range(8), "Second Tuple Value Must Be In Range(8)"
			assert board[result[1]][result[0]] == '#', "Field Occupiet"
			if result in [(1,1),(6,6),(1,6),(6,1)]:
				yesno = input('Sure you wanna go there?')
				assert yesno == 'yes', "Not answered 'yes'"
			return result
		except KeyboardInterrupt:
			exit()
		except Exception as e:
			print(e)
			continue
