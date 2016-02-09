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

import threading

class key:
	"""docstring for key - this class is for creating  object with 2 attributes which we are accounting for a key"""
	def __init__(self, name, hold, release):
		#super(key, self).__init__() ------------------- what is this doing?
		self.hold = hold #hold time for a key : (key up time - key down time)
		self.release = release # duration between each key strokes: (previous key up time - current key down time)
		self.name = name #key name in character rather string format:  for readability
		

class objthread(threading.Thread):
	"""docstring for objthread - thread module calling by keystroke for creating object and adding each object to tree"""
	def __init__(self, event_name, event_window, event_time, status):
		threading.Thread.__init__(self)
		#print(event_name, event_window, event_time, status)



dicti = {}
#trial_dict = {'a':{'b':{'c':{'d':{}}, 'e':{}}}} - Trial dictionary: datastructure will look like this if the words added are "abcd" and "abe"
dict_obj_order = {}
dict_obj_key = {}
counter = 1

#function creates dictionary which will accept a word at a time as a list of characters
def dict_create(key_list, dictionary):
	for key_val in key_list: #fetching each key and sending to the dict create function
		dictionary = key_to_dict1(key_val, dictionary) #returning dictionary recursively

def key_to_dict2(key_val, dictionary):
	#beta version of a function which is believed to be faster than the current function
	dictionary.setdefault(key_val, {})
	for key in dictionary:
		if key == key_val:
			pass#print('key is', key.name)
	return dictionary[key_val]

def key_to_dict1(key_val, dictionary):
	#function which is currently executing does not have other dictionary functions. kind of funcitonal programming
	check = 0
	for key in dictionary:
		if key.name == key_val.name:
			check = 1
			key.hold = (key.hold + key_val.hold)/2
			key.release = (key.release + key_val.release)/2
			return dictionary[key]
	if not check:
		dictionary[key_val] = {}	
		return dictionary[key_val]



#Sample codes starts here with test inputs and printing fucntion - can be used for debugging
def dict_print(dictionary):
	for key, value in dictionary.items():
		print(key.name, " : ", key.hold, " : ", key.release)
		if value:
			dict_print(value)


def obj_create(event_name, event_window, event_time, status):
	global dict_obj_order, dict_obj_key, counter
	if status == 1:
		#fetching second and millisecond from the time
		etime =	event_time.timestamp()
		#print(event_name,	etime, event_status, counter)
		#two dictionaries: one for storing current values another for finding previous value
		dict_obj_key[event_name] = [event_name,	etime, counter]
		#print('dict_obj_key', dict_obj_key)
		dict_obj_order[counter] = etime
		#print('dict_obj_order', dict_obj_order)
		counter += 1

	else:
		#fetching second and millisecond from the time
		etime =	event_time.timestamp()
		#print('key up', event_name,	etime)
		lis = dict_obj_key.pop(event_name)
		#print('lis',lis)
		prev_dict_key = lis[2] - 1
		#print('prev_dict_key',prev_dict_key)
		prev_time = dict_obj_order[prev_dict_key]
		#print('previous key time', prev_time)
		#print(event_name, etime, lis[1], prev_time)
		vars()[event_name] = key(event_name, (etime - lis[1]), (lis[1] - prev_time))




if __name__ == '__main__':
	a = key('a', 1, 1)
	b = key('b', 2, 2)
	c = key('c', 3, 3)
	d = key('d', 4, 4)
	e = key('e', 5, 5)
	f = key('f', 6, 6)
	#word1 = ['a', 'b', 'c', 'd']
	word1 = [a, b, c, d]
	dict_create(word1, dicti)

	a = key('a', 10, 10)
	b = key('b', 20, 20)
	c = key('c', 30, 30)
	d = key('d', 40, 40)
	e = key('e', 50, 50)
	f = key('f', 60, 60)
	#word2 = ['a', 'b', 'e']
	word2 = [a, b, e]
	dict_create(word2, dicti)


	dict_print(dicti)
