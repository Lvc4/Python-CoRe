import ui.html
import sandbox
import sys

output = []

turn_count = 0

def turn(amount = 1):
	global turn_count
	turn_count += amount

def game(name='No Name Provided', desc=''):
	def decorator(fun):
		global turn_count
		if len(sys.argv) > 2:
			module_1 = sandbox.load_ai(sys.argv[1])
			module_2 = sandbox.load_ai(sys.argv[2])
		else:
			print('AI arguments unspecified?')
		report(str(name) + '\n  ' + str(desc).replace('\n','\n  '))
		fun(module_1, module_2)
		if '-justresult' in sys.argv:
			print(output[-1])
		elif '-log' in sys.argv:
			for line in output:
				if isinstance(line, list):
					print('\n'.join(map(' '.join, line)))
				else:
					print(line)
		else:
			ui.html.display(output,turn_count)
		return fun
	return decorator

def get(module, field):
	# Injection alert! (not dangerous, since we, the devs, write the games)
	return eval('module.'+field)

def copy_board(matrix):
	cpy = []
	for i in range(len(matrix)):
		cpy.append([])
		for j in range(len(matrix[i])):
			cpy[i].append(matrix[i][j])
	return cpy

def display_board(matrix):
	output.append(copy_board(matrix))

def report(message):
	output.append(message)
