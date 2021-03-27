options = []
i = 0
sum = 0

while True:
	options.append(int(input('Enter a value: ')))
	if options[i] == 0:
		break
	i += 1

for n in range(0, i):
	sum += options[n]

average = sum // i

print(options)
print("The sum of all the values you typed is {} and the average is {}."
		.format(sum, average))
