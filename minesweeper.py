from os import system

def createBoard(size, bombs):
	row = []
	board = []

	for x in range(0, size):
		row.append(" ")
	for y in range(0, size):
		board.append(row)

	return(board)


#def place_bombs():


def printBoard(board):
	system("cls||clear")
	size = len(board)
	output_rows = size + 3
	output_cols = (size * 2) + 2

	x_pos = 0
	y_pos = 0

	counter = 0

	extra_space = 0
	if size > 10:
		extra_space += 1

	for y in range(0, output_rows):
		output = ""
		x_pos = 0
		for x in range(0, output_cols):
			if y == 0:
				if x == 0 or x % 2 == 1:
					output += " "
				else:
					output += str(counter)
					counter += 1
			elif y == 1 or y == output_rows - 1:
				output += "-"
				counter = 0
			elif y > 1 and y < output_rows:
				if x == 0:
					if size > 10 and counter < 10:
						output += " "
					output += str(counter)
				elif x % 2 == 1:
					output += "|"
				else:
					output += board[y_pos][x_pos]
					x_pos += 1
					if x_pos == len(board):
						y_pos += 1
						counter += 1
		print(output)


def main():
	size = int(input("Enter the size of the board: "))
	bombs = int(input("Enter the amount of bombs: "))
	board = createBoard(size, bombs)

	printBoard(board)


if __name__ == "__main__":
	main()
