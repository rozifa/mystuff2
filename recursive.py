def function(number):
	if number == 0:
		print "Finished"
	else:
		print "Working"
		return function(number - 1)