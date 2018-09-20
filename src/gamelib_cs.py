import ui.html
import sandbox
import sys
import os

output = []

turn_count = 0

counter_1 = 0
counter_2 = 0
counter_tie = 0

def clear_screen():
	os.system('cls' if os.name=='nt' else 'clear')

def turn(amount = 1):
	global turn_count
	turn_count += amount

def game(name='No Name Provided', desc=''):
	def decorator(fun):
		global turn_count
		global counter_1
		global counter_2
		global counter_tie
		if len(sys.argv) > 2:
			module_1 = sandbox.load_ai(sys.argv[1])
			module_2 = sandbox.load_ai(sys.argv[2])
			n = int(sys.argv[3])
			ai_1_base = os.path.basename(sys.argv[1])
			ai_2_base = os.path.basename(sys.argv[2])
			ai_1 = os.path.splitext(ai_1_base)[0]
			ai_2 = os.path.splitext(ai_2_base)[0]
		else:
			print('AI arguments unspecified?')
		#report(str(name) + '\n  ' + str(desc).replace('\n','\n  '))
		log_file = open('logfile_statistic_{}_v_{}.txt'.format(ai_1, ai_2), "w")
		log_file.close()
		for i in range(n):
			log_file = open('logfile_statistic_{}_v_{}.txt'.format(ai_1, ai_2), "a")
			log_file.write("Spiel Nummer {}:\n \n".format(i+1))
			log_file.close()
			counter_1, counter_2, counter_tie = fun(module_1, module_2, ai_1, ai_2, counter_1, counter_2, counter_tie)
			log_file = open('logfile_statistic_{}_v_{}.txt'.format(ai_1, ai_2), "a")
			if '-log' in sys.argv:
				for line in output:
					if isinstance(line, list):
						log_file.write('\n'.join(map(' '.join, line)))
					else:
						log_file.write(line)
			log_file.close()
			clear_screen()
			print('( {} / {} )'.format(i, n))
			print('Kampfgetümmel...\n \n')
			print('Anzahl der Siege von Spieler 1: {}'.format(counter_1))
			print('Anzahl der Siege von Spieler 2: {}'.format(counter_2))
			print('Anzahl der unentschiedenen Partien: {}'.format(counter_tie))
		clear_screen()
		print('( {} / {} )'.format(n, n))
		print('Fertig!')
		print('Anzahl der Siege von Spieler 1: {}'.format(counter_1))
		print('Anzahl der Siege von Spieler 2: {}'.format(counter_2))
		print('Anzahl der unentschiedenen Partien: {}'.format(counter_tie))
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

def copy_board_for_logfile(matrix):
	cpy = ''
	for i in range(len(matrix)):
		cpy += '\n'
		for j in range(len(matrix[i])):
			cpy += '{}'.format(matrix[i][j])
	return cpy

def display_board(matrix, ai_1, ai_2):
	log_file = open('logfile_statistic_{}_v_{}.txt'.format(ai_1, ai_2), "a")
	log_file.write('{}\n \n \n'.format(copy_board_for_logfile(matrix)))
	log_file.close()

def report(message):
	output.append(message)
