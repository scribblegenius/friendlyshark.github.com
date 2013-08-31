from Task import *
class TaskManager(object):
	# declaring tasklist here would make it static D:
	def __init__(self,name):
		self.tasklist = []
		self.name = name
		print "Task Manager {0} Started".format(self.name)

	def add_task(self,task):
		add = True
		for t in self.tasklist:
			if t.title.upper().strip() == task.title.upper().strip():
				add = False
				break
		if add:
			self.tasklist.append(task)
			print " Added {0}, to Task Manager {1} ".format(str(task), self.name)
		else:
			print ' Tried to add "{0}", however this task already exists! Unable to add duplicate Task!'.format(task.title)

	def __str__(self):
		print " Printing Task List in Task Manager " + self.name
		return ("\n".join( "	" + str(x+1) + " " +  str(y) for x,y in enumerate(self.tasklist)))

	def del_task(self,number):
		if ( self.size() >= number ):
			print " Deleted {0} from Task Manager {1}".format(str(self.tasklist[number-1]),self.name)
			del self.tasklist[number-1]
		else:
			print " Attempted deleting Task number {0} which does not exist!Attempt foiled! ".format(number)

	def do_task(self,number):
		self.tasklist[number-1].do()
		print ' Status of Task "{0}" changed to Done'.format(str(self.tasklist[number-1].title))

	def size(self):
		return len(self.tasklist)

