import simplegui

"""
Given the three function print_color(), set_red(), and set_blue() in the program
template below, create three buttons that print and manipulate the global
variable color. Use the CodeSkulptor Docs to determine the SimpleGUI method for
creating a button if needed.

This code can only be run in https://py3.codeskulptor.org/ since simplegui
only works there. Create an interactive console thet greets the user.
"""

color = "black"

def set_red():
    global color
    color = "red"
    frame.set_canvas_background(color)
    
def set_blue():
    global color
    color = "blue"
    frame.set_canvas_background(color)
    
def print_color():
    print (color)


# create frame
frame = simplegui.create_frame("Hello and Goodbye", 200, 200)
frame.set_canvas_background(color)

# register event handlers
frame.add_button("Red", set_red)
frame.add_button("Blue", set_blue)
frame.add_button("Color", print_color)

# get frame rolling
frame.start()