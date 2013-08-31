class Task(object):
	def __init__(self,title=None,status="Pending",priority=None):
		if( isinstance(title,str)):
			self.title = title
		else:
			print "Title should be a string...unable to add Task"
			self.title = None
		if( isinstance(status,str)):
			self.status = status
		else:
			self.status="Pending"
			print "Status should be a string"
		if( isinstance(priority,str)):
			self.priority = priority
		else:
			self.priority=None
			print "Priority should be a string"
	
	def __str__(self):
		return str("Task: " + str(self.title) + ", Priority: " + str(self.priority) + ", Status: " + str(self.status))

	def do(self):
		self.status="Done"
class UrgentTask(Task):
	def __init__(self,title=None,status="Pending",priority="Urgent"):
		super(UrgentTask,self).__init__(title=title,status = status,priority = priority)

class ImportantTask(Task):
	def __init__(self,title=None,status="Pending",priority="Important"):
		super(ImportantTask,self).__init__(title=title,status = status,priority = priority)