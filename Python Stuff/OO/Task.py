class Task(object):
	def __init__(self,title=None,priority=None,status="Pending"):
		self.title = title
		self.priority = priority
		self.status = status
	
	def __str__(self):
		return str("Task: " + self.title + ", Priority: " + self.priority + ", Status: " + self.status)
