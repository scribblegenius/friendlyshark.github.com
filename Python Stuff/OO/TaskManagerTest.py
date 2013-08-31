import random
import unittest
from Task import *
from TaskManager import TaskManager
class TaskManagerTest(unittest.TestCase):
	def setUp(self):                      #runs before every test
		print "--------------------------------------------------------------"
		self.tmA = TaskManager("A")
		self.tmB = TaskManager("B")
		print "--------------------------------------------------------------\n"
	def test_adding_deleting(self):       #must start with test_...
		print "Test: Multiple Add , Delete and Print\n"
		tm = self.tmA
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
		print "Test: Delete Non-Existent Task\n"
		tm = self.tmA
		tm.del_task(100)
	def test_Multitask(self):
		print "Test: Check if multiple taskmanagers can be created\n"
		self.tmA.add_task(Task("Buy milk","Done","Trivial"	))
		self.tmA.add_task(Task("Buy car","Done","Important"	))
		self.tmA.add_task(Task("Buy jet","Done","Trivial"	))
		self.tmB.add_task(Task("Move to Mars","Pending","Important"	))
		self.assertNotEqual(self.tmA.size() , self.tmB.size())
	def test_NumberInputs(self):
		args = [1,1.4,'\t']
		print "Test: Handle special input {0} \n".format(args)
		self.tmA.add_task(Task(*args))
		self.assertEqual(self.tmA.size(),1)
	def test_Duplicate_Add_Not_Allowed(self):
		print "Test: Handle Duplicate Task Adds\n"
		self.tmA.add_task(Task("Pay monthly electricity bill","Done","Urgent"))
		self.tmA.add_task(Task("Pay monthly electricity bill","Done","Urgent"))
		self.assertEqual(self.tmA.size(),1)
if __name__ == "__main__":
	unittest.main()