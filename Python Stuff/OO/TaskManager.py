from Task import *
class TaskManager(object):
	# declaring tasklist here would make it static D:
	def __init__(self,name):
		self.tasklist = []
		self.name = name
		print "Task Manager {0} Started".format(self.name)

	def add_task(self,task):
		self.tasklist.append(task)
		print " Added {0}, to Task Manager {1} ".format(str(task), self.name)

	def __str__(self):
		print " Printing Task List in Task Manager " + self.name
		return ("\n".join( "	" + str(x+1) + " " +  str(y) for x,y in enumerate(self.tasklist)))

	def del_task(self,number):
		if ( self.size() >= number ):
			print " Deleted {0} from Task Manager {1}".format(str(self.tasklist[number-1]),self.name)
			del self.tasklist[number-1]
		else:
			print " Task number {0} does not exist! ".format(number)

	def do_task(self,number):
		self.tasklist[number-1].do()
		print ' Status of Task "{0}" changed to Done'.format(str(self.tasklist[number-1].title))

	def size(self):
		return len(self.tasklist)

