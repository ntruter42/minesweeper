from os import system
from random import randint

def playGame(board, solution):
	play = 1

	while play:
		system('clear')
		# TODO: printBoard(board)
		printBoard(solution)
		user_input = input('''
		Enter s,s to give up and show solution.
		Input as row,col a block to search:
		''').split(',')
		user_input.append(str(len(board)))
		if validateInput(user_input, 1):
			if revealSelection(board, solution, user_input) in {0, 1}:
				system('clear')
				printBoard(solution)
				print('Game over!')
				play = 0
		else:
			pass


def revealSelection(board, solution, user_input):
	x = user_input[0]
	y = user_input[1]

	if x == 's' and y == 's':
		return(0)
	elif solution[y][x] == '*':
		return(1)
	elif int(solution[y][x]) > 0:
		board[y][x] = solution[y][x]
	else:
		for y in range(y - 1, y + 2):


def validateInput(user_input, check):
	if check == 0:
		if user_input.lower() == 'play' or user_input == '1':
			return(1)
		elif user_input.lower() == 'show' or user_input == '2':
			return(2)
		elif user_input.lower() == 'exit' or user_input == '3':
			return(3)
		else:
			print('Error: Invalid input. Expected "Play", "Show" or "Exit"')
	elif check == 1:
		if int(user_input[0]) > 0 and \
				int(user_input[0]) < int(user_input[2]) and \
				int(user_input[1]) > 0 and \
				int(user_input[1]) < int(user_input[2]):
			return(1)
		elif user_input[0].lower() == 's' and user_input[1].lower() == 's':
			return(2)
		else:
			print('Error: Invalid input. Expected "s,s" or numbers in the format X,Y')
	elif check == 2:
		pass

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
					output += board[y_pos][x_pos]
					x_pos += 1
					if x_pos == size:
						x_pos = 0
						y_pos += 1
					if y_pos == size:
						y_pos = 0
		print(output)


def printBoard_old(board):
	size = len(board)
	output_rows = size + 3
	output_cols = (size * 2) + 2
	counter = 0
	x_pos = 0
	y_pos = 0

	space = 0
	if size > 10:
		space += 1

	for y in range(0, output_rows):
		output = ''
		for x in range(0, output_cols):
			if y == 0:
				if x == 0 or x % 2 != 0:
					if space and x == 0:
						output += ' '
					if counter < 10:
						output += ' '
				else:
					if counter % 2 != 0:
						output += '\x1b[90m'
					output += str(counter)
					output += '\x1b[0m'
					counter += 1
			elif y == 1 or y == output_rows - 1:
				if size > 10 and x == 0:
					output += '-'
				output += '-'
				counter = 0
			elif y > 1 and y < output_rows:
				if x == 0:
					if counter % 2 == 1:
						output += '\x1b[90m'
					if size > 10 and counter < 10:
						output += ' '
					output += str(counter)
					output += '\x1b[0m'
					counter += 1
				elif x % 2 == 1:
					output += '|'
				else:
					output += board[y_pos][x_pos]
					x_pos += 1
					if x_pos == size:
						x_pos = 0
						y_pos += 1
					if y_pos == size:
						y_pos = 0
		print(output)


def main():
	size = int(input('Enter the size of the board: '))
	bombs = int(input('Enter the amount of bombs: '))
	board = createBoard(size)
	solution = createBoard(size)
	placeBombs(solution, bombs)

	level = input('''
	What would you like to do? (Enter your choice)
	1) Play Game --> Play
	2) Show Solution --> Show
	3) Exit Game--> Exit
	''')
	play = 1
	while play:
		playGame(board, solution)
		play = int(input('Play again? 1 or 0: '))

if __name__ == '__main__':
	main()
