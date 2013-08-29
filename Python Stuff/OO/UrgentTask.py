from Task import Task
class UrgentTask(Task):
	priority="Urgent"

	def __init__(self,title=None,status="Pending"):
		self.title = title
		self.status = status