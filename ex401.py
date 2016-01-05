class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def make_song(self):
		for line in self.lyrics:
			print line


puff = Song(['puff the magic dragon',
	         'lived by the sea',
	         'what a cool fucking dragon'])

immigrant = Song(['come from the land of the ice and snow',
	             'midnight sun where the hot springs blow',
	             'AHHHHHHHHHHHHHH!'])

puff.make_song()
immigrant.make_song()

# print puff
# print immigrant