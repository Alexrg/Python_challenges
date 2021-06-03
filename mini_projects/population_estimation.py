
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
CURRENT_YEAR = int(CURRENT_DATE.strftime("%Y"))

BIRTH_RATE = 7
DEATH_RATE = 13
IMMIGRANT_RATE = 35

year_to_calculate = 2024

class Population_estimation():
	"""
	Estimate the population growth.
	"""
	def __init__(self, current_population,birth_rate, death_rate, current_year, year_to_calculate):
		self.current_population = int(current_population)
		self.birth_rate = birth_rate
		self.death_rate = death_rate
		self.current_year = current_year
		self.year_to_calculate = int(year_to_calculate)
		self.yearly_growth = self.yearly_calculation()

	def birth_growth(self):
		"""
		Calculates the birth growth of a year.
		"""
		birth_year_growth = (60/self.birth_rate)*60*24*365

		return birth_year_growth

	def death_growth(self):
		"""
		Calculates the death growth of a year.
		"""
		death_year_growth = (60/self.death_rate)*60*24*365

		return death_year_growth

	def yearly_calculation(self):
		"""
		Estimates the population growth in a year
		"""
		years_to_calculate = self.year_to_calculate - self.current_year

		yearly_population = 0

		for years in range(1,years_to_calculate):
			yearly_population += int(self.current_population + self.birth_growth() - self.death_growth())

		return yearly_population



population = Population_estimation(current_population=CURRENT_POPULATION,birth_rate=BIRTH_RATE, death_rate=DEATH_RATE,
	current_year=CURRENT_YEAR, year_to_calculate=year_to_calculate)
yearly_population = population.yearly_growth

print("{} population: {}".format(CURRENT_YEAR, CURRENT_POPULATION))
print("{} population: {}".format(year_to_calculate, yearly_population))