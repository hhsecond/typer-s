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




class writedb(threading.Thread):
    """docstring for writethread - its for writing the file at each one minute"""
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
    def run(self):
    	global avg_time_params, data_to_config, dicti
    	while 1:
	    	time.sleep(60)
	    	data_to_file = ''
	    	data_out_li = dicti.filewrite()
	    	for words in data_out_li:
	    		for letter in words:
	    			data_to_file += letter.name + ':' + str(letter.hold) +':' + str(letter.releasedn) + ' '
	    		data_to_file += '\n'
	    	with open('typer-s\\typerstree.tss', 'w+') as f:
	    		f.write(data_to_file)
	    		print('data printed')
	    	data_to_config['average_hold_time'] = avg_time_params[0]
	    	data_to_config['average_release_time'] = avg_time_params[1]
	    	with open('typer-s\\typer.config', 'w+') as f:
	    		for key, val in data_to_config.items():
	    			f.write(str(key) + ':' + str(val) + '\n')



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
			counter[0] += 1
			dict_counter[self.event_name] = counter[0]
			#print('do', counter, event_name)
			dict_time_args[counter[0]] = [etime]
		else:
			print(key_dict)
			bspacing()



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
			global avg_time_params, key_dict, dict_counter, dict_time_args, counter, dicti 
			etime = self.event_time.timestamp()
			curr_count = dict_counter[self.event_name]
			#print('up', curr_count, event_name)
			dict_time_args[curr_count].append(etime)#for refering previous up time (not using now, for futureq)

			curr_hold = etime - dict_time_args[curr_count][0]#curr_up_time - curr_down_time
			if dict_time_args[curr_count - 1][0]:
				curr_releasedn = dict_time_args[curr_count][0] - dict_time_args[curr_count - 1][0]#curr_down_time - prev_down_time
			else:
				curr_releasedn = 0.0
			vars()[self.event_name] = key(self.event_name, curr_hold, curr_releasedn)
			key_dict[curr_count] = vars()[self.event_name]
			del vars()[self.event_name]

			if self.event_name == 'Space':
				dicti.enter(key_dict)
				key_dict.clear()




#Sample codes starts here with test inputs and printing fucntion - can be used for debugging


if __name__ == '__main__':
	print('make enough changes in the main file and create the data for this session')