from Task import Task
class ImportantTask(Task):
	priority="Important"

	def __init__(self,title=None,status="Pending"):
		self.title = title
		self.status = status