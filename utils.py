import os
import json
from datetime import date as py_date

def json_file_to_object(path):
	""" read a json file from path and convert it to a python dictionary """
	obj=None
	with open(path) as jf:
		obj=json.load(jf)
	return obj

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
	
def get_settings():
	return json_file_to_object("settings.json")

def init_directories():
	""" initialize the directories mentioned in settings.json """
	settings=get_settings()
	os.makedirs(settings['data_dir'], exist_ok=True)
	os.makedirs(settings['reports_dir'], exist_ok=True)
