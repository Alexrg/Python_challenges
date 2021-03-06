import simplegui
import time
"""
Our mini-project for this week will focus on combining text drawing in the
canvas with timers to build a simple digital stopwatch that keeps track of the
time in tenths of a second. The stopwatch should contain "Start", "Stop" and
"Reset" buttons.

This code can only be run in https://py3.codeskulptor.org/ since simplegui
only works there. Create an interactive console thet greets the user.
"""
clock = 0
stop_counter = 0
seconds = 0
success = 0
attempts = 0

def time_format(clock):
    """
    Gives format to the stopwatch
    """
    global seconds
    
    seconds = clock/10
    minutes = int(seconds/60)
    string_minutes = str(minutes)
    seconds = round((seconds - (minutes * 60)),2)
    string_seconds = str(seconds)
    
    if len(string_minutes) == 1 :
        string_minutes = "0"+str(minutes)
    
    if len(string_seconds) == 3 :
        string_seconds = "0"+str(seconds)
    
    format_clock = "{}:{}".format(string_minutes,string_seconds)
    
    return format_clock

def clock_counter():
    """
    The clock stop counter
    """
    global clock
    clock += 1

def start():
    """
    Starts the timer
    """
    timer.start()

def stop():
    """
    Stops the timer
    """
    global stop_counter
    global seconds
    global success
    global attempts
    
    print(seconds)
    seconds = str(seconds).split('.0')
    
    if len(seconds) == 2:
        success += 1
    else:
        attempts += 1
    
    timer.stop()
    stop_counter += 1
    
    print("Number of times stoped: {}".format(stop_counter))

def reset():
    """
    Starts the timer from zero
    """
    global clock
    global stop_counter
    
    clock = 0
    stop_counter = 0

def background_draw(canvas):
    """
    Draws the timer numbers in the background
    """
    global success
    global attempts
    
    game_text = "{}/{}".format(attempts,success)
    canvas.draw_text(str(game_text), (10, 50), 40, 'Red')
    format_clock = time_format(clock)
    canvas.draw_text(str(format_clock), (50, 100), 40, 'Red')

# create frame
frame = simplegui.create_frame("Stop watch", 200, 200)
timer = simplegui.create_timer(100, clock_counter)
frame.set_draw_handler(background_draw)

# register event handlers
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# get frame rolling
frame.start()