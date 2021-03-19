from random import randint

def createBoard(size):
    row = []
    board = []

    for x in range(0,size):
        row.append(' ')
    for y in range(0,size):
        board.append(row)

    return(board)

def placeBombs(board, bombs):
	size = len(board)
	i = 0

	while i < bombs:
		x = randint(0,size-1)
		y = randint(0,size-1)
		if board[y][x] != '*':
			board[y][x] = '*'
			i += 1

	return(board)

def printBoard(board):
	# add 3 extra rows for number row and 2 line rows
	rows = len(board) + 3
	# multiply cols by 2 for line after cols plus add 2 for first 2 cols
	cols = (len(board[0]) * 2) + 2

	# position of x and y within board (eg. board[y_pos][x_pos])
	x_pos = 0
	y_pos = 0

	# counter for rows and columns number printout
	counter = 0

	# for loop to iterate through rows
	for y in range(0,rows):
		output = ''
		x_pos = 0
		# for loop to iterate through columns
		for x in range(0,cols):
			# first column
			if y == 0:
				# first row
				if x == 0:
					output += ' '
				# odd rows
				elif x % 2 == 1:
					output += ' '
				# even rows
				else:
					output += str(counter)
					counter += 1
			# second and last column
			elif y == 1 or y == rows - 1:
				output += '-'
				counter = 0
			# all columns between second and last
			elif y > 1 and y < rows:
				# first row
				if x == 0:
					output += str(counter)
				# odd rows
				elif x % 2 == 1:
					output += '|'
				# even rows
				else:
					output += board[y_pos][x_pos]
					x_pos += 1
					# increment y_pos only when x_pos reaches end
					if x_pos == len(board[0]):
						y_pos += 1
						counter += 1
		print(output)


if __name__ == "__main__":
	print('Enter your game options in X, Y format.')
	print('X = number of bombs\nY = size of the board')
	print('Remember that X > 0 and X < Y')
	user_options = input('X, Y: ')
	user_options = user_options.split(',')

	bombs = int(user_options[0])
	size = int(user_options[1])

	board = createBoard(size)
	board = placeBombs(board, bombs)
	print(board)

	printBoard(board)
	#takeInput()
