###############################################################################################################################
## This file contains the class for each key object and core funcitons for defining the datastructure used in thsi program   ##
## datastructure is a tree like structure in which the parent node will be the space key and each node will have 26 leaf     ##
## nodes. This 26 can be defined 26 captial letters and 26 small letters of english alphabet                                 ##
## The object creation function is accepting values from front end and creat the object which stores in the datastructure    ##
## .                                                                                                                         ##
##                                                   Author: hhsecond                                                        ##
##                                          Github: github.com/hhsecond/typer-s                                              ##
##                                                   date: 2/28/2016                                                         ##
###############################################################################################################################

import threading, time
from settings import *
import os


class key:
	"""docstring for key - this class is for creating  object with 2 attributes which we are accounting for a key"""
	def __init__(self, name, hold, releasedn):
		#super(key, self).__init__() ------------------- what is this doing?
		self.hold = hold #hold time for a key : (key up time - key down time)
		self.releasedn = releasedn # duration between each key strokes: (previous key down time - current key down time)
		self.name = name #key name in character rather string format:  for readability



def dict_from_file():
	global key_dict, data_to_config
	with open('typer-s\\typerstree.tss', 'r+') as f:
		for word in f:
			i = 0
			letters = word.split()
			for letter in letters:
				attributes = letter.split(':')
				#print(attributes[0])
				vars()[attributes[0]] = key(attributes[0], float(attributes[1]), float(attributes[2]))
				key_dict[i] = vars()[attributes[0]]
				i += 1
			dict_create(key_dict)
			key_dict = {}
	with open('typer-s\\typer.config', 'r+') as f:
		data_to_config = {}
		for line in f:
			line = line.split(':', 1)
			data_to_config[str(line[0])] = float(line[1])
	try:
		avg_time_params.append(data_to_config['average_hold_time'])
		avg_time_params.append(data_to_config['average_release_time'])
	except:
		print('exception raised while reading config file')


#function creates dictionary which will accept a word at a time as a list of characters
#dictionary = dicti, fetching the main dictionary if no dictionary specified in the function call
def dict_create(key_dict, dictionary = dicti):
	#fetching each key and sending to the dict create function
	key_key = sorted(key_dict) #returns sorted key from dictionary as a list
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


def bspacing():
	global prev_key, counter, dict_counter, dict_time_args
	if key_dict:
		del dict_counter[prev_key.pop()]
		del dict_time_args[counter]
		del key_dict[counter]
		counter -= 1
	



#Sample codes starts here with test inputs and printing fucntion - can be used for debugging


if __name__ == '__main__':
	print('dont know what to say')