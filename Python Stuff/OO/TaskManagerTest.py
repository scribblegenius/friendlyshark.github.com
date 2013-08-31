import random
import unittest
from Task import *
from TaskManager import TaskManager
class TaskManagerTest(unittest.TestCase):
	def setUp(self):                      #runs before every test
		self.tmA = TaskManager("A")
		self.tmB = TaskManager("B")
	def test_adding_deleting(self):       #must start with test_...
		print "Test: Multiple Add , Delete and Print"
		tm = self.tmA                      
		tm = TaskManager("A")
		tm.add_task(Task("Buy milk","Done","Trivial"))
		tm.add_task(UrgentTask("Pay rent","Done"))
		tm.add_task(ImportantTask("Learn Python Classes","Pending"))
		print tm
		tm.del_task(1)
		tm.do_task(2)
		print tm
		print self.tmB
		self.assertEqual(len(tm.tasklist),2)
	def test_delete(self):
		print "Test: Delete Non-Existent Task"
		tm = self.tmA
		tm.del_task(100)
	def test_Multitask(self):
		self.tmA.add_task(Task("Buy milk","Done","Trivial"	))
		self.assertNotEqual(self.tmA.size() , self.tmB.size())
	def test_NumberInputs(self):
		self.tmA.add_task(Task(1,1,1))
if __name__ == "__main__":
	unittest.main()