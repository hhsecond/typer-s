###############################################################################################################################
## This file contains the class for each key object and core funcitons for defining the datastructure used in thsi program   ##
## datastructure is a tree like structure in which the parent node will be the space key and each node will have 52 leaf     ##
## nodes. This 52 can be defined 26 captial letters and 26 small letters of english alphabet                                 ##
## The object creation function is accepting values from front end and creat the object which is storing in the              ##
## datastructure.                                                                                                            ##
##                                                   Author: hhsecond                                                        ##
##                                          Github: github.com/hhsecond/typer-s                                              ##
##                                                   date: 1/30/2016                                                         ##
###############################################################################################################################

import threading, time


dicti = {}
#trial_dict = {'a':{'b':{'c':{'d':{}}, 'e':{}}}} - Trial dictionary: datastructure will look like this if the words added are "abcd" and "abe"
dict_time_args = {0:[0.0, 0.0]}
dict_counter = {'Space':0}
counter = 0
data_to_file = ''
data_to_out = ''
key_dict = {}


class key:
	"""docstring for key - this class is for creating  object with 2 attributes which we are accounting for a key"""
	def __init__(self, name, hold, releasedn):
		#super(key, self).__init__() ------------------- what is this doing?
		self.hold = hold #hold time for a key : (key up time - key down time)
		self.releasedn = releasedn # duration between each key strokes: (previous key down time - current key down time)
		self.name = name #key name in character rather string format:  for readability

#function for writing the dictionary to file
def dict_write(dictionary = dicti):
	global data_to_file
	global data_to_out
	if dictionary.keys():
		curr_val = list(dictionary)[0]
		#print(curr_val.name, curr_val.hold, curr_val.releasedn)
		data_to_file += curr_val.name + ':' + str(curr_val.hold) + ':' + str(curr_val.releasedn) + ' '
		if not curr_val.name == 'Space':
			data_to_out += curr_val.name
		#print(curr_val.name)
		if not dict_write(dictionary[curr_val]):
			del dictionary[curr_val]
			if dictionary.keys():
				return True
			else:
				return False
		return True
	return False



def dict_from_file():
	with open('typerstree.txt', 'r') as f:
		for word in f:
			letters = word.split()
			for letter in letters:
				attributes = letter.split(':')
				print(attributes[0])



#function creates dictionary which will accept a word at a time as a list of characters
#dictionary = dicti, fetching the main dictionary if no dictionary specified in the function call
def dict_create(key_dict, dictionary = dicti):
	#fetching each key and sending to the dict create function
	key_key = sorted(key_dict)
	for key_key in key_key:
		#print(key_val.name)
		dictionary = key_to_dict(key_dict[key_key], dictionary) #returning dictionary recursively




def key_to_dict(key_val, dictionary):
	#function which is currently executing does not have other dictionary functions. kind of funcitonal programming
	for key in dictionary:
		if key.name == key_val.name:			
			key.hold = (key.hold + key_val.hold)/2

			#handling cases with zero releasedn value 
			if key.releasedn == 0.0:
				key.releasedn = key_val.releasedn
				return dictionary[key]
			elif key_val.releasedn == 0.0:
				return dictionary[key]				
			else:
				key.releasedn = (key.releasedn + key_val.releasedn)/2
				return dictionary[key]
	dictionary[key_val] = {}	
	return dictionary[key_val]



class objthread_down(threading.Thread):
	"""docstring for objthread - handling threads which is creating by key down event from typer-s"""
	def __init__(self, event_name, event_window, event_time):
		#print(event_name)
		threading.Thread.__init__(self)
		self.start()
		global data_to_file
		global data_to_out
		if event_name == 'Escape':
			while dicti.keys():
				dict_write()
				data_to_file += '\n'
				data_to_out += '\n'
			with open('typerstree.txt', 'w+') as f:
				f.write(data_to_file)
				f.close()
				data_to_file = ''
				print(data_to_out)
				data_to_out = ''
			exit()
		etime = event_time.timestamp()
		global counter

		counter += 1
		dict_counter[event_name] = counter
		#print('do', counter, event_name)
		dict_time_args[counter] = [etime]



class objthread_up(threading.Thread):
	"""docstring for objthread - handling threads which is creating by key up event from typer-s"""
	def __init__(self, event_name, event_window, event_time):
		#print(event_name)
		threading.Thread.__init__(self)
		self.start()
		etime = event_time.timestamp()
		global key_dict


		curr_count = dict_counter[event_name]
		#print('up', curr_count, event_name)
		dict_time_args[curr_count].append(etime)

		curr_hold = etime - dict_time_args[curr_count][0]#curr_up_time - curr_down_time
		if dict_time_args[curr_count - 1][0]:
			curr_releasedn = dict_time_args[curr_count][0] - dict_time_args[curr_count - 1][0]#curr_down_time - prev_down_time
		else:
			curr_releasedn = 0.0
		#print(event_name, curr_hold, curr_releasedn)
		vars()[event_name] = key(event_name, curr_hold, curr_releasedn)
		key_dict[curr_count] = vars()[event_name]

		if event_name == 'Space':
			dict_create(key_dict)
			key_dict = {}






		



		



