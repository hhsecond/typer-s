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
from main_core import *


class check_key:
	"""docstring for check_key - using for comapring old user with user in the database"""
	def __init__(self):
		self.score = 0
		

def comparer(a, b):
	ret = (1-(min(a, b)/max(a, b)))
	return (ret ** 2)



def dict_check(key_dict, dictionary = dicti):
	key_key = sorted(key_dict) #returns sorted key from dictionary as a list
	for key_key in key_key:
		print('********************', key_dict[key_key])
		dictionary = key_in_dict(key_dict[key_key], dictionary) #returning dictionary recursively


def key_in_dict(key_val, dictionary):
	global key_dict, score
	for key in dictionary:
		if key.name == key_val['name']:
			if key_val['hold'] != 0 and key.hold != 0:
				score.append(comparer(key_val['hold'], key.hold))
			if key_val['releasedn'] != 0 and key.releasedn != 0:
				score.append(comparer(key_val['releasedn'], key.releasedn))
			return dictionary[key]
	return {} 



class checkdb(threading.Thread):
    """docstring for writethread - its for writing the file at each one minute"""
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
    def run(self):
    	global score
    	while 1:
	    	#print(score)
	    	sap_counter = 0
	    	totscore = 0
	    	time.sleep(30)
	    	for sap in score:
	    		sap_counter += 1
	    		totscore += sap
	    	if sap_counter:
		    	avgscore = totscore/sap_counter
		    	print('average socre you have: ', avgscore)




class objthread_down(threading.Thread):
	"""docstring for objthread - handling threads which is creating by key down event from typer-s"""
	def __init__(self, event_name, event_window, event_time):
		threading.Thread.__init__(self)
		self.event_name = event_name
		self.event_window = event_window
		self.event_time = event_time
		self.start()
	def run(self):
		global prev_key, dict_counter, counter, dict_time_args
		if self.event_name != 'Back':
			prev_key.append(self.event_name)
			etime = self.event_time.timestamp()
			counter += 1
			dict_counter[self.event_name] = counter
			#print('do', counter, event_name)
			dict_time_args[counter] = [etime]
		else:
			bspacing()


attr_dict = {}
class objthread_up(threading.Thread):
	"""docstring for objthread - handling threads which is creating by key up event from typer-s"""
	def __init__(self, event_name, event_window, event_time):
		#print(event_name)
		threading.Thread.__init__(self)
		self.event_name = event_name
		self.event_window = event_window
		self.event_time = event_time
		self.start()
	def run(self):
		if self.event_name != 'Back':
			global avg_time_params, key_dict, dict_counter, dict_time_args, counter, attr_dict
			etime = self.event_time.timestamp()
			curr_count = dict_counter[self.event_name]
			#print('up', curr_count, event_name)
			dict_time_args[curr_count].append(etime)#for refering previous up time (not using now, for futureq)

			curr_hold = etime - dict_time_args[curr_count][0]#curr_up_time - curr_down_time
			if dict_time_args[curr_count - 1][0]:
				curr_releasedn = dict_time_args[curr_count][0] - dict_time_args[curr_count - 1][0]#curr_down_time - prev_down_time
			else:
				curr_releasedn = 0.0
			#vars()[self.event_name] = key(self.event_name, curr_hold, curr_releasedn)
			#instead of creating var like in lcore, we are passing list
			attr_dict['name'] = self.event_name
			attr_dict['hold'] = curr_hold
			attr_dict['releasedn'] = curr_releasedn
			key_dict[curr_count] = attr_dict

			if self.event_name == 'Space':
				dict_check(key_dict)
				key_dict = {}



		



#Sample codes starts here with test inputs and printing fucntion - can be used for debugging


if __name__ == '__main__':
	print('is this required here')