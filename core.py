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
key_list = []


class key:
	"""docstring for key - this class is for creating  object with 2 attributes which we are accounting for a key"""
	def __init__(self, name, hold, releasedn):
		#super(key, self).__init__() ------------------- what is this doing?
		self.hold = hold #hold time for a key : (key up time - key down time)
		self.releasedn = releasedn # duration between each key strokes: (previous key down time - current key down time)
		self.name = name #key name in character rather string format:  for readability


#function creates dictionary which will accept a word at a time as a list of characters
#dictionary = dicti, fetching the main dictionary if no dictionary specified in the function call
def dict_create(key_list, dictionary = dicti):
	#fetching each key and sending to the dict create function
	for key_val in key_list:
		dictionary = key_to_dict(key_val, dictionary) #returning dictionary recursively


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



class objthread(threading.Thread):
	"""docstring for objthread - handling threads which is creating by each and every event from typer-s"""
	def __init__(self, event_name, event_window, event_time, event_status):
		threading.Thread.__init__(self)
		self.start()
		etime = event_time.timestamp()
		global counter

		if event_status == 1:
			counter += 1
			print(dict_counter)
			#how the script is printing dict_counter without declaring the value inside? its not a global variable
			dict_counter[event_name] = counter
			dict_time_args[counter] = [etime]
		else:
			curr_count = dict_counter[event_name]
			dict_time_args[curr_count].append(etime)


		



		



#Sample codes starts here with test inputs and printing fucntion - can be used for debugging
def dict_print(dictionary):
	for key, value in dictionary.items():
		print(key.name, " : ", key.hold, " : ", key.releasedn)
		if value:
			dict_print(value)



if __name__ == '__main__':
	from datetime import datetime
	
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:18:42.750011', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:18:42.796885', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:18:42.906262', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:18:42.984389', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:18:43.046889', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:18:43.140638', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('Escape', 'cmd.exe', datetime.strptime('2016-02-12 15:18:43.625020', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('Escape', 'cmd.exe', datetime.strptime('2016-02-12 15:18:43.750022', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('Escape', 'cmd.exe', datetime.strptime('2016-02-12 15:18:46.256002', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('Escape', 'cmd.exe', datetime.strptime('2016-02-12 15:18:46.412238', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:23.097165', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:23.206544', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:23.487794', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:23.581547', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('E', 'cmd.exe', datetime.strptime('2016-02-12 15:19:23.909676', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('E', 'cmd.exe', datetime.strptime('2016-02-12 15:19:24.034676', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('R', 'cmd.exe', datetime.strptime('2016-02-12 15:19:24.378394', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('R', 'cmd.exe', datetime.strptime('2016-02-12 15:19:24.503375', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:24.789287', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:24.898725', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:25.242471', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:25.351853', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:26.101857', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:26.242483', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('C', 'cmd.exe', datetime.strptime('2016-02-12 15:19:26.554981', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('C', 'cmd.exe', datetime.strptime('2016-02-12 15:19:26.664366', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:26.929992', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:27.039367', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('A', 'cmd.exe', datetime.strptime('2016-02-12 15:19:27.304995', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('A', 'cmd.exe', datetime.strptime('2016-02-12 15:19:27.461247', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('C', 'cmd.exe', datetime.strptime('2016-02-12 15:19:27.762813', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('C', 'cmd.exe', datetime.strptime('2016-02-12 15:19:27.887822', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('K', 'cmd.exe', datetime.strptime('2016-02-12 15:19:28.200321', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('K', 'cmd.exe', datetime.strptime('2016-02-12 15:19:28.294072', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('O', 'cmd.exe', datetime.strptime('2016-02-12 15:19:28.633682', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('O', 'cmd.exe', datetime.strptime('2016-02-12 15:19:28.711867', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:29.088536', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:29.213588', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('T', 'cmd.exe', datetime.strptime('2016-02-12 15:19:29.541716', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('T', 'cmd.exe', datetime.strptime('2016-02-12 15:19:29.651093', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:29.947974', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:30.041725', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('O', 'cmd.exe', datetime.strptime('2016-02-12 15:19:30.494853', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('O', 'cmd.exe', datetime.strptime('2016-02-12 15:19:30.604230', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('M', 'cmd.exe', datetime.strptime('2016-02-12 15:19:30.901106', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('M', 'cmd.exe', datetime.strptime('2016-02-12 15:19:31.026116', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('A', 'cmd.exe', datetime.strptime('2016-02-12 15:19:31.244862', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('A', 'cmd.exe', datetime.strptime('2016-02-12 15:19:31.385489', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:31.729243', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:31.854251', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:32.604252', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:32.739848', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('M', 'cmd.exe', datetime.strptime('2016-02-12 15:19:33.083603', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('M', 'cmd.exe', datetime.strptime('2016-02-12 15:19:33.192990', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('E', 'cmd.exe', datetime.strptime('2016-02-12 15:19:33.489811', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('E', 'cmd.exe', datetime.strptime('2016-02-12 15:19:33.599234', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('R', 'cmd.exe', datetime.strptime('2016-02-12 15:19:33.880490', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('R', 'cmd.exe', datetime.strptime('2016-02-12 15:19:33.989865', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:34.302369', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:34.411746', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:34.692997', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:34.818009', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:35.161753', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:35.302380', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:35.614884', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:35.724260', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:36.052389', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:36.166664', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:37.095054', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:37.204428', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('M', 'cmd.exe', datetime.strptime('2016-02-12 15:19:37.548182', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('M', 'cmd.exe', datetime.strptime('2016-02-12 15:19:37.688808', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:37.965571', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:38.106200', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:38.403077', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:38.528082', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:38.856179', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('Space', 'cmd.exe', datetime.strptime('2016-02-12 15:19:38.996834', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:39.278092', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', datetime.strptime('2016-02-12 15:19:39.371838', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:39.715592', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('H', 'cmd.exe', datetime.strptime('2016-02-12 15:19:39.824968', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:40.106221', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('I', 'cmd.exe', datetime.strptime('2016-02-12 15:19:40.215598', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:40.496851', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('N', 'cmd.exe', datetime.strptime('2016-02-12 15:19:40.606228', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('J', 'cmd.exe', datetime.strptime('2016-02-12 15:19:40.924614', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('J', 'cmd.exe', datetime.strptime('2016-02-12 15:19:41.018358', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('O', 'cmd.exe', datetime.strptime('2016-02-12 15:19:41.393364', '%Y-%m-%d %H:%M:%S.%f'), 1)
	with threading.Lock():
		objthread('O', 'cmd.exe', datetime.strptime('2016-02-12 15:19:41.502741', '%Y-%m-%d %H:%M:%S.%f'), 0)
	with threading.Lock():
		objthread('Escape', 'cmd.exe', datetime.strptime('2016-02-12 15:19:43.891825', '%Y-%m-%d %H:%M:%S.%f'), 1)
	dict_print(dicti)
