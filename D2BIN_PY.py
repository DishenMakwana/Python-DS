def dec_to_bin(n):

	if n == 0:
		return '0'
	else:
		return dec_to_bin(n//2) + str(n % 2)


for _ in range(int(input())):

	n = int(input())
	binary_string =  dec_to_bin(n)
	binary_string = '0' * (8 - len(binary_string)) + binary_string

	print(binary_string)