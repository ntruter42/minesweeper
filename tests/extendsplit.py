def validateInput(user_input):
	print(user_input)
	size = user_input[0]
	user_input[1] = int(user_input[1])

	return(user_input)

def main():
	move = [5]

	while len(move) == 1:
		move.extend(input('This is a test.\n'
		'Enter a comma seperate string: ').split(','))
		move = validateInput(move)

	print(move)

if __name__ == '__main__':
	main()
