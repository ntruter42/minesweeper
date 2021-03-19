import os, time, random
# You may create additional functions here:
def main_screen():

	os.system("cls||clear")

	print("___________________")
	print("MINESWEEPER")
	print("___________________")
	print("Play Game")
	print("Exit")

	option = input("(Play Game\Exit): ")

	option_validate(option)

def option_validate(option):

	if option.lower() == 'play game':
		dim_size= int(input("Set the dimensions of the board: "))
		num_bombs= int(input("Set the number of bombs on the board: "))
		inputvalidate(dim_size, num_bombs)
	elif option.lower()=='exit':
		print("Closing Minesweeper in 3 seconds")
		program_close()
	else:
		print("Invalid Option")
		time.sleep(1)
		main_screen()

def inputvalidate(dim_size, num_bombs):

	if dim_size < 4:
		print("Dimensions too small")
		time.sleep(1)
		main_screen()
	elif num_bombs > (dim_size * dim_size):
		print("More bombs than blocks")
		time.sleep(1)
		main_screen()
	elif num_bombs == 0:
		print("Can't play with no bombs")
		time.sleep(1)
		main_screen()
	else:
		play(dim_size, num_bombs)

def program_close():
	time.sleep(3)
	os.system("cls||clear")
	exit()

def createBoard(dim_size, num_bombs):
	board= []

	for rows in range(0, dim_size):
		board_rows=[]
		for cols in range(0, dim_size):
			board_rows.append('0')
		board.append(board_rows)

	placed_bombs= 0

	while placed_bombs != num_bombs:
		x= random.randint(0, dim_size - 1)
		y= random.randint(0, dim_size - 1)

		if board[y][x] != "*":
			placed_bombs += 1
			board[y][x] = "*"
			for rows in range(y - 1, y + 2):
				for cols in range(x - 1, x + 2):
					if (rows < 0) or (rows > dim_size - 1) or (cols < 0) or (cols > dim_size - 1) or((cols == x) and (rows == y)):
						pass
					else:
						print("rows:" + str(rows))
						print("cols:" +str(cols))
						if board[rows][cols]== '*':
							pass
						elif board[rows][cols] == ' ':
							board[rows][cols] = '1'
						else:
							value = board[rows][cols]
							value = int(value)
							value += 1
							value = str(value)
							board[rows][cols] = value

	return board

def createDisplayBoard(dim_size):
	board= []

	for rows in range(0, dim_size):
		board_rows=[]
		for cols in range(0, dim_size):
			board_rows.append(' ')
		board.append(board_rows)

	return board

def printBoard(board):
	os.system("cls||clear")
	rows= len(board)
	cols= rows + rows + 2

	output = ''
	counter= 0
	for x in range(0, cols):
		if x == 0 or x==1:
			output= output + ' '
		elif x > 1 and x%2==0:
			output= output + str(counter)
			counter += 1
		elif x > 2 and x%2==1:
			output= output + " "
	print(output)

	printBoardLine(cols)

	for y in range(0, rows):
		counter= 0
		output = ''
		output = output + str(y)
		for x in range(0, cols - 1):
			if x%2==0:
				output = output + "|"
			else:
				output = output + board[y][counter]
				counter += 1
		print(output)

	printBoardLine(cols)

def printBoardLine(cols):
	output= ''
	for x in range(0, cols):
		output= output + '-'
	print(output)

def isRevealed(display_board, solution_board, dim_size):
	for y in range(0,dim_size-1):
		for x in range(0,dim_size-1):
			if display_board[y][x] == ' ' and solution_board[y][x] != '*':
				return(False)
	return(True)

# Additional Functions above this comment

# Implement your Minesweeper Solution Below:

def play(dim_size, num_bombs):
	#Edit the code Below Here
	solution_board= createBoard(dim_size, num_bombs)
	display_board= createDisplayBoard(dim_size)
	printBoard(display_board)
	while True:
		x_input= int(input("Enter X Coordinate: "))
		y_input= int(input("Enter Y Coordinate: "))
		if x_input > dim_size - 1:
			print("Invalid X coordinate")
			time.sleep(1)
			printBoard(display_board)
		elif y_input > dim_size - 1:
			print("Invalid Y coordinate")
			time.sleep(1)
			printBoard(display_board)
		elif solution_board[y_input][x_input] == '*':
			printBoard(solution_board)
			print('Game Over!')
			done= input("Done?: ")
			main_screen()
			# TODO:
		elif isRevealed(display_board, solution_board, dim_size):
			printBoard(solution_board)
			print('Game Win!')
			done= input("Done?: ")
			main_screen()
		elif solution_board[y_input][x_input] == '0':
			for y in range(y_input - 1, y_input + 2):
				for x in range(x_input - 1, x_input + 2):
					if x<0 or x>dim_size - 1 or y<0 or y>dim_size - 1:
						pass
					else:
						display_board[y][x]= solution_board[y][x]
			printBoard(display_board)
		elif solution_board[y_input][x_input] != '0':
			display_board[y_input][x_input]= solution_board[y_input][x_input]
			printBoard(display_board)

	pass
	#Edit the code Above Here
#play Function Ends Here


if __name__=='__main__':
	main_screen()

