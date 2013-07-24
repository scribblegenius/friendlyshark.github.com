import sys
try:
	meal = float(sys.argv[1])
	tax = float(sys.argv[2])/100
	tip = float(sys.argv[3])/100
	tax_value = (meal*tax)
	meal_with_tax =  meal + tax_value
	tip_value = meal_with_tax * tip
	total = meal_with_tax + tip_value
	print "python tip_calculator.py"
	print "The base cost of of your meal was $%s" % meal
	print "You need to pay $%s for tax." % (tax_value)
	print "Tipping at a rate of {0}%, you should leave ${1} for a tip.".format( tip*100,tip_value)
	print "The grand total of your meal is $%s."% (total)
except Exception as e:
	print " Input values should be numbers! \n Exiting..."
sys.exit(0)