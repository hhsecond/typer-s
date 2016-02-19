dicti = {'n':{'e':{'v':{'e':{'r':{}}}, 'm':{'e':{'n':{}}}}}}
def dict_write(dictionary = dicti):
	if dictionary.keys():
		curr_val = list(dictionary)[0]
		print(curr_val)
		if not dict_write(dictionary[curr_val]):
			del dictionary[curr_val]
			if dictionary.keys():
				return True
			else:
				return False
		return True
	return False


while dicti.keys():
	dict_write()
	print(' ')