from os import system

def createBoard(size, bombs):
	board = []
	row = []

	for rows in range(0, size):
		for cols in range(0, size):
			row.append(" ")
		board.append(row)

	return(board)


#def place_bombs():


def printBoard(board):
	system("cls||clear")
	output_rows = len(board) + 3
	output_cols = (len(board[0]) * 2) + 2
	output = " "
	counter = 0

	for y in range(0, output_cols):
		for x in range(0, output_rows):
			if y == 0:
				if x == 0 or x == 1 or x % 2 == 1:
					output += " "
				elif x % 2 == 0:
					output += str(counter)
					counter += 1


def main():
	size = int(input("Enter the size of the board: "))
	bombs = int(input("Enter the amount of bombs: "))
	board = createBoard(size, bombs)

	printBoard(board)


if __name__ == "__main__":
	main()
