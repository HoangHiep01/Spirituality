import numpy as np

class RandomApp:

	def __init__(self, listOption = []):
		self._listOption = listOption


	def setOption(self, option):
		self._listOption = option

	def addOption(self, option):
		for opt in option:
			self._listOption.append(opt)

	def getChoice(self):

		self._choose = np.random.choice(self._listOption)
		return self._choose
