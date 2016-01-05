class Drinks(object):

	def __init__(self, name, producer, flavor):
		self.name = name
		self.producer = producer
		self.flavor = flavor

	def get_name(self):
		return self.name

	def get_prducer(self):
		return self.producer

	def get_flavor(self):
		return self.flavor

cola = Drinks("Coca Cola", "Coca-Cola-Global", "Ok")
sierra_mist = Drinks("Sierra Mist", "Pepsico", "Good")
orange_soda = Drinks("Crush", "Cali. Beverage", "Excellent")

big = cola.get_name()

print big
