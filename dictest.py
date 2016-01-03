family = {
	'Din': 'Memer',
	'Alisa': 'Worker',
	'Razifa': 'Crazy',
	'Salko': 'Angry'
}

emotions = {
	'Memer': 'Funny',
	'Worker': 'Bookish',
	'Craxy': 'Insane',
	'Angry': 'Impulsive'
}

print "%s is the older brother" % family['Din']

for name, attribute in family.items():
	print name, attribute