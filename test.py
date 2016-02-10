def test():
	a = input('enter variable name')
	b = input('enter variabe value')
	vars()[a] = b
	return vars()[a]


print(test())