from Task import Task
from UrgentTask import UrgentTask
from ImportantTask import ImportantTask
class TaskManager(object):
	TaskList = []
	def __init__(self,name):
		self.name = name
		print "Task Manager " + self.name + " Started"

	def addTask(self,task):
		self.TaskList.append(task)
		print " Added " +  str(task) + ", to Task Manager " + self.name

	def __str__(self):
		print " Printing Task List in Task Manager " + self.name
		return ("\n".join( "	" + str(x+1) + " " +  str(y) for x,y in enumerate(self.TaskList)))

	def delTask(self,number):
		print " Deleted " + str(self.TaskList[number-1]) + ", from Task Manager " + self.name
		del self.TaskList[number-1]

	def DoTask(self,number):
		self.TaskList[number-1].status="Done"
		print " Status of Task \"" + str(self.TaskList[number-1].title) + "\" changed to Done"

