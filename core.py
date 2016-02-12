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

			#handling cases with releasedn value is zero
			if key.releasedn == 0.0:
				print('0.0 --  but already in dicti', key.name)
				key.releasedn = key_val.releasedn
				return dictionary[key]
			if key_val.releasedn == 0.0:
				print('0.0 --  adding to dicti', key.name)
				return dictionary[key]				
			else:
				print('both has value', key.name,key.releasedn, key_val.releasedn, (key.releasedn + key_val.releasedn)/2)
				key.releasedn = (key.releasedn + key_val.releasedn)/2
				return dictionary[key]
			print('same', key.name, key.releasedn)
	print('different', key_val.name, key_val.releasedn)
	dictionary[key_val] = {}	
	return dictionary[key_val]



#Sample codes starts here with test inputs and printing fucntion - can be used for debugging
def dict_print(dictionary):
	for key, value in dictionary.items():
		print(key.name, " : ", key.hold, " : ", key.releasedn)
		if value:
			dict_print(value)



if __name__ == '__main__':
	s = key('s', 0.001591, 0.0)
	h = key('h', 0.002591, 0.003591)
	e = key('e', 0.003591, 0.004591)
	r = key('r', 0.004591, 0.005591)
	i = key('i', 0.005591, 0.006591)
	n = key('n', 0.006591, 0.007591)
	Space = key('Space', 0.007591, 0.008591)
	word1 = [s, h, e, r, i, n]
	dict_create(word1)


	m = key('m', 0.001591, 0.0)
	e = key('e', 0.002591, 0.003591)
	r = key('r', 0.003591, 0.004591)
	i = key('i', 0.004591, 0.005591)
	n = key('n', 0.005591, 0.006591)
	Space = key('Space', 0.006591, 0.007591)
	word1 = [m, e, r, i, n]
	dict_create(word1)


	s = key('s', 0.001591, 0.002591)
	h = key('h', 0.002591, 0.003591)
	e = key('e', 0.003591, 0.004591)
	m = key('m', 0.004591, 0.005591)
	i = key('i', 0.005591, 0.006591)
	n = key('n', 0.006591, 0.007591)
	Space = key('Space', 0.007591, 0.008591)
	word1 = [s, h, e, m, i, n]
	dict_create(word1)

	s = key('s', 0.001591, 0.002591)
	h = key('h', 0.002591, 0.0)
	i = key('i', 0.002591, 0.003591)
	j = key('j', 0.003591, 0.004591)
	o = key('o', 0.004591, 0.005591)
	Space = key('Space', 0.005591, 0.006591)
	n = key('n', 0.006591, 0.007591)
	word1 = [s, h, i, j, o]
	dict_create(word1)

#1455091742.100591
	dict_print(dicti)
