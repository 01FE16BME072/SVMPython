class Name:
	def __init__(self,name):
		self.name = name
	def saying(self):
		print(self.name)
		return self.name

n = Name('Keerthi')
n.saying()