from utils import print_task
from db import db_get,db_put,db_set_done,db_empty,db_del

# THIS IS THE SERVICE LAYER

def tasks_print_today(conn):
	for row in db_get(conn,today=True):
		print_task(row,False)
	else:
		print("no tasks set for today yet")

def task_put(conn,title,descr="",done=False,date=None,weight=0):
	db_put(conn,title,descr,done,date,weight)

def task_set_done(conn,title):
	db_set_done(conn,title)

def tasks_empty(conn):
	db_empty(conn)

def task_del(conn,title):
	db_del(conn,title)
