# example: size = 4
def createBoard():
    size = int(input("Input the size of the board: "))
    row = []
    board = []

    for i in range(0, size):
        row += " "
    for j in range(0, size):
        board = list.append(row)


if __name__ == "__main__":
    board = createBoard()
    print(board)
