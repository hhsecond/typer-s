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

import threading, time, os, mntree_struct
from settings import *

dicti = mntree_struct.mntree()

class key:
	"""docstring for key - this class is for creating  object with 2 attributes which we are accounting for a key"""
	def __init__(self, name, hold, releasedn):
		#super(key, self).__init__() ------------------- what is this doing?
		self.hold = hold #hold time for a key : (key up time - key down time)
		self.releasedn = releasedn # duration between each key strokes: (previous key down time - current key down time)
		self.name = name #key name in character rather string format:  for readability



def dict_from_file():
	global key_dict, data_to_config, dicti
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
			dicti.enter(key_dict)
			key_dict.clear()
	with open('typer-s\\typer.config', 'r+') as f:
		data_to_config.clear()
		for line in f:
			line = line.split(':', 1)
			data_to_config[str(line[0])] = float(line[1])
	dicti.testprint()
	try:
		avg_time_params.append(data_to_config['average_hold_time'])
		avg_time_params.append(data_to_config['average_release_time'])
	except:
		print('exception raised while reading config file')





def bspacing():
	global prev_key, counter, dict_counter, dict_time_args, key_dict
	print(key_dict)
	if key_dict:
		del dict_counter[prev_key.pop()]
		del dict_time_args[counter]
		del key_dict[counter]
		counter -= 1
	



#Sample codes starts here with test inputs and printing fucntion - can be used for debugging


if __name__ == '__main__':
	print('dont know what to say')