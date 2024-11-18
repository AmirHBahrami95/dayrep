from db import db_init,db_put,db_get
from utils import init_directories,get_settings
import service as ser
import argparse
import os

p=argparse.ArgumentParser(
	prog="dayrep",
	description="program to manage and monitor your daily performance",
	epilog="written by https://github.com/AmirHBahrami95"
)
p.add_argument( "operation", help="add|get|done|del|del_all|export") # mandatory
p.add_argument("-t","--title",nargs="?",metavar="text",default=None,type=str)
p.add_argument("-d","--descr",nargs="?",metavar="text",default='',type=str)
p.add_argument("-o","--done",nargs="?",metavar="0|1",default=0,type=int,choices=[0,1])
# p.add_argument("-w","--weight",nargs="?",deprecated=True) # not supported for now, if u give a shit, implement it yourself :)
args=p.parse_args()

# XXX weird bug: for some reason args.x will be turned into some built-in method :|
title="{}".format(args.title)
descr="{}".format(args.descr)
done=int(args.done)

# check if title is provided for some operations
op=args.operation
if (op=="add" or op=="done" or op=="del") and not args.title:
	print("title is required. aborting...")
	os._exit(1)

# open connection
db_path="{}{}dayrep.db".format(get_settings()['data_dir'],os.sep)
conn=db_init(db_path)

# once before the program begins
init_directories()

# choose operation
if op=="add":
	ser.task_put(conn,title,descr,done)
elif op=="get": # for now, all tasks get printed at once
	ser.tasks_print_today(conn)
elif op=="done":
	ser.task_set_done(conn,title)
elif op=="del":
	ser.task_del(conn,title)
elif op=="del_all":
	ser.tasks_empty(conn)
elif op=="export":
	ser.tasks_export(conn)
else:
	print("operation not valid. aborting...")
	conn.close()
	os._exit(1)

# never forget!
conn.close()
