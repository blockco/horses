import os

def child():
	while True:
		print ("hello")

def parent():
   while True:
      newpid = os.fork()
      if newpid == 0:
         child()

parent()
