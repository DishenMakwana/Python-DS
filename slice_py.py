test_cases = int(input())
for i in range(test_cases):
	n = int(input())
	l = [int(e) for e in input().split()]
	
	# print(l[::-1]) # reverse order
	for i in reversed(l):
		print(i,end=' ')
	print()

	l_3 = l[3::3]

	l_5 = l[5::5]

	sum_37 = sum(l[3:8])

	for e in l_3:
		print(e+3, end=" ")
	print()

	for e in l_5:
		print(e-7, end=" ")
	print()

	print(sum_37)

