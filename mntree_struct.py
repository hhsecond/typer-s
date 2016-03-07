class mntree(dict):
	"""docstring for mntree - defining the datastructure as a class"""
	def __init__(self):
		pass
	def enter(self, key_dict):
		#fetching each key and sending to the dict create function
		key_key = sorted(key_dict) #returns sorted key from dictionary as a list
		dictionary = self
		for key_key in key_key:
			#print(key_val.name)
			dictionary = key_to_dict(key_dict[key_key], dictionary) #returning dictionary recursively


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
				key_dict = {}

				#not changing any values because we think that the value can be wrong
				return dictionary[key]
			else:
				key.releasedn = (key.releasedn + key_val.releasedn)/2
				avg_time_params[1] = (avg_time_params[1] + key_val.releasedn)/2
				return dictionary[key]
	
	#handling key_val.releasedn value if it is more than usual hold time
	dictionary[key_val] = {}
	return dictionary[key_val]

