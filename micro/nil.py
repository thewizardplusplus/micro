class nil:
	def __nonzero__(self):
		return False

	def __repr__(self):
		return self.__class__.__name__

nil_instance = nil()
