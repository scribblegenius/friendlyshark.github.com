import random
import unittest
from Task import *
from TaskManager import TaskManager
class TaskManagerTest(unittest.TestCase):
	def setUp(self):                      #runs before every test
		print "\n\n\n--------------------------------------------------------------"
		self.tmA = TaskManager("A")
		self.tmB = TaskManager("B")
		print "--------------------------------------------------------------\n"
	def test_adding_deleting(self):       #must start with test_...
		print "Test 4: Multiple Add , Delete and Print\n"
		tm = self.tmA
		tm.add_task(Task("Buy milk","Done","Trivial"))
		tm.add_task(UrgentTask("Pay rent","Done"))
		tm.add_task(ImportantTask("Learn Python Classes","Pending"))
		print tm
		tm.del_task(1)
		tm.do_task(2)
		print tm
		self.tmB.add_task(Task("Buy gold","Done","Pending"))
		self.tmB.add_task(ImportantTask("Conquer self","Done"))
		tm.add_task(ImportantTask("Learn Python Classes","Pending"))
		print self.tmB
		self.assertEqual(len(tm.tasklist),2)
	def test_delete(self):
		print "Test 5: Delete Non-Existent Task\n"
		tm = self.tmA
		tm.del_task(100)
	def test_Multitask(self):
		print "Test 2: Check if multiple taskmanagers can be created\n"
		self.tmA.add_task(Task("Buy milk","Done","Trivial"	))
		self.tmA.add_task(Task("Buy car","Done","Important"	))
		self.tmA.add_task(Task("Buy jet","Done","Trivial"	))
		self.tmB.add_task(Task("Move to Mars","Pending","Important"	))
		print "\n\n"
		print self.tmA 
		print "\n\n"
		print self.tmB 
		self.assertNotEqual(self.tmA.size() , self.tmB.size())
	def test_NumberInputs(self):
		args = [1,1.4,100000000]
		print "Test 3: Handle special input {0} \n".format(args)
		self.tmA.add_task(Task(*args))
		self.assertEqual(self.tmA.size(),1)
	def test_Duplicate_Add_Not_Allowed(self):
		print "Test 1: Handle Duplicate Task Adds\n"
		self.tmA.add_task(Task("Pay monthly electricity bill","Done","Urgent"))
		self.tmA.add_task(Task("   pay MONTHLy ELECTRICity BIll   ","Done","Urgent"))
		self.assertEqual(self.tmA.size(),1)
if __name__ == "__main__":
	print "\n\n\nRunning Test Suite: "
	unittest.main()