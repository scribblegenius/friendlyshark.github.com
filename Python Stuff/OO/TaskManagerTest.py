from Task import Task
from TaskManager import TaskManager
from UrgentTask import UrgentTask
from ImportantTask import ImportantTask
class TaskManagerTest:
	pass
def main():
	tm = TaskManager("A")
	tm.addTask(Task("Buy milk","Trivial","Done"))
	tm.addTask(UrgentTask("Pay rent","Done"))
	tm.addTask(ImportantTask("Learn Python Classes","Pending"))
	print tm
	tm.delTask(1)
	print tm
	tm.DoTask(2)
	print tm
if __name__ == "__main__":
	main()