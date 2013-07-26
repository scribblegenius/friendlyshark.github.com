from optparse import OptionParser
import sys
try:
	parser = OptionParser()
	parser.add_option("-m", "--meal", dest="meal", help="base meal cost")
	parser.add_option("-x", "--tax", dest="tax", help="tax percentage")
	parser.add_option("-t", "--tip", dest="tip", help="tip percentage")
	(options,args) = parser.parse_args()
	meal = float(options.meal)
	tax = float(options.tax)/100
	tip = float(options.tip)/100
	tax_value = meal * tax
	meal_with_tax =  meal + tax_value
	tip_value = meal_with_tax * tip
	total = meal_with_tax + tip_value
	print "python tip_calculator.py"
	print "The base cost of of your meal was $%s" % meal
	print "You need to pay $%s for tax." % (tax_value)
	print "Tipping at a rate of {0}%, you should leave ${1} for a tip.".format( tip*100,tip_value)
	print "The grand total of your meal is $%s."% (total)
except Exception as e:
	print "Inputs should be numbers!\nExiting..."
