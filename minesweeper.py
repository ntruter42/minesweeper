from os import system
from random import randint

class RangeError(Exception):
	pass


def validateInput(user_input, check):
	red = '\x1b[1;31m'
	green = '\x1b[1;32m'
	reset = '\x1b[0m'
	# Check game choice in string format
	if check == 0:
		try:
			user_input = user_input.lower()
			if user_input == 'play' or user_input == '1':
				return(1)
			elif user_input == 'show' or user_input == '2':
				return(2)
			elif user_input == 'exit' or user_input == '3':
				return(3)
			else:
				raise ValueError
		except ValueError:
				print('{}Invalid input. Expected 1/Play, 2/Show or 3/Exit.{}'
						.format(red, reset))
				system('sleep 2')
				return(0)
	# Check size of board in string format - user_input[0]
	elif check == 1:
		try:
			size = int(user_input)
			if 4 <= size <= 100:
				print('Size validated: {}{}{}'.format(green, size, reset))
				return(size)
			else:
				raise RangeError
		except ValueError:
			print('{}Invalid input. Expected a NUMBER between 4 and 100.{}'
					.format(red, reset))
		except RangeError:
			print('{}Invalid number. Expected a value BETWEEN 4 and 100.{}'
					.format(red, reset))
		system('sleep 2')
		return (0)
	# Check amount of bombs in string format user_input[1]
	elif check == 2:
		max = int(user_input[1]) * int(user_input[1])
		try:
			bombs = int(user_input[2])
			if 1 <= bombs < max:
				print('Bombs validated: {}{}{}'.format(green, bombs, reset))
				return(bombs)
			else:
				raise RangeError
		except ValueError:
			print('{}Invalid input. Expected a NUMBER between 1 and {}.{}'
					.format(red, max - 1, reset))
		except RangeError:
			print('{}Invalid number. Expected a value BETWEEN 1 and {}.{}'
					.format(red, max - 1, reset))
		system('sleep 2')
		return (0)
	# Check move co-ordinates in string format X,Y
	elif check == 3:
		if len(user_input) != 3:
			print('{}Invalid input. Expected 2 comma seperated values X,Y.{}'
					.format(red, reset))
		elif user_input[0].lower() == 's' and user_input[1].lower() == 's':
			return(1)
		else:
			try:
				xy = [int(user_input[0]), int(user_input[1])]
				size = user_input[2]
				if xy[0] >= 0 and xy[0] < size and xy[1] >= 0 and xy[1] < size:
					return(xy)
				else:
					raise RangeError
			except ValueError:
				print('{}Invalid input. Expected S,S or NUMBERS in the format X,Y.{}'
						.format(red, reset))
			except RangeError:
				print('{}Invalid number(s). Expected numbers BETWEEN 0 and {}.{}'
						.format(red, size - 1, reset))
		system('sleep 2')
		return(0)

	return(0)


def createBoard(size):
	board = []

	for n in range(0, size):
		row = [' ']*size
		board.append(row)

	return(board)


def placeBombs(board, bombs):
	size = len(board)
	n = 0

	while n < bombs:
		x = randint(0, size - 1)
		y = randint(0, size - 1)
		if board[y][x] != '*':
			board[y][x] = '*'
			n += 1


def countBombs(board):
	size = len(board)

	for y in range(0, size):
		for x in range(0, size):
			print('\x1b[32m', y, x, '\x1b[0m', end='')
			if board[y][x] == '*':
				for i in range(y-1, y+2):
					for j in range(x-1, x+2):
						if 0 <= i < size and 0 <= j < size:
							if i == y and j == x:
								pass
							else:
								print('\x1b[31m', i, j, '\x1b[0m', end='')
								if board[i][j] == ' ':
									board[i][j] = 1
								elif board[i][j] == '*':
									pass
								elif 0 < board[i][j] < 8:
									board[i][j] += 1
	print()


def playGame(solution, board):
	play = True
	size = len(board)

	while play:
		system('clear')
		printBoard(board)
		move = 0

		while move == 0:
			move = input('Enter S,S to give up and show the solution OR\n'
			'Input a block to search as row,col: ').split(',')
			move.append(size)
			move = validateInput(move, 3)

		if move == 1:
			system('clear')
			printBoard(solution)
			system('sleep 2')
			play = False
		else:
			print(move)
			system('sleep 2')
			# TODO: revealSelection(solution, board, move)
			# TODO: win = checkBoard(board) -> return(-1/0/1)

'''
def revealSelection(solution, board, move):
	x = move[0]
	y = move[1]

	if solution[y][x] == '*':
		return(1)
	elif int(solution[y][x]) > 0:
		board[y][x] = solution[y][x]
	else:
		for y in range(y - 1, y + 2):
			pass
'''

def printBoard(board):
	size = len(board)
	output_rows = size + 3
	output_cols = (size * 3) + 3
	counter = 0
	x_pos = 0
	y_pos = 0

	for y in range(0, output_rows):
		output = ''
		for x in range(0, output_cols):
			if y == 0:
				if x == 0 or x % 3 == 1 or x % 3 == 2:
					if x % 3 == 2 and counter > 10:
						continue
					output += ' '
				else:
					if counter % 2 != 0:
						output += '\x1b[90m'
					output += str(counter)
					output += '\x1b[0m'
					counter += 1
			elif y == 1 or y == output_rows - 1:
				output += '-'
				counter = 0
			elif y > 1 and y < output_rows:
				if x == 0:
					if counter % 2 != 0:
						output += '\x1b[90m'
					if counter < 10:
						output += str(counter)
					else:
						output += str(counter // 10)
				elif x == 1:
					if counter < 10:
						output += ' '
					else:
						output += str(counter % 10)
					output += '\x1b[0m'
					counter += 1
				elif x % 3 == 2:
					output += '|'
				elif x % 3 == 1:
					output += ' '
				else:
					output += str(board[y_pos][x_pos])
					x_pos += 1
					if x_pos == size:
						x_pos = 0
						y_pos += 1
					if y_pos == size:
						y_pos = 0
		print(output)


def main():
	system('clear')
	print('What would you like to do?\n'
	'1) Play Game\n'
	'2) Show Solution\n'
	'3) Exit Game')
	options = [0, 0, 0]
	board = []

	# options[0] = game choice
	while options[0] == 0:
		options[0] = validateInput(input('Your choice: '), 0)
	# options[1] = size
	while options[1] == 0:
		options[1] = validateInput(input('Enter the size of the board: '), 1)
	# options[2] = bombs
	while options[2] == 0:
		options[2] = input('Enter the amount of bombs: ')
		options[2] = validateInput(options, 2)

	# board[0] = solution board
	board = [createBoard(options[1])]
	placeBombs(board[0], options[2])
	countBombs(board[0])

	if options[0] == 1:
		# board[1] = playing board
		board.append(createBoard(options[1]))

		playGame(board[0], board[1])

	elif options[0] == 2:
		printBoard(board[0])
	elif options[0] == 3:
		for i in range(0, 3):
			system('clear')
			print('Game will close in {} second(s).'.format(3 - i))
			system('sleep 1')
	else:
		main()

	exit()

if __name__ == '__main__':
	main()
