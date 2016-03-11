word = []
data_out_list = []
score_dicti = {}
count_check = 0
from settings import avg_time_params



class mntree(dict):
	"""docstring for mntree - defining the datastructure as a class"""
	def __init__(self):
		pass
	
	#usng same enter function for key insert and score insert by introducing new argument 'status'. It will be 'basic' always for key entry. 
	#But different for score entry
	def enter(self, key_dictionary, status = 'basic'):
		print('entering enter with status', status)
		#fetching each key and sending to the dict create function
		key_key = sorted(key_dictionary) #returns sorted key from dictionary as a list
		dictionary = self
		if status == 'basic':
			for key_key in key_key:
				#print(key_val.name)
				dictionary = key_to_dict(key_dictionary[key_key], dictionary) #returning dictionary recursively
		else:
			for key_key in key_key:
				#print(key_val.name)
				dictionary = key_to_sdict(key_dictionary[key_key], dictionary) #returning dictionary recursively			

	def testprint(self):
		printintheorder(self)

	def filewrite(self):
		global data_out_list
		data_out_list = []
		dict_to_file(self)
		return data_out_list

	def checker(self, keydict, sdicti):
		global score_dicti, count_check
		score_dicti = {}
		count_check = 0
		dictionary = self
		key_key = sorted(keydict) #returns sorted key from dictionary as a list
		for key_key in key_key:
			dictionary = key_in_dict(keydict[key_key], dictionary, sdicti) #returning dictionary recursively
		return sdicti.enter(score_dicti, 'advanced')

class check_key:
	"""docstring for check_key - using for comapring old user with user in the database"""
	def __init__(self, name):
		self.hold_score = 0
		self.releasedn_score = 0
		self.name = name


def comparer(a, b):
	if (b*1.3) >= a >= (b*0.7):
		print('returning zero in comparer')
		return 0
	else:
		print('else in comparer')
		return 1 


def key_in_dict(key_val, dictionary, sdicti):
	global count_check, score_dicti
	for key in dictionary:
		if key.name == key_val.name:
			vars()[key.name] = check_key(key.name)
			if key_val.hold != 0 and key.hold != 0:
				vars()[key.name].hold_score = (comparer(key_val.hold, key.hold))
			if key_val.releasedn != 0 and key.releasedn != 0:
				vars()[key.name].releasedn_score = (comparer(key_val.releasedn, key.releasedn))
			count_check += 1
			print('count_check: ', count_check)
			score_dicti[count_check] = vars()[key.name]
			return dictionary[key]
	return {} 



def dict_to_file(dictionary):
	try:
		global word, data_out_list
		temp_var = 0
		for key in dictionary:
			#print(key.name)
			temp_var = 1
			word.append(key)
			#print('word length', len(word))
			dict_to_file(dictionary[key])
		if temp_var == 0:
			data_out_list.append(list(word))
			#print('****main length****', len(data_out_list))
		word.pop()
	except Exception as e:
		print('exception in dict_to_file: ', e)


def printintheorder(dictionary):
	for key in dictionary:
		print(key.name)
		printintheorder(dictionary[key])

def key_to_dict(key_val, dictionary):
	global avg_time_params, key_dict, prev_avg
	for key in dictionary:
		if key.name == key_val.name:
			#handling non usual high key releasedn value
			temp_avg = key.releasedn * 2
			key.hold = (key.hold + key_val.hold)/2

			#handling cases with zero releasedn value 
			if key.releasedn == 0.0:
				if key_val.releasedn <= avg_time_params[1]:
					key.releasedn = key_val.releasedn#handling non usual high key releasedn value
					avg_time_params[1] = (avg_time_params[1] + key.releasedn)/2
					return dictionary[key]
				else:
					return dictionary[key]
			elif key_val.releasedn == 0.0:
				avg_time_params[1] = (avg_time_params[1] + key.releasedn)/2
				return dictionary[key]				
			elif key_val.releasedn > temp_avg:#handling non usual high key releasedn value

				print('starting variable emptying process')
				#emptying variables because of the non usual delay in keystroke
				dict_time_args = {0:[0.0, 0.0]}
				dict_counter = {'Space':0}
				counter = 0
				key_dict.clear()

				#not changing any values because we think that the value can be wrong
				return dictionary[key]
			else:
				key.releasedn = (key.releasedn + key_val.releasedn)/2
				avg_time_params[1] = (avg_time_params[1] + key_val.releasedn)/2
				return dictionary[key]
	
	#handling key_val.releasedn value if it is more than usual hold time
	dictionary[key_val] = {}
	return dictionary[key_val]


def key_to_sdict(key_val, dictionary):
	for key in dictionary:
		if key.name == key_val.name:
			key.hold_score += key_val.hold_score
			key.releasedn_score += key_val.releasedn_score
			return dictionary[key]	
	dictionary[key_val] = {}
	return dictionary[key_val]
