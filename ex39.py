### Code without module ###
# # create a dash printing function so I don't have to continuously retype it
# def dash():
# 	print '-' * 20

# # create a mapping of state to abbreviation
# states = {
# 	'Oregon': 'OR',
# 	'Florida': 'FL',
# 	'California': 'CA',
# 	'New York': 'NY',
# 	'Michigan': 'MI'
# }

# # create a basic set of states and some cities in them
# cities = {
# 	'CA': 'San Francisco',
# 	'MI': 'Detroit',
# 	'FL': 'Jacksonville'
# }

# # add some more cities
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'

# # print out some of the cities
# dash()
# print "NY State has: ", cities['NY']
# print "OR State has: ", cities['OR']

# # print some states
# dash()
# print "Michigan's abriviation is: ", states['Michigan']
# print "FLorida's abriviation is: ", states['Florida']

# #do it by using the state then cities dict
# dash()
# print "Michigan has: ", cities[states['Michigan']]
# print "Florida has: ", cities[states['Florida']]

# # print every state abbreviation
# dash()
# for state, abbrev in states.items():
# 	print "%s is abbreviated %s" % (state, abbrev)

# # print every city in state
# dash()
# for abbrev, city in cities.items():
# 	print "%s has the city %s" % (abbrev, city)

# # now do both at the same time
# dash()
# for state, abbrev in states.items():
# 	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

# # safely get an abbreviation by state that might not be there
# dash()
# state = states.get('Texas')	

# if not state:
# 	print "Sorry, no Texas."

# # get a city with a default value
# city = cities.get('TX', 'Does Not Exist')
# print "The city for the state 'TX' is: %s" % city

### Code with self-made module ###

import hashmap

def dash():
	print '-' * 20

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI') 

# create basic set of states and cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print out some cities
dash()
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

# print some states
dash()
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

# do so by using the state then cities dict
dash()
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print 'Florida has: %s' % hashmap.get(cities, hashmap.get(states, 'Florida'))

# print every state abbreviation
dash()
hashmap.list(states)

# print every city in state
dash()
hashmap.list(cities)

dash()
state = hashmap.get(states, 'Texas')

if not state:
	print "Sorry, no Texas."

# default values using ||= with the nil result
# can I do this on one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city