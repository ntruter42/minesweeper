for n in range(0, 5):
	for i in range(n-1, n+2):
		if 0 <= i < 5 and i != n:
			print("n:", n, "| i:", i)
		else:
			pass

print()

for n in range(0, 5):
	for i in {n-1, n+1}:
		if 0 <= i < 5:
			print("n:", n, "| i:", i)
		else:
			pass
