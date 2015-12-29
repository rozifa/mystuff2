def dash():
	print '-' * 25

print "Welcome to Meme Fuck"
dash()
print "Enjoy my dude!"
dash()

print "What is your name?"
usr_name = raw_input("> ")

print "Hello %s." % usr_name

print "You wake up in a dark room"
c1 = raw_input("> ")

if c1 == "look around" or "Look around" or "Look Around":
	print "You see three doors."

c2 = raw_input("> ")

if c2 == "inspect doors":
	print "Door one is made of wood."
	print "Door two is made of metal."
	print "Door three is transparent."

c3 = raw_input("> ")

print "Have you considered suicide..."

c4 = raw_input("> ")

if c4 == "Yes" or "yes":
	print "Congratulations! You have realized the transient and pointless nature of human existance."
elif c4 == "No" or "no":
	print "Consider it..."
if c4 == "kill myself":
	print "Are you sure?"
	print "Yes / No"

c5 = raw_input("Kill yourself?... ")

if c5 == "Yes":
	print "Congrat! R.I.P. "
elif c5 == "No":
		print "Do it feggit..."











