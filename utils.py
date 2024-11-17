import os
from datetime import date as py_date

def mk_file(path):
	""" make a file if it doesn't exist """

	if not os.path.exists(path):
		os.mknod(path)

def get_today_str():
	return py_date.today().strftime("%Y-%m-%d")

def print_task(task,print_descr=True):
	""" task:=(title,descr,done,date,weight) """

	is_done="[ ]"
	if task[2]:
		is_done="[x]"
	print("{} {} ({})".format(is_done,task[0],task[3]))
	if print_descr:
		print("'{}'".format(task[1]))
