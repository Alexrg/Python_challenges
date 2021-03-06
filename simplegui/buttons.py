import simplegui

"""
This code can only be run in https://py3.codeskulptor.org/ since simplegui
only works there. Create an interactive console thet greets the user.
"""

def print_goodbye():
    """
    Returns a "Goodbye" message to the user

    Returns:
        messafe (string): A "Goodbye" message to the user
    """
    message = "Goodbye"
    print(message)


def print_hello():
    """
    Returns a "Goodbye" message to the user

    Returns:
        messafe (string): A "Goodbye" message to the user
    """
    message = "Hello"
    print(message)

# create frame
frame = simplegui.create_frame("Hello and Goodbye", 200, 200)

# register event handlers
frame.add_button("Hello", print_hello)
frame.add_button("Goodbye", print_goodbye)

# get frame rolling
frame.start()