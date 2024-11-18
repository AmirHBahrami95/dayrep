from utils import print_task,get_today_str,get_settings
from db import db_get,db_put,db_set_done,db_empty,db_del
from doc import docx_export
import os

# THIS IS THE SERVICE LAYER

def tasks_print_today(conn):
	rowses=db_get(conn,today=True)
	if not rowses or len(rowses)<=0:
		print("no tasks set for today yet")
	for row in rowses:
		print_task(row,False)

def task_put(conn,title,descr="",done=False,date=None,weight=0):
	db_put(conn,title,descr,done,date,weight)

def task_set_done(conn,title):
	db_set_done(conn,title)

def tasks_empty(conn):
	db_empty(conn)

def task_del(conn,title):
	db_del(conn,title)

def tasks_export(conn):
	rows=db_get(conn)
	if not docx_export(rows):
		print("aborting...")
	else:
		print("wrote to {}{}{}.docx".format(
			get_settings()['reports_dir'],
			os.sep,
			get_today_str(),
		))
	
