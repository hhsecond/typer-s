import time
def first():
	print('first called')
	time.sleep(5)
	print('first sleep completed')

def second():
	print('second called')
	first()
	print('checking the time from second')

second()
print('third instance')