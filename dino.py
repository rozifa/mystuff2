def dino(a, b, c):
	if a > 1 and a < 5:
		return "NICE, %s, %s" % (b, c)
	elif a >= 5 and a <= 10:
		return "EXCELLENT, %s, %s" % (b, c)
	else:
		return "BRETTY GUD, %s, %s" % (b, c)

bobeeno = dino(3, 4, 5)
print bobeeno
print "fuck github"
print "i hope the repo rename worked ugh..."