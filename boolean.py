class boolean:
	def __nonzero__(self):
		return self == true

	def __repr__(self):
		return 'true' if self else 'false'

true = boolean()
false = boolean()

def to_boolean(value):
	return true if value else false