#Sample codes starts here with test inputs and printing fucntion - can be used for debugging


if __name__ == '__main__':
	from datetime import datetime


	
	with threading.Lock():
		objthread_down('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:23.097165', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_down('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:23.487794', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:23.581547', '%Y-%m-%d %H:%M:%S.%f'))	
	with threading.Lock():
		objthread_up('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:23.206544', '%Y-%m-%d %H:%M:%S.%f'))


	with threading.Lock():
		objthread_down('E', 'cmd.exe', datetime.strptime('2016-02-12 15:19:23.909676', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('E', 'cmd.exe', datetime.strptime('2016-02-12 15:19:24.034676', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('R', 'cmd.exe', datetime.strptime('2016-02-12 15:19:24.378394', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('R', 'cmd.exe', datetime.strptime('2016-02-12 15:19:24.503375', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:24.789287', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:24.898725', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:25.242471', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:25.351853', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:26.101857', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:26.242483', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('C', 'cmd.exe', datetime.strptime('2016-02-12 15:19:26.554981', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('C', 'cmd.exe', datetime.strptime('2016-02-12 15:19:26.664366', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:26.929992', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:27.039367', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('A', 'cmd.exe', datetime.strptime('2016-02-12 15:19:27.304995', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('A', 'cmd.exe', datetime.strptime('2016-02-12 15:19:27.461247', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('C', 'cmd.exe', datetime.strptime('2016-02-12 15:19:27.762813', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('C', 'cmd.exe', datetime.strptime('2016-02-12 15:19:27.887822', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('K', 'cmd.exe', datetime.strptime('2016-02-12 15:19:28.200321', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('K', 'cmd.exe', datetime.strptime('2016-02-12 15:19:28.294072', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('O', 'cmd.exe', datetime.strptime('2016-02-12 15:19:28.633682', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('O', 'cmd.exe', datetime.strptime('2016-02-12 15:19:28.711867', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:29.088536', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:29.213588', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('T', 'cmd.exe', datetime.strptime('2016-02-12 15:19:29.541716', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('T', 'cmd.exe', datetime.strptime('2016-02-12 15:19:29.651093', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:29.947974', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:30.041725', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('O', 'cmd.exe', datetime.strptime('2016-02-12 15:19:30.494853', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('O', 'cmd.exe', datetime.strptime('2016-02-12 15:19:30.604230', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('M', 'cmd.exe', datetime.strptime('2016-02-12 15:19:30.901106', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('M', 'cmd.exe', datetime.strptime('2016-02-12 15:19:31.026116', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('A', 'cmd.exe', datetime.strptime('2016-02-12 15:19:31.244862', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('A', 'cmd.exe', datetime.strptime('2016-02-12 15:19:31.385489', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:31.729243', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:31.854251', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:32.604252', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:32.739848', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('M', 'cmd.exe', datetime.strptime('2016-02-12 15:19:33.083603', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('M', 'cmd.exe', datetime.strptime('2016-02-12 15:19:33.192990', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('E', 'cmd.exe', datetime.strptime('2016-02-12 15:19:33.489811', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('E', 'cmd.exe', datetime.strptime('2016-02-12 15:19:33.599234', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('R', 'cmd.exe', datetime.strptime('2016-02-12 15:19:33.880490', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('R', 'cmd.exe', datetime.strptime('2016-02-12 15:19:33.989865', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:34.302369', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:34.411746', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:34.692997', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:34.818009', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:35.161753', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:35.302380', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:35.614884', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:35.724260', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:36.052389', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:36.166664', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:37.095054', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:37.204428', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('M', 'cmd.exe', datetime.strptime('2016-02-12 15:19:37.548182', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('M', 'cmd.exe', datetime.strptime('2016-02-12 15:19:37.688808', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:37.965571', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:38.106200', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:38.403077', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:38.528082', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:38.856179', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:38.996834', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:39.278092', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:39.371838', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:39.715592', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:39.824968', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:40.106221', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:40.215598', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:40.496851', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:40.606228', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('J', 'cmd.exe', datetime.strptime('2016-02-12 15:19:40.924614', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('J', 'cmd.exe', datetime.strptime('2016-02-12 15:19:41.018358', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('O', 'cmd.exe', datetime.strptime('2016-02-12 15:19:41.393364', '%Y-%m-%d %H:%M:%S.%f'))#this is down
	with threading.Lock():
		objthread_up('O', 'cmd.exe', datetime.strptime('2016-02-12 15:19:41.502741', '%Y-%m-%d %H:%M:%S.%f'))
	with threading.Lock():
		objthread_down('Escape', 'cmd.exe', datetime.strptime('2016-02-12 15:19:43.891825', '%Y-%m-%d %H:%M:%S.%f'))#this is down
		print('test')
	print('testing')
	dict_print(dicti)
