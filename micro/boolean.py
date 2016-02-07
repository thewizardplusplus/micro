class boolean:
	def __init__(self, value):
		self.value = bool(value)

	def __nonzero__(self):
		return self.value

	def __eq__(self, value):
		return self.value == bool(value)

	def __ne__(self, value):
		return self.value != bool(value)

	def __repr__(self):
		return str(self.value).lower()
