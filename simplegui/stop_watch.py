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