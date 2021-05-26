
"""
Write a program that estimate the population growth. The rates of change are the
following:

- A birth every 7 seconds
- A death every 13 seconds
- A new immigrant every 35 seconds

Assume that the current population is 307'357,870, and that there are exactly
365 days in the year.
"""
import datetime

CURRENT_POPULATION = 307357870
CURRENT_DATETIME = datetime.datetime.now()
CURRENT_DATE = CURRENT_DATETIME.date()
CURRENT_YEAR = CURRENT_DATE.strftime("%Y")

BIRTH_RATE = 7
DEATH_RATE = 13
IMMIGRANT_RATE = 35

class Population_estimation():
	"""
	Estimate the population growth.
	"""
	def __init__(self, birth_rate):
		self.birth_rate = birth_rate
		self.yearly_population = self.birth_growth(self.birth_rate)

	def birth_growth(self, birth_rate):
		"""
		Calculates the birth growth of a year.
		"""
		birth_year_growth = birth_rate*60*24*365

		return birth_year_growth

print(Population_estimation(birth_rate=BIRTH_RATE).yearly_population)