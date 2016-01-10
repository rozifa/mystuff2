class Animals(object):

	def __init__(self, name, species, hair, likeable):
		self.name = name
		self.hair = hair
		self.likeable = likeable
		self.species = species

	def get_name(self):
		return self.name

	def get_hair(self):
		return self.hair

	def get_likeable(self):
		return self.likeable

	def get_species(self):
		return self.species

	def get_nickname(self):
		return self.

# Create the animals (objects)

mrmeow = Animals('Mr.Meow', 'Cat', 'Short-hair', 'He is ok')
fudgems = Animals('Fudgems', 'Cat', 'Long and fluffy', 'One of the best')
pistachio = Animals('Pistachio', 'Cat', "Nice N' Short", 'As good as Fudgems')
bingus = Animals('Bingus', 'Dog', 'Spotted', 'He nice')

meow_one = [mrmeow.get_name(), mrmeow.get_species(), mrmeow.get_hair(), mrmeow.get_likeable()]
meow_two = [fudgems.get_name(), fudgems.get_species(), fudgems.get_hair(), fudgems.get_likeable()]
meow_three = [pistachio.get_name(), pistachio.get_species(), pistachio.get_hair(), pistachio.get_likeable()]
pupper = [bingus.get_name(), bingus.get_species(), bingus.get_hair(), bingus.get_likeable()]

statstr = "This animal's stats are: "

print statstr, meow_one
print statstr, meow_two
print statstr, meow_three
print statstr, pupper

print "WOW! I understand how classes and objects work in Python now...I think."