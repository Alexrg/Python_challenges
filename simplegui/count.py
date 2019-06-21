import simplegui
"""
Challenge: Given the program template below, implement four buttons that
manipulate a global variable count as follows. The function reset() sets the
value of count to be zero, the function increment() adds one to count, the
function decrement() subtracts one from count, and the function print_count()
prints the value of count to the console.

This code can only be run in https://py3.codeskulptor.org/ since simplegui
only works there. Create an interactive console thet greets the user.
"""
count = 0

def reset():
	"""
	Set the counter back to zero
	"""
	global count
	count = 0

def increment():
	"""
	Increment the counter by one
	"""
	global count
	count += 1

def decrement():
	"""
	Decrement the counter by one
	"""
	global count
	count -= 1

def print_count():
	"""
	Print the counter to the user
	"""
	global count
	print(count)

# create frame
frame = simplegui.create_frame("Count", 200, 200)

# register event handlers
frame.add_button("Reset", reset)
frame.add_button("Increment", increment)
frame.add_button("Decrement", decrement)
frame.add_button("Print Count", print_count)

# get frame rolling
frame.start()