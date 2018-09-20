# When found in the nature, AIs are peaceful pets,
# however some people (often called hackers) try to turn them into evil animals,
# so be aware of not letting bad AIs in.
# This module filters bad AIs, by forcing them to play in a sandbox,
# in fact, only tame ones will play in this sandbox,
# so the bad guys will be detected!

import imp

def load_ai(filename):
	# the sandbox is currently as clever as ... well ... it's not clever
	code = open(filename).read() # quick and dirty, yet production ready code ;)
	module = imp.new_module('ai')
	mdict = module.__dict__
	def getboard(board, x, y):
		if x in range(8) and y in range(8):
			return board[y][x]
		else:
			return None
	mdict['getboard'] = getboard

	# Pop the obvious exploits
	mdict.pop('exec',0)
	mdict.pop('eval',0)

	# Lexical analyzer
	# TODO: Fix the stupid
	forbidden = ['import subprocess', 'import sys', 'import os']
	for word in forbidden:
		if word in code:
			raise Exception('Found security issue in {} while looking for {}'.format(filename, word))

	exec(code, mdict) # 'exec' is the root of all eval, here we gonna sandbox
	return module
