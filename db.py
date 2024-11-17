from os.path import exists as file_exists
from utils import mk_file, get_today_str
import sqlite3

def __db_init_table(conn):	
	cur=None
	if not conn==None:
		cur=conn.cursor()
		try:
			cur.execute(
				"""CREATE TABLE IF NOT EXISTS task(
					title TEXT NOT NULL,
					descr TEXT DEFAULT NULL,
					done INTEGER DEFAULT 0,
					date TEXT NOT NULL,
					weight INTEGER DEFAULT 0
				)"""
			)
		except e:
			print("error encontered while initializing table")
			print(e)

def db_init(path):
	""" makes a connection to the path .db file (makes one if it doesn't exist) and returns the connection.
		XXX do not forget to close it XXX """

	if not path.endswith(".db"):
		print("invalid path!")
		return None
	conn=None
	if not file_exists(path):
		mk_file(path)
	try:
		conn=sqlite3.connect(path)
	except e:
		print(e)
	__db_init_table(conn)
	return conn

def db_put(conn,title,descr="",done=False,date=None,weight=0):
	""" only title is required and date is yyyy-mm-dd format. duplicate row's are not removed in database! """

	if date==None:
		date=get_today_str()
	done=int(done)
	cur=conn.cursor()
	cur.executemany(
		"INSERT INTO task(title,descr,done,date,weight) VALUES(?,?,?,?,?)",
		[(title,descr,done,date,weight)]
	)
	conn.commit()

def db_get(conn,today=False):
	cur=conn.cursor()
	st="SELECT * FROM task"
	if today:
		st=st+" WHERE date='{}'".format(get_today_str())
	cur.execute(st)
	return cur.fetchall()	

def db_set_done(conn,title):
	cur=conn.cursor()
	st="UPDATE task SET done=1 WHERE title=?"
	cur.execute(st,(title,))
	conn.commit()

def db_empty(conn):
	cur=conn.cursor()
	cur.execute("DELETE FROM task")
	conn.commit()

def db_del(conn,title):
	cur=conn.cursor()
	st="DELETE FROM task WHERE title=?"
	cur.execute(st,(title,))
	conn.commit()
