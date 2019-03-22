"""
The Great Lakes in the United States contain roughly 22% of the world fresh
surface water (22,810 km^3). It is hard to conceive how much water that is.
Write a program to calculate how deep it would be if all the water in the
Great Lake was spread evenly accross the 48 continguous U.S. states. You
will need to do some Internet research to determine the area of that region.
"""
# A cubic meter also equals 1000 liters or a million cubic centimeters.
# Cubic
GREAT_LAKE_WATER = 22810

# Cuadratic
CALIFORNIA_SURFACE = 423972
NEVADA_SURFACE  = 286380
UTAH_SURFACE  = 219882
ARIZONA_SURFACE  = 295234
COLORADO_SURFACE  = 269601
NUEVO_MEXICO_SURFACE  = 314917


STATES = [california_surface,nevada_surface,utah_surface,arizona_surface,
colorado_surface,nuevo_mexico_surface
]


def sum_surfaces(states):
	"""
	Sum the surfaces of the 48 continguous states

	Args:
		states: An array with all the surfaces

	Returns:
		sum_states_surfaces: Sums all the surfaces of the array in the argument
	"""
	sum_states_surfaces = 0
	
	for surface in states:
		sum_states_surfaces += surface

	return sum_states_surfaces


# Calculate the volume using the surface of 48 states
total_surface = sum_surfaces(states)

