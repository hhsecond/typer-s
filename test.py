




		

class objthread(threading.Thread):
	"""docstring for objthread - thread module calling by keystroke for creating object and adding each object to tree"""
	def __init__(self, event_name, event_window, event_time, event_status):
		threading.Thread.__init__(self)
		self.start()
		print(event_name)


		global dict_obj_order, dict_obj_key, counter, key_list
		if event_status == 1:
			#fetching second and millisecond from the time
			etime =	event_time.timestamp()
			#print(event_name, etime, event_status, counter)
			#two dictionaries: one for storing current values another for finding previous value
			dict_obj_key[event_name] = counter
			print(event_name, 'dict_obj_key', dict_obj_key)
			dict_obj_order[counter] = [etime]#this list (RHS) will get up time from below else condition
			print(event_name, 'dict_obj_order', dict_obj_order)
			counter += 1

		else:
			#fetching second and millisecond from the time
			etime =	event_time.timestamp()
			#print('key up', event_name,	etime)
			count = dict_obj_key.pop(event_name)
			#print('lis',lis)
			prev_dict_count = count - 1
			cur_dict_count = count
			print(event_name, 'prev_dict_count',prev_dict_count)
			
			dict_obj_order[cur_dict_count].append(etime) #first element of this list is down time and second eleement is up time
			print(event_name, 'dict_obj_order', dict_obj_order)

			prev_dntime = dict_obj_order[prev_dict_count][0]
			#prev_uptime = dict_obj_order[prev_dict_count][1]
			
			#print('previous key time', prev_time)
			#print(event_name, etime, lis[1], prev_time)
			releasedn = 1.0#(dict_obj_order[cur_dict_count] - prev_dntime)
			hold = 1.0#(etime - dict_obj_order[cur_dict_count][0])
			#to avoid long time lag of user because he is not typing and to avoid the first key stroke error
			if not prev_dntime:
				releasedn = 0.0
				vars()[event_name] = key(event_name, hold, releasedn)
				key_list.append(vars()[event_name])
			elif  releasedn > 3.0:
				releasedn = 0.0
				vars()[event_name] = key(event_name, hold, releasedn)
				key_list.append(vars()[event_name])
				dict_create(key_list, dicti)
				key_list = []
				#making the datastructures free for next word
				dict_obj_order = {0:[0.0, 0.0]}
				dict_obj_key = {'Space':['Space', 0.0, 0]}
				counter = 1
			elif event_name == 'Space':
				vars()[event_name] = key(event_name, hold, releasedn)
				key_list.append(vars()[event_name])
				dict_create(key_list, dicti)
				key_list = []
				#making the datastructures free for next word
				dict_obj_order = {0:[dict_obj_order[cur_dict_count][0], dict_obj_order[cur_dict_count][1]]}
				dict_obj_key = {'Space':['Space', dict_obj_order[cur_dict_count][0], 0]}
				counter = 1
			else:
				vars()[event_name] = key(event_name, hold, releasedn)
				key_list.append(vars()[event_name])


			






